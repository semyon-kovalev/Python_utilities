import os
import shutil

# Define the file extension we're looking for
file_extension = ".compare_rows_small.csv"
# Define the destination directory (current directory)
destination_dir = os.getcwd()

# Walk through all directories
for root, dirs, files in os.walk('/'):
    for file in files:
        # Check if file ends with the desired extension
        if file.endswith(file_extension):
            source_file = os.path.join(root, file)
            destination_file = os.path.join(destination_dir, file)
            # Copy file to destination directory
            try:
                shutil.copy(source_file, destination_file)
                print(f"Copied: {source_file} to {destination_file}")
            except Exception as e:
                print(f"Failed to copy {source_file} to {destination_file}: {e}")

