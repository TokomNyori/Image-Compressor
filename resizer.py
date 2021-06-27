from PIL import Image
import os
from sys import exit

x = 533

# This function resizes images and also maintains the aspect ratio
def resizer(img, new_width):
    width, height = img.size
    ratio = height / width
    new_height = int(ratio * new_width)
    resized_image = img.resize((new_width, new_height), Image.ANTIALIAS)
    return resized_image

# This list carries the valid acceptable image extensions
img_extns = ['jpg', 'jpeg', 'png', 'gif', 'bmp']

# Changing directory
os.chdir('images/')


# Saving images into a list
img_list = os.listdir()

# Verifies the images
for i in img_list:
    ext = i.split('.')
    if ext[-1] in img_extns:
        print('Valid image extension')
    else:
        print('Invalid image extension')
        exit()

# Prompt users to enter desired width
img_width = int(input('Enter your desired width for resizing: '))

# Loops the images for resizing and saving
for i in img_list:
    # Opens the facade image
    image = Image.open(i)

    # Saves the copies of resized images to a new folder
    resized_image = resizer(image, img_width) # Calls the resizer function for resizing
    resized_image.save(f'F:/python_projects/Image-Compressor/resized_images/{i}') # Saves the image using absolute file path
