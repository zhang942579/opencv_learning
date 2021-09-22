import cv2

img1 = cv2.imread('./imge/leimu.jpg')
img2 = cv2.imread('./imge/aixin4.jpg')
#设置一个ROI
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]
cv2.imshow('roi', roi)
#灰度图
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#使用二值化函数cv2.threshold()将灰度图二值化
ret, mask = cv2.threshold(img2gray, 200, 255, cv2.THRESH_BINARY)
cv2.imshow('gray', mask)
#使用“非”操作函数cv2.bitwise_not()将上图颠倒黑白
mask_inv = cv2.bitwise_not(mask)
#使用“与”操作函数cv2.bitwise_and()对图像掩膜（遮挡）：对操作区域掩膜：
img1_bg = cv2.bitwise_and(roi, roi, mask=mask)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask_inv)
#图像相加
dst = cv2.add(img1_bg, img2_fg)
#覆盖操作区域，就得到了最后结果
img1[0:rows, 0:cols] = dst

cv2.imshow('res', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()