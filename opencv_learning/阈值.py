import cv2
import numpy as np

img = cv2.imread('./imge/leimu.jpg')

ret1, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret2, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret3, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret4, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret5, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

img7 = cv2.medianBlur(img, 5)

cv2.imshow('1', thresh1)
cv2.imshow('2', thresh2)
cv2.imshow('3', thresh3)
cv2.imshow('4', thresh4)
cv2.imshow('5', thresh5)
cv2.imshow('7', img7)

cv2.waitKey(0)
cv2.destroyAllWindows()


