# Importing libraries
import cv2 as cv
from PIL import Image

# Reading image
img = cv.imread("me.jpg")

# Printing image size
print("Image size : ", img.shape[0], img.shape[1])

# Getting image meta data (similar to MATLAB's imfinfo())
# Opening Image as an object
imgPIL = Image.open("me.jpg")
# Getting the filename of image
print("Filename : ", imgPIL.filename)
# Getting the format of image
print("Format : ", imgPIL.format)
# Getting the mode of image
print("Mode : ", imgPIL.mode)
# Getting the size of image
print("Size : ", imgPIL.size)
# Getting only the width of image
print("Width : ", imgPIL.width)
# Getting only the height of image
print("Height : ", imgPIL.height)
# Getting the color palette of image
print("Image Palette : ", imgPIL.palette)
# Getting the info about image
print("Image Info : ", imgPIL.info)
# Closing Image object
imgPIL.close()

cv.waitKey(0)
