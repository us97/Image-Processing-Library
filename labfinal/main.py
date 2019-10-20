import numpy as np
import cv2 as cv
import functions as f
from matplotlib import pyplot as plt

img1 = cv.imread("img/fig1.jpg",1)
print(np.shape(img1))
r = img1[:,:,0] # red is in black
g = img1[:,:,2] # g is in black

ret,r = cv.threshold(r,127,255,cv.THRESH_BINARY)
ret,g = cv.threshold(g,127,255,cv.THRESH_BINARY)

cv.imwrite("g.jpg",g)
cv.imwrite("r.jpg",r)

kernel1 = np.ones((9, 9), np.uint8)
r = cv.morphologyEx(r, cv.MORPH_DILATE, kernel1)
g = cv.morphologyEx(g, cv.MORPH_DILATE, kernel1)

contours, hier = cv.findContours(r, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

img = r
for c in contours:
    x, y, w, h = cv.boundingRect(c)
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # get the min area rect
    rect = cv.minAreaRect(c)
    box = cv.boxPoints(rect)
    # convert all coordinates floating point values to int
    box = np.int0(box)
    # draw a red 'nghien' rectangle
    cv.drawContours(img, [box], 0, (0, 0, 255))

cv.imwrite("contoursr.jpg", img)

contours, hier = cv.findContours(g, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

img = g
for c in contours:
    x, y, w, h = cv.boundingRect(c)
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # get the min area rect
    rect = cv.minAreaRect(c)
    box = cv.boxPoints(rect)
    # convert all coordinates floating point values to int
    box = np.int0(box)
    # draw a red 'nghien' rectangle
    cv.drawContours(img, [box], 0, (0, 0, 255))

cv.imwrite("contoursg.jpg", img)

# rosearray = cv.imread("img/rose.jpg",0)
#
# plt.hist(rosearray.ravel(),256,[0,256]); plt.show()
# my_transformed_image1 = np.fft.fft2(np.array([[5, 6, 9, 8, 2],
#                                               [7, 2, 8, 8, 1],
#                                               [9, 5, 2, 2, 6]]))
# data = np.fft.fftshift(my_transformed_image1)
# print(data)

