# from_root.py

from pathlib import Path

def from_root():
    # Returns the root directory of the project
    return str(Path(__file__).resolve().parent)
