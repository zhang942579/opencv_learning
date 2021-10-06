import cv2
import numpy as np
import time
cap = cv2.VideoCapture(0)
print('摄像头是否已初始化：', cap.isOpened())
img_back = cv2.imread('./imge/kaishi.jpg')
# rows, cols, channels = img_back.shape
cap.open(0)
while True:
    # 获取每一帧
    ret, frame = cap.read()
    # rows, cols, channels = frame.shape
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    rows = frame.shape[0]
    cols = frame.shape[1]
    lower_blue = np.array([15, 55, 75])
    upper_blue = np.array([220, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    erode = cv2.erode(mask, None, iterations=1)
    # # cv2.imshow('erode', erode)
    dilate = cv2.dilate(erode, None, iterations=1)
    # cv2.imshow('dilate', dilate)
    # cv2.imshow('frame', frame)
    res = cv2.bitwise_and(frame, frame, mask=dilate)
    # center = [300, 300]  # 在新背景图片中的位置
    # img_back1 = img_back
    # for i in range(rows):
    #     for j in range(cols):
    #         if dilate[i, j] == 255:  # 0代表黑色的点
    #
    #             img_back[center[0] + i, center[1] + j] = frame[i, j]  # 此处替换颜色，为BGR通道

    cv2.imshow('dilate2', res)

    dst2 = cv2.addWeighted(res, 0.6, img_back, 0.4, 0)
    cv2.imshow('dilate5', dst2)
    k = cv2.waitKey(1) & 0xFF

    if k == 27:
        break

    elif k == ord('q'):
        cv2.imwrite('./imge/koutu.jpg', frame)
        img = cv2.imread('./imge/koutu.jpg')
        mask1 = np.zeros(img.shape[:2], np.uint8)
        bgdmodel = np.zeros((1, 65), np.float64)
        fbmodel = np.zeros((1, 65), np.float64)
        rect = (100, 80, 540, 400)
        cv2.grabCut(img, mask1, rect, bgdModel=bgdmodel, fgdModel=fbmodel, iterCount=4, mode=cv2.GC_INIT_WITH_RECT)
        mask2 = np.where((mask1 == 2) | (mask1 == 0), 0, 1).astype('uint8')  # 0和2做背景
        img = img * mask2[:, :, np.newaxis]  # 使用蒙板来获取前景区域
        dst2 = cv2.addWeighted(img, 0.8, img_back, 0.2, 0)
        cv2.imshow('Result map', dst2)




cap.release()
cv2.destroyAllWindows()

