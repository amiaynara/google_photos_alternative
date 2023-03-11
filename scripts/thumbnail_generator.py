import os
from PIL import Image

# Define the maximum dimensions for the thumbnail
MAX_SIZE = (300, 300)
root_location = '/Users/amiaynarayan/Projects/photos'
# Create a thumbnails directory if it doesn't already exist
if not os.path.exists(os.path.join(root_location, 'thumbnails')):
    os.makedirs(os.path.join(root_location, 'thumbnails'))

# Loop through all the image files in the current directory
for filename in os.listdir(os.path.join(root_location, 'actual_images')):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # Open the image file and create a thumbnail
        with Image.open(os.path.join(root_location, 'actual_images', filename)) as img:
            img.thumbnail(MAX_SIZE)
            # Save the thumbnail to the thumbnails directory
            thumbnail_filename = os.path.join(root_location, 'thumbnails', f'thumb_{filename}')
            img.save(thumbnail_filename)
