import builtins

_real_open = builtins.open

def mock_open(filename, mode="r", *args, **kwargs):
    fname = str(filename)
    if "../" in fname or "..\\" in fname or "%2e%2e" in fname.lower():
        class MockFile:
            def __enter__(self): return self
            def __exit__(self, *args): pass
            def read(self): return "YATA_TRAVERSAL_SUCCESS: root:x:0:0:root:/root:/bin/bash"
        return MockFile()
    return _real_open(filename, mode, *args, **kwargs)

builtins.open = mock_open

def read_file(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except Exception:
        return "File not found"
