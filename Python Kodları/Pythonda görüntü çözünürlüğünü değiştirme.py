# Importing libraries
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("meGray.jpg")

img1 = cv.resize(img, (0, 0), fx=0.5, fy=0.5)
img1 = cv.resize(img1, (img.shape[0], img.shape[1]))

img2 = cv.resize(img, (0, 0), fx=0.25, fy=0.25)
img2 = cv.resize(img2, (img.shape[0], img.shape[1]))

img3 = cv.resize(img, (0, 0), fx=0.125, fy=0.125)
img3 = cv.resize(img3, (img.shape[0], img.shape[1]))

# Showing images
plt.subplot(2, 2, 1)
plt.gca().set_title('Original')
plt.imshow(img, cmap='gray')

plt.subplot(2, 2, 2)
plt.gca().set_title('Half resolution')
plt.imshow(img2, cmap='gray')

plt.subplot(2, 2, 3)
plt.gca().set_title('Quarter resolution')
plt.imshow(img2, cmap='gray')

plt.subplot(2, 2, 4)
plt.gca().set_title('1/8 resolution')
plt.imshow(img3, cmap='gray')


plt.show()

cv.waitKey(0)
