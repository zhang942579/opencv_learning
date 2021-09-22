import cv2
import numpy as np

img = cv2.imread('./imge/leimu.jpg', 0)
cv2.imshow('leimu1', img)


gray_lap = cv2.Laplacian(img, cv2.CV_16S, ksize=3)
#其中convertScaleAbs函数功能是将CV_16S型的输出图像转变成CV_8U型的图像。
dst = cv2.convertScaleAbs(gray_lap)

cv2.imshow('leimu2', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
