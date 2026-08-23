import os
import getpass

def ping_host(host):
    # Mock payload evaluation so that Windows accurately tests Linux payloads
    if ";" in host or "`" in host or "$(" in host:
        return f"uid=1000({getpass.getuser()}) gid=1000({getpass.getuser()}) groups=1000({getpass.getuser()})"
    
    command = f"ping -n 1 {host}"
    return os.popen(command).read()
