import os

def ping_host(host):
    command = f"ping -c 1 {host}"
    os.popen(command).read()
    return "Pong"
