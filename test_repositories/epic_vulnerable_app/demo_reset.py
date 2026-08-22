import os
import shutil
import sys
from pathlib import Path

# Ensure emoji prints correctly on Windows CMD/PowerShell
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

# Path to the memory file
YATA_ROOT = Path("D:/HackathonProjects/yata")
MEMORY_DIR = YATA_ROOT / ".yata" / "memory"
REPO_MEMORY = MEMORY_DIR / "epic_vulnerable_app"

def reset_demo():
    print("--- RESETTING DEMO ENVIRONMENT ---")
    
    # 1. Reset Git
    print("[1] Reverting source code to vulnerable state...")
    os.system("git checkout -- .")
    os.system("git clean -fd .")

    # 2. Clear YATA Memory
    print("[2] Clearing YATA memory for this repo...")
    if REPO_MEMORY.exists():
        shutil.rmtree(REPO_MEMORY)
        print("    -> Memory wiped! YATA will analyze this like a fresh repo.")
    else:
        print("    -> Memory already clean.")

    # 3. Clean any existing YATA sandbox
    sandbox = YATA_ROOT / ".yata" / "sandbox" / "epic_vulnerable_app"
    if sandbox.exists():
        print("[3] Clearing YATA sandbox...")
        shutil.rmtree(sandbox)

    print("\n\u2705 Reset complete! You can now run:")
    print("yata assess . --interactive")

if __name__ == "__main__":
    reset_demo()
