import cv2
import numpy as np

#调用摄像头
cap = cv2.VideoCapture(0)
print('摄像头是否已初始化：', cap.isOpened())
cap.open(0)
while True:
    #获取每一帧
    ret, frame = cap.read()
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #cv2.imshow('frame1', gray)

    cv2.imshow('frame2', frame)
    #如果按q就保存图像并退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite('./imge/paizhao.jpg', frame)
        break


#关闭摄像头
cap.release()
cv2.destroyAllWindows()