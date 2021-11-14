# Importing libraries
import cv2 as cv
import matplotlib.pyplot as plt


# reads an input image
img1 = cv.imread('me.jpg')
img1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)

img2 = cv.imread("me2.jpg")
img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

# find frequency of pixels in range 0-255
hist1 = cv.calcHist([img1], [0], None, [256], [0, 256])
hist2 = cv.calcHist([img2], [0], None, [256], [0, 256])

# show the plotting graph of an image
plt.subplot(2, 2, 1)
plt.gca().set_title('IMG1')
plt.imshow(img1, cmap='gray')

plt.subplot(2, 2, 2)
plt.gca().set_title('Histogram 1')
plt.plot(hist1)

plt.subplot(2, 2, 3)
plt.gca().set_title('IMG2')
plt.imshow(img2, cmap='gray')

plt.subplot(2, 2, 4)
plt.gca().set_title('Histogram 2')
plt.plot(hist2)

plt.show()

cv.waitKey(0)
