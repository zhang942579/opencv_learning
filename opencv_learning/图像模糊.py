import cv2
import numpy as np

img = cv2.imread('./imge/leimu.jpg')
#平均模糊
blur1 = cv2.blur(img, (5, 5))
blur2 = cv2.blur(img, (1, 5))
#高斯模糊
blur3 = cv2.GaussianBlur(img, (7, 7), 0)
# blur5 = cv2.GaussianBlur(img, (1, 7), 0)
#中值模糊
median = cv2.medianBlur(img, 5)
# median2 = cv2.medianBlur(img, 5)
#双边滤波
blur4 = cv2.bilateralFilter(img, 9, 75, 75)
blur6 = cv2.bilateralFilter(img, 100, 75, 75)
# cv2.imshow('a2', blur1)
cv2.imshow('a1', img)
# cv2.imshow('a3', blur2)
# cv2.imshow('a7', blur5)
# cv2.imshow('a4', blur3)
# cv2.imshow('a5', median)
# cv2.imshow('a8', median2)
cv2.imshow('a6', blur4)
cv2.imshow('a9', blur6)

cv2.waitKey(0)
cv2.destroyAllWindows()


