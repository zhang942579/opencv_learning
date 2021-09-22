import cv2
import numpy as np

img = cv2.imread('./imge/leimu.jpg')

rows, cols, ch = img.shape
#图片原因，无法运行
pts1=np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2=np.float32([[0,0],[300,0],[0,300],[300,300]])

M=cv2.getPerspectiveTransform(pts1,pts2)
dst=cv2.warpAffine(img,M,(300, 300))

cv2.imshow('asa', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
