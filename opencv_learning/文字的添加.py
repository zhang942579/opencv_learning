import cv2
import numpy as np


img = cv2.imread('./imge/leimu.jpg')

font = cv2.FONT_HERSHEY_SIMPLEX
#openCV并不支持添加汉字
cv2.putText(img, 'Rem', (10, 00), font, 4, (255, 255, 255), 2)

cv2.imshow('huatu', img)

cv2.waitKey(0)
cv2.destroyAllWindows()



