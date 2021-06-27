from PIL import Image
import os
from sys import exit

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
del img_list[-1]

# Verifies the images
for i in img_list:
    ext = i.split('.')
    if ext[-1] in img_extns:
        print('Valid image extension')
    else:
        print('Invalid image extension')
        exit()    

counter = 0

# Loops the images for resizing and saving
for i in img_list:
    img_name = i.split('.')
    if img_name[0] == 'facade':
        # Opens the facade image
        image = Image.open(i)

        # Saves a copy of facade image into 640px
        resized_image = resizer(image, 640) # Calls the resizer function for resizing
        resized_image.save(f'resized_images/facade_sm.{img_name[-1]}') # Saves the image

        # Saves a copy of facade image into 1920px
        resized_image = resizer(image, 1920)
        resized_image.save(f'resized_images/facade_lg.{img_name[-1]}')
    else:
        # Opens the facade image
        image = Image.open(i)

        # Saves the interior images into 1920px
        resized_image = resizer(image, 1280)
        resized_image.save(f'resized_images/interior-{counter}.{img_name[-1]}')

    counter += 1 # Increements the counter variable by one  