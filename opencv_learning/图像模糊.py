import cv2
import numpy as np

img = cv2.imread('./imge/leimu.jpg')
#平均模糊
blur1 = cv2.blur(img, (5, 5))
blur2 = cv2.blur(img, (1, 5))
#高斯模糊
blur3 = cv2.GaussianBlur(img, (5, 5), 0)
#中值模糊
median = cv2.medianBlur(img, 5)

cv2.imshow('a2', blur1)
cv2.imshow('a1', img)
cv2.imshow('a3', blur2)
cv2.imshow('a4', blur3)
cv2.imshow('a5', median)
cv2.waitKey(0)
cv2.destroyAllWindows()


