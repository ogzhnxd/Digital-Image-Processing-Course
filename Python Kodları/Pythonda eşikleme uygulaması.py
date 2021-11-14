# Importing libraries
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("text.tif")
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

noise = np.random.rand(img.shape[0], img.shape[1])
noisy = np.multiply(noise, np.bitwise_not(img))
_, th = cv.threshold(noisy, 0, 255, cv.THRESH_BINARY)

plt.subplot(1, 3, 1)
plt.imshow(img, cmap="gray")
plt.gca().set_title("Original")

plt.subplot(1, 3, 2)
plt.imshow(noisy, cmap="gray")
plt.gca().set_title("Noisy")

plt.subplot(1, 3, 3)
plt.imshow(th, cmap="gray")
plt.gca().set_title("Recovered")

plt.show()

cv.waitKey(0)
