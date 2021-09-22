import cv2
import numpy as np
#画圆
def draw_circle(event, x, y, flags, param):
    #如果双击左键
    if event == cv2.EVENT_LBUTTONDOWN:
        #画圆
        cv2.circle(img, (x, y), 100, (0, 255, 0), -1)
#创建图像与窗口并将窗口与回调函数绑定
img = np.zeros((512, 512, 3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while 1:
    cv2.imshow('image', img)
    #如果按下Esc键退出
    if cv2.waitKey(20)&0xFF == 27:
        break

cv2.destroyAllWindows()




