import cv2
import numpy as np

img = cv2.imread('./imge/leimu.jpg', cv2.COLOR_BGR2GRAY)
cv2.imshow('leimu1', img)
#将图片转换为RGB格式
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#将图片转换为灰度图
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#两个数组
kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=int)
kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=int)

x = cv2.filter2D(grayImage, cv2.CV_16S, kernelx)
y = cv2.filter2D(grayImage, cv2.CV_16S, kernely)

adsX = cv2.convertScaleAbs(x)
adsy = cv2.convertScaleAbs(y)
Prewitt = cv2.addWeighted(adsX, 0.5, adsy, 0.5, 0)
cv2.imshow('leimu2', Prewitt)

cv2.waitKey(0)
cv2.destroyAllWindows()
