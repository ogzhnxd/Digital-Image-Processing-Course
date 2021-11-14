import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("me.jpg")
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

th = cv.inRange(img, 100, 150)

plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray")
plt.gca().set_title("Original")

plt.subplot(1, 2, 2)
plt.imshow(th, cmap="gray")
plt.gca().set_title("Threshold")

plt.show()

cv.waitKey(0)
