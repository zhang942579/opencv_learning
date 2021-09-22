import cv2
import numpy as np
img = cv2.imread('D:\software_code\python\pc_xuexi\opencv_learning\imge\leimu.jpg')
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
imgShift1 = np.float32([[-1, 0, 640], [0, 1, 0]])
dst1 = cv2.warpAffine(img, imgShift1, (width, height))

imgShift2 = np.float32([[1, 0, 0], [0, -1, 517]])
dst2 = cv2.warpAffine(img, imgShift2, (width, height))

imgShift3 = np.float32([[-1, 0, 640], [0, -1, 517]])
dst3 = cv2.warpAffine(img, imgShift3, (width, height))

cv2.imshow('as', img)
cv2.imshow('img1', dst1)
cv2.imshow('img2', dst2)
cv2.imshow('img3', dst3)
cv2.waitKey(0)