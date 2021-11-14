import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

a = cv.imread("cameraman.tif")
a = cv.cvtColor(a, cv.COLOR_BGR2GRAY)
b = cv.imread("text.tif")
b = cv.cvtColor(b, cv.COLOR_BGR2GRAY)
a_double = a.astype(np.float16)
b_double = b.astype(np.float16)
m = a_double + 255*b_double
m[m > 255] = 255
m = m.astype(np.uint8)

_, img1 = cv.threshold(m, 254, 255, cv.THRESH_BINARY_INV)

img2 = np.copy(m)

for idx in np.where(m == 255):
    img2[idx] = a[idx]

hista = cv.calcHist([a], [0], None, [256], [0, 256])
histb = cv.calcHist([b], [0], None, [256], [0, 256])
histm = cv.calcHist([m], [0], None, [256], [0, 256])
histimg1 = cv.calcHist([img1], [0], None, [256], [0, 256])
histimg2 = cv.calcHist([img2], [0], None, [256], [0, 256])

images = [a, b, m, img1, img2]
hists = [hista, histb, histm, histimg1, histimg2]
img_titles = ["A", "B", "M", "separated cameraman", "separated text"]
hist_titles = ["hista", "histb", "histm", "histimg1", "histimg2"]

for i in range(len(images)):
    plt.subplot(2, 5, i + 1)
    plt.gca().set_title(img_titles[i])
    plt.imshow(images[i], cmap="gray")

    plt.subplot(2, 5, i + 6)
    plt.gca().set_title(hist_titles[i])
    plt.plot(hists[i])

plt.show()

cv.waitKey(0)
