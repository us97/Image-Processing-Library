import numpy as np
import cv2 as cv
import math as m
import functions as f

imgArray = cv.imread("image.png",0)

gyMask = np.array( [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
gxMask = np.array( [[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

blockimage = f.paddingAdder(imgArray, int(3/2))
gxImage = f.convolution(gxMask,blockimage)
gyImage = f.convolution(gyMask,blockimage)

cv.imwrite("gxImage.png",gxImage)
cv.imwrite("gyImage.png", gyImage)

mag = gxImage**2 + gyImage**2

row , col = np.shape(gxImage)
for i in range(0, row):
    for j in range(0, col):
        if gxImage[i][j] == 0:
            gxImage[i][j] = 0.001

dir = np.arctan(gyImage/gxImage)

blur = cv.GaussianBlur(imgArray,(5,5),0)