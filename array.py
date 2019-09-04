# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#/		Authored by TheRavikin (https://github.com/Ravikin)    \#
#\	   ravi@uwcontrol.pl   |   				       /#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# This lil thing is printing given image in asci style array with grayscale values
# Some tips for me for later 
# PIL convert options
# https://pillow.readthedocs.io/en/latest/handbook/concepts.html#modes
from numpy import *
from PIL import Image
from PIL import ImageOps
import sys
import os
import time

# Checking for numpy loaded properly
modulename = 'numpy'
	if modulename not in sys.modules:
    print("You have not imported the {} module").format(modulename)

# Loading local image for ~fun~
img = Image.open('img.png')
width, height = img.size

# Converting to grayscale
im = ImageOps.grayscale(img)

# Saving not needed in this case
# im.save(os.getcwd() + '\\Snap__' + str(int(time.time())) + '.png', 'PNG')

a = []
 for x in range(0,width):
    for y in range(0,height):
		a.append(im.getpixel((x,y)))

a = array(a)
final = a.reshape(width,height)

print(final)

# cya! well done!

