import cv2
import numpy as np
img = cv2.imread('./imge/leimu.jpg')
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
imgShift = np.float32([[1, 0, 100], [0, 1, 100]])# [1,0,100]的意思是，宽右移距离100 [0,1,200]高下移200
print(imgShift)
dst = cv2.warpAffine(img, imgShift, (width, height))
cv2.imshow('as', img)
cv2.imshow('img', dst)
cv2.waitKey(0)