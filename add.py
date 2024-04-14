import os
import os

# Define the root directory
root_dir = "./result"

# Loop through directories
for root, dirs, files in os.walk(root_dir):
    for dir in dirs:
        # Construct the path for version.txt
        version_file_path = os.path.join(root, dir, "version.txt")
        # Create an empty version.txt file
        open(version_file_path, 'a').close()
