import numpy as np
import cv2 as cv
import math as m
import matplotlib as mp

#  TASK 1
carArray = cv.imread("./car.jpg", 0)
Xmin = np.percentile(carArray, 5)
Xmax = np.percentile(carArray, 95)
brow, bcol = np.shape(carArray)

def mapRange(s):
    a1, a2, b1, b2 = Xmin, Xmax, 0, 255
    return b1 + ((s - a1) * (b2 - b1) / (a2 - a1))


for i in range(0, brow):
    for j in range(0, bcol):
        if carArray[i][j] < Xmin:
            carArray[i][j] = 0
        elif carArray[i][j] > Xmax:
            carArray[i][j] = 255
        else:
            carArray[i][j] = mapRange(carArray[i][j])
cv.imwrite("newcarImage.jpg", carArray);


# TASK 3
gama = 0.5
power = np.power(carArray, gama)
c = 255 / np.max(power)

for i in range(0, brow):
    for j in range(0, bcol):
        carArray[i][j] = c * pow(power[i][j], gama)

cv.imwrite("gamaImage.jpg", carArray)
