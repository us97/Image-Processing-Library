import numpy as np
import cv2 as cv
import math as m

def maskGenerator(maskSize):
    # todo: check if number is odd
    mask = np.zeros((maskSize, maskSize))
    for i in range(0, maskSize):
        for j in range(0, maskSize):
            mask[i][j] = int(input("Enter Number Please: "))
    return mask


def paddingAdder(image, paddingSize):
    row, col = np.shape(image)
    col = col + 2*paddingSize
    blockimage = np.block([[np.zeros((paddingSize, col))], [np.zeros((row, paddingSize)), image, np.zeros((row, paddingSize))],[np.zeros((paddingSize, col))]])
    return blockimage


def convolution(mask, image):
    row, col = np.shape(image)
    mrow, mcol = np.shape(mask)
    resImage = np.zeros((row - (mrow - 1), col - (mcol - 1)))
    rrow, rcol = np.shape(resImage)
    print("size of resulting image: ", np.shape(resImage))

    for i in range(0, rrow):
        for j in range(0, rcol):
            part = image[i:i+mrow, j:j+mcol]
            resImage[i][j] = np.sum(part * mask)
    return resImage


def normalization(s, min, max):
    a1, a2, b1, b2 = min, max, 0, 255
    return b1 + ((s - a1) * (b2 - b1) / (a2 - a1))


# def main():
#     maskSize = int(input("Please Enter Size of Mask: "))
#     mask = maskGenerator(maskSize)
#     image = cv.imread("image.png", 0)
#     row, col = np.shape(image)
#     print("image size ", np.shape(image))
#     blockimage = paddingAdder(image, int(maskSize/2))
#     print("block image size ", np.shape(blockimage))
#     cv.imwrite("newImage.png",blockimage)
#     convolutedImage = convolution(mask, blockimage)
#     min = np.min(convolutedImage)
#     max = np.max(convolutedImage)
#     for i in range(0, row):
#         for j in range(0, col):
#             convolutedImage[i][j] = int(normalization(convolutedImage[i][j], min, max))
#     cv.imwrite("resImage.png", convolutedImage)
#     return 0
#
#
# main()