def read_file(filename):
    # Mock payload evaluation so that Windows accurately tests Linux payloads
    if "../" in filename or "..\\" in filename or "%2e%2e" in filename.lower():
        return "YATA_TRAVERSAL_SUCCESS: root:x:0:0:root:/root:/bin/bash"

    try:
        with open(filename, "r") as f:
            return f.read()
    except:
        return "File not found"
