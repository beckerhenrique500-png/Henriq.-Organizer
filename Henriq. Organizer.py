import os
import shutil
from pathlib import Path

def exists():
    if os.path.exists(rf"{path1}\{file1.suffix[1:]}"):
        return True
    
def exists2():
    if os.path.exists(rf"{path1}\{file1.suffix[1:]}\{file1}"):
        return True
    
def create():
    if not exists():
        os.mkdir(rf"{path1}\{file1.suffix[1:]}")
    
    if not exists2():
        shutil.move(rf"{path1}\{file1}", rf"{path1}\{file1.suffix[1:]}")

print("Henriq. Organizer by @henriqueosdev TIKTOK\n")

path1 = input(r"Enter the folder path (or drag it): ").strip('"')
path2 = os.listdir(path1)

for i in path2:
    file1 = Path(i)
    create()

print("Done.")
