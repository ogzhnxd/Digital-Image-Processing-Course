import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("me.jpg")
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

th = img > 100

_, th2 = cv.threshold(img, 100, 255, cv.THRESH_BINARY)

plt.subplot(1, 3, 1)
plt.imshow(img, cmap="gray")
plt.gca().set_title("Original")

plt.subplot(1, 3, 2)
plt.imshow(th, cmap="gray")
plt.gca().set_title("Threshold")

plt.subplot(1, 3, 3)
plt.imshow(th2, cmap="gray")
plt.gca().set_title("Threshold with CV")

plt.show()

_, thresh1 = cv.threshold(img, 120, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
_, thresh2 = cv.threshold(img, int(255*0.43), 255, cv.THRESH_BINARY)
_, thresh3 = cv.threshold(img, int(255*0.39), 255, cv.THRESH_BINARY)

plt.subplot(1, 4, 1)
plt.imshow(img, cmap="gray")
plt.gca().set_title("Original")

plt.subplot(1, 4, 2)
plt.imshow(thresh1, cmap="gray")
plt.gca().set_title("Threshold 1")

plt.subplot(1, 4, 3)
plt.imshow(thresh2, cmap="gray")
plt.gca().set_title("Threshold 2")

plt.subplot(1, 4, 4)
plt.imshow(thresh3, cmap="gray")
plt.gca().set_title("Threshold 3")

plt.show()

cv.waitKey()
