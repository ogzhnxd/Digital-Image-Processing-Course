# Importing libraries
import cv2 as cv
import numpy as np
import skimage
import matplotlib.pyplot as plt
from scipy import signal


# Reading images
img = cv.imread("me.jpg")
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
kernel_size = 30

# Create the vertical kernel.
kernel_v = np.zeros((kernel_size, kernel_size))

# Fill the middle row with ones.
kernel_v[:, int((kernel_size - 1) / 2)] = np.ones(kernel_size)

# Normalize
kernel_v /= kernel_size

# Apply the vertical kernel.
motion = cv.filter2D(img, -1, kernel_v)

original = io.imread("meGray.jpg")

# create disk-like filter footprint with given radius
radius = 10
circle = skimage.morphology.disk(radius)

# apply median filter with given footprint = structuring element = selem
disk = skimage.filters.median(original, selem=circle)

kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])
sharp = cv.filter2D(src=img, ddepth=-1, kernel=kernel)

plt.subplot(2, 3, 2)
plt.gca().set_title("Original")
plt.imshow(img, cmap="gray")
plt.subplot(2, 3, 4)
plt.gca().set_title("Motion blur")
plt.imshow(motion, cmap="gray")
plt.subplot(2, 3, 5)
plt.gca().set_title("Disk blur")
plt.imshow(disk, cmap="gray")
plt.subplot(2, 3, 6)
plt.gca().set_title("Sharpening")
plt.imshow(sharp, cmap="gray")

plt.show()

cv.waitKey()
