import os
from pathlib import Path

def tree(path, prefix="", last=True):
    p = Path(path)
    print(f"{prefix}{'|___ ' if last else '├── '}{p.name}")
    
    if p.is_dir():
        items = sorted(p.iterdir(), key=lambda x: (x.is_file(), x.name))
        for i, item in enumerate(items):
            tree(item, prefix + ("    " if last else "|   "), i == len(items) - 1)

folder = input("Enter folder path (or press Enter for current): ") or "."
if Path(folder).exists():
    tree(folder)
else:
    print("Folder not found!")