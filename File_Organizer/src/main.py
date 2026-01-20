# Copyright 2026 Jafet Valle <<jafet.valle@ucr.ac.cr / jaldova4@gmail.com>>
# Universidad de Costa Rica

import os
import sys
# sys.path.append("src") 

# from organizer import organize

def main():
    # instructions for the main function
    # organize(os.getcwd())
    path = os.getcwd()  # Get the current working directory
    test_path = os.path.join(path, "tests")
    os.makedirs("Music", exist_ok=True)
    os.makedirs("Documents", exist_ok=True)
    os.makedirs("Images", exist_ok=True)
    os.makedirs("Videos", exist_ok=True)
    print(os.listdir(path))  # List files in the current directory


    os.rmdir("Music")
    os.rmdir("Documents")
    os.rmdir("Images")
    os.rmdir("Videos")
    print("Directories created and removed successfully.")

    print(os.listdir(path))  # List files in the current directory after removal

if __name__ == "__main__":
    main()