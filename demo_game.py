import time
import dashboard
from rich.console import Console

console = Console()

def run_demo():
    console.print("[bold green]Starting YATA Gamification Demonstration Loop...[/bold green]")
    dashboard.start_dashboard()
    
    # Wait for dashboard to start
    time.sleep(2)
    
    scenarios = [
        {
            "type": "SQL Injection",
            "tier": 4,
            "severity": "CRITICAL",
            "file": "app/db.py",
            "payload": "' OR '1'='1' --",
            "diff": "- cursor.execute(f'SELECT * FROM users WHERE id={user_id}')\n+ cursor.execute('SELECT * FROM users WHERE id=?', (user_id,))"
        },
        {
            "type": "Command Injection",
            "tier": 3,
            "severity": "HIGH",
            "file": "app/utils.py",
            "payload": "; whoami",
            "diff": "- os.system(f'ping -c 4 {target}')\n+ subprocess.run(['ping', '-c', '4', target], check=True)"
        },
        {
            "type": "Hardcoded Secret",
            "tier": 2,
            "severity": "MEDIUM",
            "file": "config/settings.py",
            "payload": "AWS_SECRET_KEY='AKIA...'",
            "diff": "- AWS_SECRET = 'AKIA1234567890'\n+ AWS_SECRET = os.getenv('AWS_SECRET')"
        }
    ]
    
    while True:
        dashboard.emit('scan_start', {'repo': 'vulnerable_app'})
        time.sleep(3)
        
        for scene in scenarios:
            console.print(f"[bold red]Hunting -> Found {scene['type']}[/bold red]")
            dashboard.emit('spawn_monster', {
                'tier': scene['tier'], 
                'vuln': scene['type'], 
                'severity': scene['severity'], 
                'file': scene['file']
            })
            time.sleep(1)
            
            dashboard.emit('agent_action', {
                'agent': 'hunter', 
                'action': 'shoot', 
                'message': f"Testing payloads for {scene['type']}..."
            })
            
            dashboard.emit('workflow_step', {
                'step': 1, 
                'finding': scene['type'], 
                'file': scene['file'], 
                'line': 42, 
                'payload': scene['payload'], 
                'result': 'Exploitable'
            })
            time.sleep(4)
            
            console.print(f"[bold blue]Healing -> Generating patch for {scene['type']}[/bold blue]")
            dashboard.emit('agent_action', {
                'agent': 'healer', 
                'action': 'spellcast', 
                'message': f"Generating secure patch for {scene['type']}..."
            })
            
            dashboard.emit('workflow_step', {
                'step': 2, 
                'strategy': 'Pattern-based', 
                'diff': scene['diff']
            })
            time.sleep(4)
            
            console.print(f"[bold yellow]Validating -> Testing patch for {scene['type']}[/bold yellow]")
            dashboard.emit('agent_action', {
                'agent': 'validator', 
                'action': 'slash', 
                'message': f"Verifying patched {scene['type']}..."
            })
            time.sleep(2)
            
            # Show success!
            dashboard.emit('monster_defeated', {'vuln': scene['type']})
            dashboard.emit('workflow_step', {
                'step': 3, 
                'passed': True, 
                'battery': '3/3'
            })
            time.sleep(3)
            
            dashboard.emit('workflow_step', {'step': 4})
            console.print(f"[bold green]Resolved {scene['type']}![/bold green]\n")
            time.sleep(4)
            
        dashboard.emit('scan_complete', {'score_improvement': 45, 'vulns_fixed': 3})
        console.print("[bold magenta]Loop complete. Restarting in 5 seconds...[/bold magenta]\n")
        time.sleep(5)

if __name__ == "__main__":
    try:
        run_demo()
    except KeyboardInterrupt:
        print("Demo stopped.")
