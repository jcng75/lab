"""
This file is used to help us learn Python scripting.
This will read the files from the test-data directory and do the following:
- Concatenate all the *_game folders and it's files and move them all into one new single folder 'games'
- Remove the _game from each folder
- Create a .json file with information about each game
- Compile all of the game code
- Run all of the game code

This script was taken inspiration from TechWithTim, as the go files were copied from his repository: https://github.com/techwithtim/Python-Scripting-Project
"""

import os
from pathlib import Path
import subprocess

# Assume we are creating the result directory within current directory
def create_result_directory(folder_name):
    os.makedirs(folder_name, exist_ok=True)
    return

def get_folders(path):
    items = os.listdir(path)
    folders = []
    for item in items:
        test_path = os.path.join(path, item)
        if os.path.isdir(test_path):
            folders.append(item)
    return folders

def main():
    # Initialize resulting file structure
    new_location = "test-data-modified/games"
    create_result_directory(new_location)

    # Create new folders inside new location without _game
    p = Path(".") / "test-data"
    folders = get_folders(p)
    strip_game = lambda s: s.split("_game")[0]
    for folder in folders:
        stripped = strip_game(folder)
        create_result_directory(f"{new_location}/{stripped}")


if __name__ == "__main__":
    main()