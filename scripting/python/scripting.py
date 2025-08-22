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
def create_result_directory(cwd, folder_name):
    items = os.listdir(cwd)
    for item in items:
        item_path = os.path.join(cwd, item) 
        if os.path.isdir(item_path) and item == folder_name:
            print(f"{folder_name} already exists - Skipping Creation process")
            return

    os.mkdir(folder_name)
    return
    

def main():
    p = Path(".")
    create_result_directory(p, "test-data-modified")



if __name__ == "__main__":
    main()