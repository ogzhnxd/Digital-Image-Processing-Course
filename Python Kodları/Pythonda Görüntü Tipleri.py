# Importing libraries
import cv2 as cv
import matplotlib.pyplot as plt

# Reading images
img = cv.imread("me.jpg")
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
imgGray = cv.imread("meGray.jpg")
imgBinary = cv.imread("meBinary.jpg")

# Showing images
plt.subplot(1, 3, 1)
plt.imshow(img)
plt.subplot(1, 3, 2)
plt.imshow(imgGray, cmap="gray")
plt.subplot(1, 3, 3)
plt.imshow(imgBinary, cmap="binary")

plt.show()

cv.waitKey(0)
