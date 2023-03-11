import os

# Specify the folder path
folder_path = '/Users/amiaynarayan/Projects/photos/actual_images'

# Get a list of all the file names in the folder
file_names = os.listdir(folder_path)

# Open a file for writing the image names
with open('image_names.txt', 'w') as f:
    # Write each file name to a new line in the file
    for file_name in file_names:
        f.write(file_name + '\n')

