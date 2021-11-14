# Importing libraries
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("circles.tif")
c = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

x = np.ones([256, 1]) * np.arange(1, 257)
c2 = (c.astype(np.float32) * ((x / 2) + 50)) + ((1 - c.astype(np.float32)) * (x / 2))
out = np.zeros(c2.shape, np.double)
normalized = cv.normalize(c2, out, 1.0, 0.0, cv.NORM_MINMAX, dtype=cv.CV_64F) * 8
c3 = np.round(2550 * normalized).astype(np.uint8)

_, thresh = cv.threshold(c3, 120, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

thresh1 = cv.adaptiveThreshold(c3, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 131, -1)

plt.subplot(1, 3, 1)
plt.gca().set_title("Original")
plt.imshow(c3, cmap="gray")

plt.subplot(1, 3, 2)
plt.gca().set_title("THRESH")
plt.imshow(thresh, cmap="gray")

plt.subplot(1, 3, 3)
plt.gca().set_title("ADAPTIVE THRESH")
plt.imshow(thresh1, cmap="gray")

plt.show()

cv.waitKey()
