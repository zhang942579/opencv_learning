import cv2

red = [0, 0, 255]
img = cv2.imread('./imge/leimu.jpg')

replicat = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img,  20, 20, 20, 20, cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img,  20, 20, 20, 20, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img,  20, 20, 20, 20, cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img,  20, 20, 20, 20, cv2.BORDER_CONSTANT, value=red)


cv2.imshow('1', replicat)
cv2.imshow('2', reflect)
cv2.imshow('3', reflect101)
cv2.imshow('4', wrap)
cv2.imshow('5', constant)

cv2.waitKey(0)
cv2.destroyAllWindows()

