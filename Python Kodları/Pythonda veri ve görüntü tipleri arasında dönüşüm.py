# Importing libraries
import cv2 as cv
import numpy as np
from skimage import util
import matplotlib.pyplot as plt


f = np.array([[-1.65, 0.5], [0.75, 0.85]])
f = f.clip(0, f.max())
print(f)
print("Shape : ", f.shape)
print("Size  : ", f.size)
print("dtype : ", f.dtype)


g = util.img_as_ubyte(f)
print("\n", g)
print("Shape : ", g.shape)
print("Size  : ", g.size)
print("dtype : ", g.dtype)

f = cv.imread("meGray.jpg")
plt.subplot(1, 2, 1)
plt.gca().set_title("uint8")
plt.imshow(f, cmap="gray")

print("\nShape : ", f.shape)
print("Size  : ", f.size)
print("dtype : ", f.dtype)

g = util.img_as_float64(f)
plt.subplot(1, 2, 2)
plt.gca().set_title("float64")
plt.imshow(f, cmap="gray")

print("\nShape : ", g.shape)
print("Size  : ", g.size)
print("dtype : ", g.dtype)

plt.show()

cv.waitKey(0)
