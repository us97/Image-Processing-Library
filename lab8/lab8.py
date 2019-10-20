import cv2 as cv
import numpy as np
import math as m

# Task 1
array = cv.imread("image.png",0)
newarray = (array > np.mean(array)) * 255
cv.imwrite("res.png",newarray)

newarray1 = (array > np.median(array)) * 255
cv.imwrite("res1.png",newarray1)

# Task 2


def paddingAdder(image, paddingSize):
    row, col = np.shape(image)
    col = col + 2*paddingSize
    blockimage = np.block([[np.zeros((paddingSize, col))], [np.zeros((row, paddingSize)), image, np.zeros((row, paddingSize))],[np.zeros((paddingSize, col))]])
    return blockimage


def threshConv(mask, image):
    row, col = np.shape(image)
    mrow, mcol = np.shape(mask)
    resImage = np.zeros((row - (mrow - 1), col - (mcol - 1)))
    rrow, rcol = np.shape(resImage)
    print("size of resulting image: ", np.shape(resImage))

    for i in range(0, rrow):
        for j in range(0, rcol):
            part = image[i:i+mrow, j:j+mcol]
            resImage[i][j] = (image[i][j] > np.sum(part * mask)-2) * 255
    return resImage


def normalization(s, min, max):
    a1, a2, b1, b2 = min, max, 0, 255
    return b1 + ((s - a1) * (b2 - b1) / (a2 - a1))

mask = np.zeros((3, 3))
for i in range(0, 3):
    for j in range(0, 3):
        mask[i][j] = 1/9
print(mask)
newarray2 = paddingAdder(array, 1)
newarray3 = threshConv(mask, newarray2)
cv.imwrite("res2.png", newarray3)


