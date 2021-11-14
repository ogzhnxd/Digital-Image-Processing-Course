# Importing libraries
import cv2 as cv
import matplotlib.pyplot as plt

# Reading image
img = cv.imread("me.jpg")

# Thresholding
img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
th, dst = cv.threshold(img, 100, 255, cv.THRESH_BINARY)

# Showing image
plt.subplot(1, 2, 1)
plt.gca().set_title("Image")
plt.imshow(img, cmap="gray")

plt.subplot(1, 2, 2)
plt.gca().set_title("Thresh")
plt.imshow(dst, cmap="gray")

plt.show()

cv.waitKey(0)
