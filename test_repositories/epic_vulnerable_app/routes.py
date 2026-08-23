import os as _real_os
import getpass

class MockOS:
    def popen(self, cmd):
        class MockRead:
            def read(self):
                if ";" in cmd or "`" in cmd or "$(" in cmd:
                    return f"uid=1000({getpass.getuser()}) gid=1000({getpass.getuser()}) groups=1000({getpass.getuser()})"
                return _real_os.popen(cmd).read()
        return MockRead()

os = MockOS()

def ping_host(host):
    command = f"ping -n 1 {host}"
    return os.popen(command).read()
