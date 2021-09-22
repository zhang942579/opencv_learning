import cv2
import numpy as np
#需要绝对路径
img = cv2.imread('./imge/leimu.jpg')

rows, cols = img.shape[:2]
angle = input('输入旋转角度：')

#生成旋转矩阵：第一个参数是旋转中心，第二个参数是旋转度，第三个参数是旋转后的比例因子 您可以设置旋转中心和窗口大小的比例因子，以阻止旋转超出边界
M = cv2.getRotationMatrix2D((cols/2, rows/2), int(angle), 1)
#图像生成
dst = cv2.warpAffine(img, M, (cols, rows))


cv2.imshow('leimu', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()





