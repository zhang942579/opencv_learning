import cv2
import numpy as np


img = cv2.imread('./imge/leimu.jpg')

ball = img[446:491, 476:605]
img[446:491, 0:129] = ball

cv2.imshow('green', img)

cv2.waitKey(0)
cv2.destroyAllWindows()


