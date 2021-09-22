import cv2
import numpy as np

img1 = cv2.imread('./imge/leimu.jpg')
img2 = cv2.imread('./imge/leimu3.jpg')
#两图像相加
dst1 = cv2.add(img1, img2)
#两图像混合
dst2 = cv2.addWeighted(img1, 0.8, img2, 0.2, 0)

cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()


