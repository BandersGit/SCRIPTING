import shutil
from pathlib import Path

current_folder = Path.cwd()

copies_folder = current_folder / "copies"

copies_folder.mkdir(exist_ok=True)

shutil.copy2("test.ini", copies_folder / "test.bak.ini")
