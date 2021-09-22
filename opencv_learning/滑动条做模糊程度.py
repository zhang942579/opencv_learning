import cv2
import numpy as np



#图像膨胀函数
def img_dilated(img, d):
    #定义 kernel
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (d, d))
    #图像膨胀
    dilated = cv2.dilate(img, kernel)
    #返回膨胀图片
    return dilated

def nothing(pos):
    pass

img = cv2.imread('./imge/leimu.jpg', 1)
#创建老窗口
cv2.namedWindow('Oldimg')

#绑定老窗口和滑动条（滑动条的数值）
cv2.createTrackbar('D', 'Oldimg', 1, 30, nothing)

while True:
    #提取滑动条的数值d
    d = cv2.getTrackbarPos('D', 'Oldimg')
    #滑动条数字传入函数img_dilate中，并且调用函数img_dilated
    dilated = img_dilated(img, d)
    #绑定 img 和 dilated
    result = np.hstack([img, dilated])
    cv2.imshow('Oldimg', result)
    #设置退出键
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
