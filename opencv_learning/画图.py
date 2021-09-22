#要想将当前的数组作为图像类型来进行各种操作，就要转换到uint8类型，转换的方式推荐使用第二种，因为第一种在值大于255以后就容易丢失。
import cv2
import numpy as np


img=cv2.imread('./imge/leimu.jpg')#np.zeros((512, 512, 3),np.uint8)

#左上角到右下角的线

cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

#右上角的矩形
cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
#右上角的圆
cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)
#多边形
pts = np.array([[100, 50], [200, 300], [500, 200], [500, 100]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (255, 255, 0))

cv2.imshow('huatu', img)

cv2.waitKey(0)
cv2.destroyAllWindows()