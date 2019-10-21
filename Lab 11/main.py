# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 15:41:37 2019

@author: Me
"""

import cv2 as cv
import numpy as np

# =============================================================================
# im1=cv.imread("Fig1.png",0)
# im2=cv.imread("Fig2.png",0)
# =============================================================================
im1=cv.imread("Fig3.png",0)
im2=cv.imread("Fig4.png",0)
size=np.shape(im2)
row=(int(size[0]))
col=(int(size[1]))
im1=cv.resize(im1,(col,row))
im1f=np.fft.fft2(im1)
im1f=np.fft.fftshift(im1f)
im1f=np.abs(im1f)
cv.imwrite('ffig3.png',im1f)

midx=(int(size[0]))/2
midy=(int(size[1]))/2
# =============================================================================
# for i in range(row):
#     for j in range(col):
#         if(im2[i][j]>127):
#             im2[i][j]=1;
#         else:
#             im2[i][j]=0
# =============================================================================
for i in range(size[0]):
    for j in range(size[1]):
        dist=np.sqrt(((midx-i)**2)+((midy-j)**2))
        if(dist>50):
            im2[i][j]=1
        else:
            im2[i][j]=0




mulx=np.multiply(im1f,im2)
mul2=np.fft.ifft2(mulx)
ifft=np.abs(mul2)

mifft=np.max(ifft)
sifft=np.min(ifft)
q=np.shape(ifft)
for i in range (0,q[0]):
    for j in range (0,q[1]):
        ifft[i][j]=((ifft[i][j]-sifft)/(mifft-sifft))*255
ifft=np.uint8(ifft)
cv.imwrite("test.png",ifft)
