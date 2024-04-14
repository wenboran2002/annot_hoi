import os
from PIL import Image

def resize_images(directory):
    # List all files in the directory
    files = os.listdir(directory)
    
    # Loop through each file
    for file in files:
        # Check if the file is an image (you can add more image extensions if needed)
        if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
            # Open the image
            img_path = os.path.join(directory, file)
            img = Image.open(img_path)
            
            # Get the current width and height
            width, height = img.size
            
            # Calculate the ratio to resize the image to a width of 100 pixels
            ratio = 600 / width
            
            # Resize the image
            new_width = 600
            new_height = int(height * ratio)
            img = img.resize((new_width, new_height), Image.ANTIALIAS)
            
            # Save the resized image, overwriting the original
            img.save(img_path)
            
            print(f"Resized {file} to width 100 pixels.")

# Replace 'your_directory' with the path to your directory containing the images
resize_images('./')
