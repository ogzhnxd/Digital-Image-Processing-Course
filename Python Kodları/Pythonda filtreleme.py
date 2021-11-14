# Importing libraries
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

x = np.random.randint(25, size=(5, 5), dtype=np.uint8) * 10

a = np.ones((3, 3), np.float32) / 9
dst1 = signal.convolve2d(x, a, mode='same')
dst1 = dst1.astype(np.uint8)

dst2 = signal.convolve2d(x, a, mode='valid')
dst2 = dst2.astype(np.uint8)

print("x = \n", x)
print("a = \n", a)
print("ans (same) = \n", dst1)
print("ans (valid) = \n", dst2)

img = cv.imread("me.jpg")
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

filtered = cv.boxFilter(img, -1, (3, 3))
filtered1 = cv.boxFilter(img, -1, (9, 9))
filtered2 = cv.boxFilter(img, -1, (25, 25))

plt.subplot(2, 3, 2)
plt.imshow(img, cmap="gray")
plt.gca().set_title("Original")

plt.subplot(2, 3, 4)
plt.imshow(filtered, cmap="gray")
plt.gca().set_title("3x3")

plt.subplot(2, 3, 5)
plt.imshow(filtered1, cmap="gray")
plt.gca().set_title("9x9")

plt.subplot(2, 3, 6)
plt.imshow(filtered2, cmap="gray")
plt.gca().set_title("25x25")

plt.show()

cv.waitKey()
