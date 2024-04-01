import os
import shutil
import glob
import logging

logging.basicConfig(filename='file_organizer.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def organize_files(directory):
    try:
        os.chdir(directory)
        for file in glob.glob("*"):
            if os.path.isfile(file):
                file_type = get_file_type(file)
                create_directory(file_type)
                move_file(file, file_type)
        logging.info("Files organized successfully!")
    except Exception as e:
        logging.error(f"Error occurred while organizing files: {e}")

def get_file_type(file):
    file_extension = os.path.splitext(file)[1]
    if file_extension:
        return file_extension[1:].lower()  # remove the dot and convert to lowercase
    else:
        return "other"

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def move_file(file, directory):
    try:
        shutil.move(file, directory)
        logging.info(f"Moved file '{file}' to '{directory}'")
    except Exception as e:
        logging.error(f"Error occurred while moving file '{file}' to '{directory}': {e}")

if __name__ == "__main__":
    directory_path = input("Enter the directory path to organize files: ")
    backup_path = input("Enter the backup directory path: ")

    # Backup directory
    try:
        shutil.copytree(directory_path, backup_path)
        logging.info(f"Backup created successfully at '{backup_path}'")
    except Exception as e:
        logging.error(f"Error occurred while creating backup: {e}")

    organize_files(directory_path)
