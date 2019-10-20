import cv2 as cv
import numpy as np
import math as m


def mapRange(s):
    a1, a2, b1, b2 = 255, 0, 0, 255
    return b1 + ((s - a1) * (b2 - b1) / (a2 - a1))


data = cv.imread("walle.png",1)
row, col, rgb = np.shape(data)
print(row, col, rgb)
print(data[1026][494])
print(data[1026][495])
print(data[170][165])
print(data[150][150])

newarray = np.zeros((1250, 2500, 3))  #data[0:row, 0:col, 2:3] # blue colour
print(np.shape(newarray))
for i in range(row):
    for j in range(col):
        if data[i][j][0] == 250 and data[i][j][1] == 245 and data[i][j][2] ==244:
            newarray[i][j] = [223 , 239, 212]
        #     r g b
        #     b g r
        # [216, 220, 213]
        # [238, 236, 234]
        # [227, 204, 169]
        # [233, 231, 229]
        # [207, 243, 252]
        # [223 , 239, 212]
        # elif data[i][j][0] == 228 and data[i][j][1] == 219 and data[i][j][2] ==213:
        #     newarray[i][j] = [126, 109, 93]

        elif data[i][j][0] == 240 and data[i][j][1] == 231 and data[i][j][2] == 224:
            newarray[i][j] = [126, 109, 93]
        else:
            newarray[i][j][0] = data[i][j][0]
            newarray[i][j][1] = data[i][j][1]
            newarray[i][j][2] = data[i][j][2]

cv.imwrite("blue.png",newarray)
# https://outlane.co/now/wall-e-illustration-tutorial/