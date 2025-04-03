import os

def list_files_in_directory():
    """
    Prints all files in the current working directory.
    """
    current_directory = os.getcwd()
    files = [f for f in os.listdir(current_directory) if os.path.isfile(os.path.join(current_directory, f))]
    if files:
        print("Files in the current working directory:")
        for file in files:
            print(file)
    else:
        print("No files found in the current working directory.")
