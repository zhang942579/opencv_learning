import cv2
import numpy as np
import time
img = cv2.imread('./imge/leimu.jpg')
#当鼠标按下时变为True
drawing = False

#如果 mode 为 true 绘制矩形，按下'm'变成绘制曲线。
mode = True
ix, iy = -1, -1
#画圆
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode
    #如果按下左键是返回起始位置坐标
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        if drawing == True:
            if mode == True:
                #绘制小矩形
                cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 255), -1)
            else:
                #绘制小圆圈
                cv2.circle(img, (x, y), 3, (0, 255, 0), -1)
    elif event == cv2.EVENT_LBUTTONUP:
         drawing = False


#创建图像与窗口并将窗口与回调函数绑定

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while 1:
    cv2.imshow('image', img)
    k = cv2.waitKey(1)&0xFF
    #按下m转换模式
    if k == ord('m'):
        mode = not mode
    #按下q结束
    elif k == ord('q'):
        break

