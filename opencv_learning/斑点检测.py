from cv2 import cv2


img = cv2.imread('./imge/leimu.jpg')
cv2.imshow('leimu1', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#sift为实例化的sift函数
sift = cv2.SIFT_create()
#kp表示生成的关键点，gray表示输入的灰度图
kp = sift.detect(gray, None) #找出图像的关键点
#gray表示输入图片, kp表示关键点，img表示输出的图片
img = cv2.drawKeypoints(gray, kp, img)#在图中画出关键点
cv2.imshow('leimu2', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
