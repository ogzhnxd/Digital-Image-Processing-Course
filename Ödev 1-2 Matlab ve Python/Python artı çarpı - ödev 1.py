# Importing libraries
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Drawing \ part od X
imgCross = np.zeros((265, 256))
imgPlus = np.zeros((265, 256))

for i in range(63, 192):
    for j in range(63, 192):
        if i == j:
            imgCross[i - 10:i + 10, j - 10:j + 10] = 5

# / part of X
mirror_img = np.fliplr(imgCross)
# Merge \ and /
imgCross = np.bitwise_or(imgCross.astype(np.bool_), mirror_img.astype(np.bool_))
imgCross = imgCross.astype(np.uint8)
# Drawing cross
imgPlus[118:138, 32:224] = 2
imgPlus[32:224, 118:138] = 2
# Adding + and X side by side
image = np.concatenate((imgCross, imgPlus), axis=1)
# Changing X grayscale value to 5
image[image == 1] = 5
image = image.astype(np.uint8)

# Making cross visible
cross = np.copy(image)
cross[cross > 4] = 255

# Applying double threshold on cross and making visible plus
ret1, img4 = cv.threshold(cross, 1, 255, cv.THRESH_BINARY)  # Applying threshold to cross image !
ret2, img5 = cv.threshold(cross, 3, 255, cv.THRESH_BINARY)
plus = img4 - img5

# Histogram of image
hist1 = cv.calcHist([image], [0], None, [256], [0, 256])
# Histogram of cross
hist2 = cv.calcHist([cross], [0], None, [256], [0, 256])
# Histogram of plus
hist3 = cv.calcHist([plus], [0], None, [256], [0, 256])

# Plotting images and histograms
plt.subplot(2, 3, 1)
plt.gca().set_title("Original")
plt.imshow(image, cmap="gray", vmin=0, vmax=255)

plt.subplot(2, 3, 2)
plt.gca().set_title("cross")
plt.imshow(cross, cmap="gray")

plt.subplot(2, 3, 3)
plt.gca().set_title("plus")
plt.imshow(plus, cmap="gray")

plt.subplot(2, 3, 4)
plt.gca().set_title('Histogram 1')
plt.plot(hist1)

plt.subplot(2, 3, 5)
plt.gca().set_title('Histogram 2')
plt.plot(hist2)

plt.subplot(2, 3, 6)
plt.gca().set_title('Histogram 3')
plt.plot(hist3)

plt.show()

cv.waitKey(0)
