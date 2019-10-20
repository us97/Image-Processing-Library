import numpy as np
import cv2 as cv
# For the image given below (provided with the lab handout), apply the connectected component
# labelling and count the total number of white objects. First threshold the images
# ( replace pixel values less than 127 equal to 0 and above 127 equal to 1)
# and then do connected component analysis.

array = cv.imread("./Picture2.png",0)
row, col = np.shape(array)

cv.imwrite("array.png", array)


def threshold(pixel):
    if pixel < 147:
        return 1
    else:
        return 255


newarray = np.zeros((row, col))
for i in range(0, row):
    for j in range(0, col):
        newarray[i][j] = threshold(array[i][j])

# newarray = np.array([
#         [1,     1,     1,     1,     1,     1,     1,     1,     1,     1],
#         [1,   255,    255,     255,     1,     1,     1,     1,     1,     1],
#         [1,   255,    255,     255,     1,     1,     1,     1,     1,     1],
#         [1,   255,    255,     255,     1,     1,     1,     1,     1,     1],
#         [1,   1,    1,     1,     1,     1,     1,     1,     1,     1],
#         [1,   1,    1,     1,     255,     1,     1,     255,     255,     1],
#         [1,   1,    1,     1,     255,     1,     1,     255,     255,     1],
#         [1,   1,    1,     1,     255,     255,     255,     255,     255,     1],
#         [1,   255,    255,     255,     255,     255,     255,     255,     255,     1],
#         [1,   255,    255,     255,     255,     255,     255,     255,     255,     1],
#         [1,   1,    1,     1,     1,     1,     1,     1,     1,     1]])
# row, col = np.shape(newarray)

labels = []  # [,200, 180, 180, 120, 80, 40]
for i in range(2, 555):
    labels.append(i)
print(labels)
equilencyList = []
# Raster scan step 1
for i in range(0, row):
    for j in range(0, col):
        if newarray[i][j] != 1:
            if newarray[i-1][j] == 1 and newarray[i][j-1] == 1:  # check top and left, if both background then true
                temp = labels.pop()
                equilencyList.append([temp, temp])
                newarray[i][j] = temp  # give new label
            elif newarray[i-1][j] == newarray[i][j-1]:  # if top and left are equal, then copy same value
                newarray[i][j] = newarray[i-1][j]
            elif newarray[i-1][j] == 1:  # if top is background then copy value of left
                newarray[i][j] = newarray[i][j-1]
            elif newarray[i][j-1] == 1:  # if left is background then copy value of top
                newarray[i][j] = newarray[i-1][j]
            else:  # if different objects but connected
                if newarray[i-1][j] < newarray[i][j-1]:
                    newarray[i][j] = newarray[i-1][j]
                    for x in equilencyList:
                        if x[1] == newarray[i][j-1]:
                            x[1] = newarray[i - 1][j]

                else:
                    newarray[i][j] = newarray[i][j-1]
                    for x in equilencyList:
                        if x[1] == newarray[i - 1][j]:
                            x[1] = newarray[i][j-1]

# Raster scan step 2
for i in range(0, row):
    for j in range(0, col):
        if newarray[i][j] != 1:
            for x in equilencyList:
                if newarray[i][j] == x[0]:
                    newarray[i][j] = x[1]

# count number of object in picture
countList = []
for x in equilencyList:  # [:][1:1]
    countList.append(x[1])
count = len(np.unique(countList))

# Printing
print("Number of objects", count)
print("Equivalency list", equilencyList)
print("Image", newarray)
cv.imwrite("newarray.png", newarray)

# row, col = np.shape(array)

#         If the next pixel to process is 1
#         i.)   If only one from top or left is 1, copy its label.
#         ii.)  If both top and left are one and have the  same label, copy it.
#         iii.) If top and left they have different labels
# 		        Copy the smaller label
# 		        Update the equivalence table.
#         iv.) Otherwise, assign a new label.
# ω	Re-label with the smallest of equivalent labels
# ω

# connected component analysis
# 0 means dark , 255 means white