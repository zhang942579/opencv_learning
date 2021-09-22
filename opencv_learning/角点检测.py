import cv2
import numpy as np

img = cv2.imread('./imge/leimu.jpg')

cv2.imshow('leimu1', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 3, 23, 0.04)
print(dst.shape)
img[dst > 0.01 * dst.max()] = [255, 0, 0]
cv2.imshow('leimu2', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

