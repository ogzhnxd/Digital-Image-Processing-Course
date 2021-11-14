# Importing libraries
import cv2 as cv
import matplotlib.pyplot as plt

img1 = cv.imread("me.jpg")

img1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
hist1 = cv.calcHist([img1], [0], None, [256], [0, 256])

img2 = cv.equalizeHist(img1)
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

img1 = cv.imread("me.jpg")
img1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
hist1 = cv.calcHist([img1], [0], None, [256], [0, 256])

img2 = cv.divide(img1, 4)
hist2 = cv.calcHist([img2], [0], None, [256], [0, 256])

img3 = cv.equalizeHist(img2)
hist3 = cv.calcHist([img3], [0], None, [256], [0, 256])

# show the plotting graph of an image
plt.subplot(3, 2, 1)
plt.gca().set_title('IMG1')
plt.imshow(img1, cmap='gray')

plt.subplot(3, 2, 2)
plt.gca().set_title('Histogram 1')
plt.plot(hist1)

plt.subplot(3, 2, 3)
plt.gca().set_title('IMG2')
plt.imshow(img2, cmap='gray')

plt.subplot(3, 2, 4)
plt.gca().set_title('Histogram 2')
plt.plot(hist2)

plt.subplot(3, 2, 5)
plt.gca().set_title('IMG3')
plt.imshow(img3, cmap='gray')

plt.subplot(3, 2, 6)
plt.gca().set_title('Histogram 3')
plt.plot(hist3)

plt.show()

cv.waitKey()
