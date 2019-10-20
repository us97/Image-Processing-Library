import numpy as np
import cv2 as cv

# gray scale 0 means dark, 255 means white



# Read any image that you want and save it in gray scale. Now mirror the image that you have
# read at center i.e. the upper half of the image should be the copy of the lower half but mirrored.
# Write the image to the disk. See the image below.

array = cv.imread("./image.png", 0)
size = np.shape(array)
row = size[0]
col = size[1]
print(row, col)
newarray = array[0:row, 0:col]
# print(newarray)
for i in range(row//2,row):
    for j in range(0, col):
        newarray[i][j] = array[row -1 - i][j]

cv.imwrite("fake.png", newarray)

# Now create a generic code that create a border around any landscape image as shown below.
# The length of right and left borders must be 10% of the original horizontal length of the image.
# The length of upper and lower border must be such that the image now have same number of rows as columns.
# Save the image.

array = cv.imread("./image.png", 0)
size = np.shape(array)
row = size[0]
col = size[1]
print(row, col)

col = col + 20
sqr = 0
if row > col:
    sqr = row
else:
    sqr = col

lengthToAdd = sqr - row
blockimage = np.block([[np.ones((lengthToAdd//2,col))], [np.ones((row, 10)), array, np.ones((row, 10))], [np.ones((lengthToAdd//2,col))]])
cv.imwrite("blockimage.png", blockimage)
print(blockimage)

# Using the following formula f (i, j) = sin (2 π f (i + j)) where i are j indices of a pixel,
# draw an image with different frequencies (input from user).


def feqgen(i, j):
    return np.sin(0.051 * (i + j))


def mapRange(s):
    a1, a2, b1, b2 = -1, 1, 0, 255
    return b1 + ((s - a1) * (b2 - b1) / (a2 - a1))



square = np.zeros((1000, 1000))
for i in range(0, 1000):
    for j in range(0, 1000):
        square[i][j] = mapRange(feqgen(i,j))

print(square)
cv.imwrite("freqimage.png", square)

# Write a function to create a white image size entered by the user and then create 4 boxes of Black, Blue,
# Green and Red respectively on each corner of the image as shown below.
# The size of the colored boxes should be 1/10th the size of the image.
# (HINT: the arrays of ones and zeros can be in more than 2 dimensions)

array = np.full((10, 10, 3), 255)

for i in range(0,2):
    for j in range(0,2):
        array[i][j][0] = 0
        array[i][j][1] = 0
for i in range(8,10):
    for j in range(0,2):
        array[i][j][1] = 0
        array[i][j][2] = 0
for i in range(0,2):
    for j in range(8,10):
        for k in range(0,3):
            array[i][j][k] = 0
for i in range(8,10):
    for j in range(8,10):
        array[i][j][2] = 0
        array[i][j][0] = 0
print(array)
cv.imwrite("new.png", array)
# source
# https://rosettacode.org/wiki/Map_range#Python