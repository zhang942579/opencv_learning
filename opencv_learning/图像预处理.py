import cv2
img = cv2.imread('./imge/leimu.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('color', img)
cv2.imshow('gray', gray)

size, angle = map(float, input("请输入缩放系数和旋转角度：").split())
rows, cols = img.shape[:2]

M = cv2.getRotationMatrix2D((cols/2, rows/2), int(angle), size)

change = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow('Geometric transformation', change)

(b, g, r) = cv2.split(img)
bH = cv2.equalizeHist(b)
gH = cv2.equalizeHist(g)
rH = cv2.equalizeHist(r)
dst = cv2.merge((bH, gH, rH))

cv2.imshow('Histogram equalization', dst)
# cv2.imshow('blue', bH)
# cv2.imshow('red', gH)
# cv2.imshow('green', rH)
cv2.waitKey(0)
cv2.destroyAllWindows()
