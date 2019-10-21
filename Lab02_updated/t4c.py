import numpy as np
import cv2
import os
os.chdir("E:\Drive\CEME Study\Semester 6\Digital Image Processing EC-312\Lab\Lab2(8-3-17)")
siz = 550
b8 = 50
n=2
my=np.zeros((siz,siz))
x=0
y=0
n=n+1
xmax =np.int16( siz/n-(b8*n-b8)/n)
ymax=xmax
for i in range(0,siz):
    y=0
    for j in range(0,siz):
        if x<xmax:
            if y<ymax:
                my[i,j]=255
        
        
        y=y+1
        
        if y >= ymax+b8:
            y=0
    x=x+1
    if x >= xmax+b8:
        x=0

       
cv2.imshow("dg.jpg",my)
cv2.imwrite("f4net.jpg",my)
