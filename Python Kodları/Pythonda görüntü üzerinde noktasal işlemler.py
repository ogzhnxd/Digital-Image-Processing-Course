# Importing libraries
import cv2 as cv
import matplotlib.pyplot as plt

# Reading image
img = cv.imread("meGray.jpg")
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Doing mathematical operations
img1 = cv.add(img, 100)
img2 = cv.subtract(img, 100)

img3 = cv.multiply(img, 0.5)
img4 = cv.divide(img, 2)
img5 = cv.multiply(img, 2)

img6 = cv.add(cv.multiply(img, 0.5), 128)

# Showing images
plt.subplot(3, 3, 1)
plt.gca().set_title('Original')
plt.imshow(img, cmap='gray')

plt.subplot(3, 3, 2)
plt.gca().set_title('+100')
plt.imshow(img1, cmap='gray')

plt.subplot(3, 3, 3)
plt.gca().set_title('-100')
plt.imshow(img2, cmap='gray')

plt.subplot(3, 3, 4)
plt.gca().set_title('*0.5')
plt.imshow(img3, cmap='gray')

plt.subplot(3, 3, 5)
plt.gca().set_title('/2')
plt.imshow(img4, cmap='gray')

plt.subplot(3, 3, 6)
plt.gca().set_title('*2')
plt.imshow(img5, cmap='gray')

plt.subplot(3, 3, 8)
plt.gca().set_title('*0.5+128')
plt.imshow(img6, cmap='gray')

plt.show()

cv.waitKey(0)
