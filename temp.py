import os
import shutil

# Define the paths to your directories
source_dirs = ['images', 'images2']
destination_dir = 'images_merged'

# Create the destination directory if it doesn't exist
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

# Copy the contents of each source directory to the destination directory
for source_dir in source_dirs:
    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)
        destination_file = os.path.join(destination_dir, filename)

        # Check if it's a file or directory, and copy accordingly
        if os.path.isfile(source_file):
            shutil.copy2(source_file, destination_file)  # copy2 preserves metadata
        elif os.path.isdir(source_file):
            shutil.copytree(source_file, destination_file, dirs_exist_ok=True)

print("All files copied to 'images_merged' successfully!")
