import cv2
import numpy as np

#图像分辨率的修改
def ResolutionModification(path, size):
    w = size[0]
    h = size[1]
    img = cv2.imread(path)
    #cv2.resize() 参数1：要修改的图片；参数2：宽度与高度；参数3：插值方式，默认为双线性插值（INTER_LINEAR）这里选择4x4像素邻域的双三次插值。
    # INTER_NEAREST 最近邻插值
    # INTER_LINEAR 双线性插值（默认设置）
    # INTER_AREA 使用像素区域关系进行重采样。
    # INTER_CUBIC 4x4像素邻域的双三次插值
    # INTER_LANCZOS4 8x8像素邻域的Lanczos插值
    ladel = cv2.resize(img, (w, h), interpolation=cv2.INTER_CUBIC)

    # data=np.array(new_array, dtype='int32')
    return ladel
#修改的大小
size_a = [200, 200]
#要修改的图片路径
img_path = './imge/aixin2.jpg'
#调用函数
ladel = ResolutionModification(img_path, size_a)
#保存修改的图片路径
img_path2 = './imge/aixin4.jpg'
#保存修改后的图片
cv2.imwrite(img_path2, ladel)
#展示修改后的图片与修改前的图片
img1 = cv2.imread(img_path2)
img2 = cv2.imread(img_path)
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
# print(ladel[100])
cv2.waitKey(0)
cv2.destroyAllWindows()

