import numpy
def ConvSum(Padded,Filter):
    SizeImage=numpy.shape(Padded)
    nr = SizeImage[0]
    nc = SizeImage[1]
    SizeFilter=numpy.shape(Filter)
    rows=SizeFilter[0]; cols=SizeFilter[1]
    Padded2=numpy.zeros((nr,nc),dtype=numpy.uint64)
    for i in range(nr):
        for j in range(nc):
            summ = 0
            for l in range(rows):
                for m in range(cols):
                    if i < (nr - 2) and j < (nc - 2):
                        summ = (Padded[i + l][j + m] * Filter[l][m]) + summ
            if i < nr or j < nc:
                Padded2[i][j] = summ

    return Padded2

def ConvSumx(Padded,Filter,Pad):
    SizeImage=numpy.shape(Padded)
    nr = SizeImage[0]
    nc = SizeImage[1]
    SizeFilter=numpy.shape(Filter)
    rows=SizeFilter[0]; cols=SizeFilter[1]
    Padded2=numpy.zeros((nr,nc),dtype=numpy.uint64)
    for i in range(nr):
        for j in range(nc):
            summ = 0
            for l in range(rows):
                for m in range(cols):
                    if i < (nr - (Pad*2)) and j < (nc - (Pad*2)):
                        summ = (Padded[i + l][j + m] * Filter[l][m]) + summ
                        # summ=summ/273
            if i < nr or j < nc:
                Padded2[i][j] = summ

    return Padded2


def Padding(Image):
    SizeImage=numpy.shape(Image)
    nr = SizeImage[0] + 2
    nc = SizeImage[1] + 2
    Padded = numpy.zeros((nr, nc), dtype=numpy.uint64)
    Padded2 = numpy.zeros((nr, nc), dtype=numpy.uint64)
    for i in range(nr):
        for j in range(nc):
            if i > 0 and i < nr - 1 and j > 0 and j < nc - 1:
                Padded[i][j] = Image[i - 1][j - 1]

    return Padded

def Paddingx(Image,Pad):
    SizeImage=numpy.shape(Image)
    nr = SizeImage[0] + Pad*2
    nc = SizeImage[1] + Pad*2
    Padded = numpy.zeros((nr, nc), dtype=numpy.uint64)
    Padded2 = numpy.zeros((nr, nc), dtype=numpy.uint64)
    for i in range(nr):
        for j in range(nc):
            if i >= Pad and i < nr - (Pad) and j >= Pad and j < nc - (Pad):
                Padded[i][j] = Image[i - Pad][j - Pad]

    return Padded

def testy(nums,target):
    for i in range(len(nums)):
        for j in range(1,len(nums)):

                if nums[i] + nums[j] == target and i!=j:
                    return i, j
