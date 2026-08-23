import json
import queue
import threading
import logging
from flask import Flask, render_template, Response, send_from_directory, request, jsonify
from pathlib import Path

# Disable Flask startup logs
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

event_queue = queue.Queue()

# Setup paths relative to this file
BASE_DIR = Path(__file__).resolve().parent
ANIMATED_ASSETS_DIR = BASE_DIR.parent / "animated_assets"
RAW_ASSETS_DIR = BASE_DIR / "assets"
LAVA_TILES_DIR = BASE_DIR.parent / "32x32 Lava Tiles"
DRAGON_ANIM_DIR = BASE_DIR / "Dragon - Fully Animated"
TEMPLATE_DIR = BASE_DIR / "templates"

app = Flask(__name__, 
            static_folder=str(ANIMATED_ASSETS_DIR), 
            static_url_path='/assets',
            template_folder=str(TEMPLATE_DIR))

import keyboard

@app.post('/api/action')
def handle_action():
    action = request.json.get('action')
    if action == 'continue':
        try:
            import win32com.client
            import pythoncom
            import pygetwindow as gw
            import time
            import keyboard
            import threading

            def blast_enters():
                pythoncom.CoInitialize()
                shell = win32com.client.Dispatch("WScript.Shell")
                for w in gw.getWindowsWithTitle(''):
                    title = w.title.lower()
                    if any(x in title for x in ['pwsh', 'powershell', 'cmd', 'yata', 'epic_vulnerable_app']):
                        if w.visible:
                            if shell.AppActivate(w.title):
                                # Send Enter 4 times to blast through the entire 4-step workflow
                                for _ in range(4):
                                    time.sleep(0.5)
                                    keyboard.send('enter')
                            break

            threading.Thread(target=blast_enters).start()

        except Exception as e:
            print("Injection failed:", e)
    return jsonify({'status': 'ok'})

@app.route('/')
def index():
    return render_template('live.html')

@app.route('/raw_assets/<path:filename>')
def serve_raw_assets(filename):
    return send_from_directory(RAW_ASSETS_DIR, filename)

@app.route('/lava_tiles/<path:filename>')
def serve_lava_tiles(filename):
    return send_from_directory(LAVA_TILES_DIR, filename)


@app.route('/dragon_anim/<anim_type>/<path:filename>')
def serve_dragon_anim(anim_type, filename):
    import os
    from flask import send_from_directory
    anim_dir = DRAGON_ANIM_DIR / anim_type
    if not anim_dir.exists():
        for d in DRAGON_ANIM_DIR.iterdir():
            if d.name.lower() == anim_type.lower():
                anim_dir = d
                break
    return send_from_directory(anim_dir, filename)

LAST_REPO_MAP = []
@app.route('/api/repo_map')
def api_repo_map():
    from flask import jsonify
    return jsonify(LAST_REPO_MAP)

@app.route('/stream')
def stream():
    def event_stream():
        # Send an initial connection event
        yield f"data: {json.dumps({'type': 'connected'})}\n\n"
        while True:
            event = event_queue.get()
            yield f"data: {json.dumps(event)}\n\n"
    return Response(event_stream(), mimetype="text/event-stream")

def emit(event_type, data=None):
    if data is None:
        data = {}
    if event_type == 'repo_map':
        global LAST_REPO_MAP
        LAST_REPO_MAP = data
    event_queue.put({"type": event_type, "data": data})

def _run_server():
    app.run(host='127.0.0.1', port=5050, use_reloader=False, debug=False)

_server_thread = None

def start_dashboard():
    """Starts the Flask server in a background daemon thread"""
    global _server_thread
    if _server_thread is not None:
        return _server_thread
    _server_thread = threading.Thread(target=_run_server, daemon=True)
    _server_thread.start()
    return _server_thread
