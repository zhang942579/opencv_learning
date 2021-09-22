import math
import random
import sys

import cv2
import numpy as np
from PyQt5 import QtGui, QtCore, QtWidgets
from UI import main_UI

class GAME_UI(main_UI):
    def __init__(self):
        main_UI.__init__(self)
        self.timer_camera = QtCore.QTimer()  # 视频流
        self.timer_game = QtCore.QTimer()  # 游戏流
        self.timer_result = QtCore.QTimer()  # 计时流
        self.CAM_NUM = 0  # ’0‘表示内置摄像头，’1‘表示外界摄像头
        self.cap = cv2.VideoCapture(self.CAM_NUM)  # 读取摄像头
        self.img_size = 900  # 设置图片尺寸
        self.kernel = np.ones((5, 5), np.uint8)  # 设置卷积核
        self.slot_init()  # 初始化槽函数

    '''初始化所有槽函数'''

    def slot_init(self):
        self.button_open_camera.clicked.connect(self.button_open_camera_clicked)  # 若该按键被点击，则调用button_open_camera_clicked()
        self.timer_camera.timeout.connect(self.show_camera)  # 若定时器结束，则调用show_camera()
        self.button_start.clicked.connect(self.button_start_play_game)  # 若该按键被点击，则调用play_game()
        self.timer_game.timeout.connect(self.play_game)
        self.button_close.clicked.connect(self.close_game)  # 若该按键被点击，则调用close()，注意这个close是父类QtWidgets.QWidget自带的，会关闭程序
        self.timer_result.timeout.connect(self.showtime)

    '''基于HSV颜色空间的肤色识别'''

    def skin_detection_HSV(self, frame):
        low = np.array([2, 20, 30])  # 最低阈值
        high = np.array([40, 255, 255])  # 最高阈值
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # 转换到HSV空间
        mask = cv2.inRange(hsv, low, high)  # 掩膜，d不在范围内设为255
        skin = cv2.bitwise_and(frame, frame, mask=mask)  # 图像与运算
        return skin

    '''肤色识别'''

    def skin_detection_YCrCb(self, frame):
        YCrCb = cv2.cvtColor(frame, cv2.COLOR_BGR2YCR_CB)  # 转为CRCb颜色空间
        y, cr, cb = cv2.split(YCrCb)  # 划分通道
        cr1 = cv2.GaussianBlur(cr, (5, 5), 0)  # 高斯滤波
        _, skin = cv2.threshold(cr1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  # 阈值计算
        skin = cv2.bitwise_and(frame, frame, mask=skin)  # 图像与运算
        return skin

    '''轮廓检测'''

    def contour_detection(self, frame, skin):
        gray = cv2.cvtColor(skin, cv2.COLOR_BGR2GRAY)  # 灰度处理
        dst = cv2.Laplacian(gray, cv2.CV_16S, ksize=3)  # 拉普拉斯变换
        laplacian = cv2.convertScaleAbs(dst)  # 图像增强
        cont = cv2.findContours(laplacian, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # 寻找轮廓
        if len(cont) > 0:
            contour = cont[1]
            contour = sorted(contour, key=cv2.contourArea, reverse=True)  # 已轮廓区域面积进行排序
            contour = cv2.drawContours(frame, contour[0], -1, (255, 0, 0), 4)  # 绘制黑色轮廓
        return contour

    '''凸包检测'''

    def calculateFingers(self, skin):
        drawing = np.zeros(skin.shape, np.uint8)  # 建造画布
        gray = cv2.cvtColor(skin, cv2.COLOR_BGR2GRAY)  # 灰度处理
        dst = cv2.Laplacian(gray, cv2.CV_16S, ksize=3)  # 拉普拉斯变换
        laplacian = cv2.convertScaleAbs(dst)  # 图片增强
        contours = cv2.findContours(laplacian, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # 寻找轮廓
        length = len(contours)
        maxArea = -1
        # 寻找最大的轮廓
        if length > 0:
            for i in range(length):
                temp = contours[i]
                area = cv2.contourArea(temp)
                if area > maxArea:
                    maxArea = area
                    ci = 1
            res = contours[ci]
        hull = cv2.convexHull(res, returnPoints=False)  # 计算凸包
        if len(hull) > 3:
            defects = cv2.convexityDefects(res, hull)  # 凸包检测
            if type(defects) != type(None):
                cnt = 0
                # 计算角度
                for i in range(defects.shape[0]):
                    s, e, f, d = defects[i][0]
                    start = tuple(res[s][0])
                    end = tuple(res[e][0])
                    far = tuple(res[f][0])
                    a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
                    b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
                    c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
                    angle = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))  # 余弦定理
                    if angle <= math.pi / 2.4:  # 如果角小于90度，则判定为手指
                        cnt += 1  # 手指数
                        cv2.circle(drawing, far, 8, [211, 84, 0], -1)  # 根据给定的圆心和半径等画圆
                return True, cnt
        return False, 0
    #打开摄像头
    def button_open_camera_clicked(self):
        if self.timer_camera.isActive() == False: #若定时器未启动
            flag = self.cap.open(self.CAM_NUM)    #参数是0，表示打开笔记本的内置摄像头，参数是视频文件路径则打开视频

            if flag == False:
                QtWidgets.QMessageBox.warning(self, 'warning', "请检查相机与电脑是否链接正确", buttons=QtWidgets.QMessageBox.OK)
            else:
                self.timer_camera.start(30)      #定时器开始计时30ms，结果是每过30秒从摄像头中取一帧显示
                self.button_open_camera.setStyleSheet("QPushButton{background-image:url(./imge/close_camera.png);border-radius:22;}")
        else:
            self.button_open_camera.setStyleSheet("QPushButton{background-image:url(./imge/open_camera.png);border-radius:22;}")
            self.timer_camera.stop() #关闭定时器
            self.cap.release()       #释放视频流
            self.label_show_camera.clear()#清空视频显示区域
            self.label_result_player.clear()#清空标签内容
            self.label_result_pc.clear()  #清空标签内容
            self.label_result.clear()     #清空标签内容


    #摄像头调用
    def show_camera(self):
        flag, self.image = self.cap.read()     #从视频流中获取
        show = cv2.resize(self.image, (self.img_size, self.img_size))#把读到的帧尺寸重新设置
        show = cv2.flip(show, 1)                #水平翻转视频
        skin = self.skin_detection_YCrCb(show)  #肤色识别
        show = self.contour_detection(show, skin)#轮廓添加
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)#视频色彩转换回RGB， 这样才是现实的颜色
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)#把读取到得到的视频数据完成QImage形式
        self.label_show_camera.setPixmap(QtGui.QPixmap.fromImage(showImage))#往显示视频的Label里显示QImage





    '''开始游戏'''
    def button_start_play_game(self):
        if self.timer_game.isActive() == False:   #若定时器未启动
            flag = self.cap.open(self.CAM_NUM)    #参数是0，表示打开笔记本的内置摄像头，参数是视频文件路径则打开视频
            if flag == False:   #flag表示open成不成功
                QtWidgets.QMessageBox.warning(self, 'warning', "请检查相机与电脑是否连接正确", buttons=QtWidgets.QMessageBox.Ok)
            else:
                self.timer_game.start(5000)   #定时器开始计时5秒，结果是没过30ms从摄像头中取一帧显示
                self.button_start.setStyleSheet("QPushButton{background-image:url(./imge/close_game.png);border-radius:20;}")
                self.time = 4
                self.starttimer()
        else:
            self.button_start.setStyleSheet("QPushButton{background-image:url(./imge/start_game.png);border-radius:20;}")
            self.timer_game.stop()#关闭定时器
            self.label_show_camera.clear()  # 清空视频显示区域
            self.label_result_player.clear()  # 清空标签内容
            self.label_result_pc.clear()  # 清空标签内容
            self.label_result.clear()  # 清空标签内容


    '''游戏判断'''
    def judge(self, hull):
        if hull <= 0:
            Player = 1  #石头

        elif hull <= 3:
            Player = 2   #剪刀

        else:
            Player = 0   #布

        pc = random.randint(0, 2)
        #电脑将从0， 1， 2中随机选取一个数， 其中0， 1， 2分别是布，石头，剪刀
        if pc == 0:
            self.label_result_pc.setPixmap(QtGui.QPixmap("imge/paper.png"))
            if Player == 0:
                self.label_result_player.setPixmap(QtGui.QPixmap("imge/paper.png"))
                self.label_result.setPixmap(QtGui.QPixmap("imge/ping.png"))
            elif Player == 1:
                self.label_result_player.setPixmap(QtGui.QPixmap("imge/rock.png"))
                self.label_result.setPixmap(QtGui.QPixmap("imge/lose.png"))

            else:
                self.label_result_player.setPixmap(QtGui.QPixmap("imge/scissors.png"))
                self.label_result.setPixmap(QtGui.QPixmap("imge/win.png"))
        elif pc == 1:
            self.label_result_pc.setPixmap(QtGui.QPixmap("imge/rock.png"))
            if Player == 0:
                self.label_result_player.setPixmap(QtGui.QPixmap("imge/paper.png"))
                self.label_result.setPixmap(QtGui.QPixmap("imge/win.png"))
            elif Player == 1:
                self.label_result_player.setPixmap(QtGui.QPixmap("imge/rock.png"))
                self.label_result.setPixmap(QtGui.QPixmap("imge/ping.png"))

            else:
                self.label_result_player.setPixmap(QtGui.QPixmap("imge/scissors.png"))
                self.label_result.setPixmap(QtGui.QPixmap("imge/lose.png"))

        else:
            self.label_result_pc.setPixmap(QtGui.QPixmap("imge/scissors.png"))
            if Player == 0:
                self.label_result_player.setPixmap(QtGui.QPixmap("imge/paper.png"))
                self.label_result.setPixmap(QtGui.QPixmap("imge/lose.png"))
            elif Player == 1:
                self.label_result_player.setPixmap(QtGui.QPixmap("imge/rock.png"))
                self.label_result.setPixmap(QtGui.QPixmap("imge/win.png"))

            else:
                self.label_result_player.setPixmap(QtGui.QPixmap("imge/scissors.png"))
                self.label_result.setPixmap(QtGui.QPixmap("imge/ping.png"))

    '''游戏程序'''

    def play_game(self):
        flag, self.image = self.cap.read()  # 从视频流读取图像
        self.image = cv2.resize(self.image, (self.img_size, self.img_size))  # 改变图像大小
        skin = self.skin_detection_YCrCb(self.image)  # 手势提取
        skin = cv2.erode(skin, self.kernel)
        skin = cv2.dilate(skin, self.kernel)  # 膨胀操作
        _, hull = self.calculateFingers(skin)   # 计算凸包
        self.time = 4
        self.starttimer()
        self.judge(hull)


    '''定时器'''
    def showtime(self):
        self.time -= 1
        self.label_result.setText(str(self.time))
        self.label_result.setAlignment(QtCore.Qt.AlignCenter)#设置标签居中
        self.label_result.setFont(QtGui.QFont("Roman times", 50, QtGui.QFont.Bold))  #设置标签的字体相关信息
        self.label_result_player.clear()  #清空标签内容
        self.label_result_pc.clear()  # 清空标签内容
        if self.time == 1:
            self.endtimer()

    def starttimer(self):
        self.timer_result.start(1000)

    def endtimer(self):
        self.timer_result.stop()



    '''关闭游戏'''

    def close_game(self):
        self.button_close.setStyleSheet("QPushButton{background-image: url(./imge/close_new.png);border-radius:20;}")
        QtWidgets.QMessageBox.information(self, '退出游戏', "欢迎下次!", buttons=QtWidgets.QMessageBox.Ok)
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # 固定的，表示程序应用
    ui = GAME_UI()  # 实例化Game_UI
    ui.show()  # 调用ui的show()以显示。同样show()是源于父类QtWidgets.QWidget的
    sys.exit(app.exec_())  # 不加这句，程序界面会一闪而过







