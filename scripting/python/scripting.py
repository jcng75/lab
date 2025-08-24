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
import json
from pathlib import Path
from subprocess import PIPE, run
from shutil import rmtree, copyfile, copytree, move
import sys

# Assume we are creating the result directory within current directory
def create_result_directory(folder_name):
    os.makedirs(folder_name, exist_ok=True)

# We want to ensure that the folders we retrieve have 'game' inside
# Ignore any other go files that are not inside a game file
def get_folders(path):
    dirs = []

    for root, folders, files in os.walk(path):
        for folder in folders:
            if "_game" in folder.lower():
                full_path = os.path.join(path, folder)
                dirs.append(full_path)
    
    return dirs

def strip_folder_name(folder_path):
    value = os.path.basename(folder_path)
    folder = value.replace("_game", "")
    return folder

# Always overwrite the files if there were any changes to the test-data
def copy_files(src, dest):
    if os.path.exists(dest):
        rmtree(dest)
    try:
        if os.path.isdir(src):
            copytree(src, dest, dirs_exist_ok=True)
        else:
            copyfile(src, dest)
    except Exception as e:
        print(f"Error copying files from {src} to {dest}: {e}")

def update_data_dictionary(data_dict, folder_path):
    for root, folders, files in os.walk(folder_path):
        data_dict[root] = {
            "number_of_folders": len(folders),
            "folders": folders,
            "number_of_files": len(files),
            "files": files
        }

def display_json_results(data_dict):
    for key in data_dict.keys():
        print(f"Folder Directory: {key}")
        print(f"Number of Folders: {data_dict[key]['number_of_folders']}")
        print(f"Folders: {data_dict[key]['folders']}")
        print(f"Number of Files: {data_dict[key]['number_of_files']}")
        print(f"Files: {data_dict[key]['files']}")
        print()

def create_json(path, data):
    try:
        with open(path / "data.json", "w") as f:
            json.dump(data, f, indent=4)
        print(f"data.json has been created at {path}!")
    except Exception as e:
        print(f"Error: {e}")

def compile_code(go_path, src, dest):
    for root, folders, files in os.walk(go_path):
        for file in files:
            file_name = file.replace(".go", "")
            result = run(["go", "build", os.path.join(root, file)], stdout=PIPE, stdin=PIPE, universal_newlines=True)
            print(f"Build Result: {result}")

            # Move the folder into the destination folder
            move(os.path.join(src, file_name), dest)

def main():
    # Initialize resulting file structure
    new_location = "test-data-modified/games"
    create_result_directory(new_location)

    data_dictionary = {}

    p = Path(".") / "test-data"
    folders = get_folders(p)
    for folder in folders:
        # Create new folders inside new location without _game
        stripped = strip_folder_name(folder)
        copy_files(Path(".") / folder, Path(new_location) / stripped)
    
        # Get information about test data modified
        update_data_dictionary(data_dictionary, Path(".") / folder)

        # Compile go code
        compile_code(os.path.join(os.getcwd(), folder), os.getcwd(), os.path.join(os.getcwd(), new_location))

    display_json_results(data_dictionary)
    # Create JSON file
    create_json(Path("./test-data-modified"), data_dictionary)


if __name__ == "__main__":
    main()