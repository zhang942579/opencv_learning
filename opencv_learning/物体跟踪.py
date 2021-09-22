import cv2
import numpy as np

cap = cv2.VideoCapture(0)
print('摄像头是否已初始化：', cap.isOpened())
cap.open(0)

while 1:

    #获取每一帧
    ret, frame = cap.read()

    #转换到 HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #设置蓝色的侷值
    lower_blue = np.array([20, 100, 100])
    upper_blue = np.array([220, 255, 255])

    #根据侷值构建掩膜
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    #对原图像和掩膜进行位运算
    res = cv2.bitwise_and(frame, frame, mask=mask)

    #显示图像
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    k = cv2.waitKey(5)& 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()






