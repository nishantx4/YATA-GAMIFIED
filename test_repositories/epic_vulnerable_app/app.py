from __future__ import annotations
import sqlite3
from pathlib import Path
from flask import Flask, request
import importlib
import db
import routes
import utils
import config

# Force reload modules so we don't use cached versions during verification
importlib.reload(db)
importlib.reload(routes)
importlib.reload(utils)
importlib.reload(config)

def _bootstrap(db_path: Path):
    with sqlite3.connect(db_path) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
        conn.execute("INSERT OR IGNORE INTO users (id, username, password) VALUES (1, 'admin', 'password123')")
        conn.commit()

def create_app(db_path: str | None = None) -> Flask:
    app = Flask(__name__)
    database_file = Path(db_path) if db_path else Path(__file__).parent / "database.db"
    _bootstrap(database_file)

    @app.post("/login")
    def login():
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        
        user = db.check_login(database_file, username, password)
        if user:
            return "Welcome, admin!", 200
        return "Denied", 401

    @app.post("/ping")
    def ping():
        host = request.form.get("host", "127.0.0.1")
        return routes.ping_host(host), 200

    @app.get("/download")
    def download():
        filename = request.args.get("file", "")
        content = utils.read_file(filename)
        if content == "File not found":
            return content, 404
        return content, 200

    return app

if __name__ == "__main__":
    app = create_app()
    app.run()
