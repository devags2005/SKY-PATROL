from PIL import Image
import os

# Folder with your images
image_folder = 'images'

# Loop through each image
for filename in os.listdir(image_folder):
    if filename.endswith('.jpg'):
        print(f"Checking image: {filename}")

        # Just pretend and make a guess
        if '1' in filename or '2' in filename:
            print("Unauthorized construction detected!")
        else:
            print("All clear. No construction.")
