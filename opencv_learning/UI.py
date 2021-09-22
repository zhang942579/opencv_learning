from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QPalette, QBrush, QPixmap

class main_UI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("石头剪刀布游戏")  # 设置窗口标题
        self.setWindowIcon(QtGui.QIcon('imge/scissors.png'))  # 设置窗口的图标
        self.setFixedSize(1360, 920)
        self.window_pale = QtGui.QPalette()
        self.window_pale.setBrush(QPalette.Background, QBrush(QPixmap("imge/UInews.jpg")))
        self.setPalette(self.window_pale)
        self.set_ui()  # 初始化程序界面

    '''程序界面化布局'''
    def set_ui(self):
        self.__layout_main = QtWidgets.QVBoxLayout()  # 总布局，垂直布局
        self.__layout_show = QtWidgets.QHBoxLayout()  # 显示布局，水平布局
        self.__layout_result = QtWidgets.QVBoxLayout()  # 结果布局，垂直布局
        self.__layout_button = QtWidgets.QHBoxLayout()  # 按键布局，水平布局
        '''相机'''
        self.label_show_camera = QtWidgets.QLabel()  # 定义显示视频标签
        self.label_show_camera.setFrameShape(QtWidgets.QFrame.Box)
        self.label_show_camera.setFixedSize(785, 560)  # 设置标签尺寸
        self.label_show_camera.setStyleSheet("QLabel{border-radius:75;}")
        '''结果'''
        self.label_result_player = QtWidgets.QLabel()  # 定义显示玩家标签
        self.label_result_player.setFixedSize(150, 175)  # 设置标签尺寸
        self.label_result_pc = QtWidgets.QLabel()  # 定义显示电脑标签
        self.label_result_pc.setFixedSize(150, 175)  # 设置标签尺寸
        self.label_result = QtWidgets.QLabel()  # 定义显示结果标签
        self.label_result.setFixedSize(150, 175)  # 设置标签尺寸
        '''相机按键'''
        self.button_open_camera = QtWidgets.QPushButton()  # 定义摄像头按钮
        self.button_open_camera.setFont(QtGui.QFont("Roman times", 15, QtGui.QFont.Bold))
        self.button_open_camera.setShortcut(QtGui.QKeySequence(65))  # 设置快捷键A
        self.button_open_camera.setStyleSheet("QPushButton{background-image: url(./imge/open_camera.png);border-radius:5;}")
        self.button_open_camera.setFixedSize(315, 60)  # 设置按键尺寸
        '''开始按键'''
        self.button_start = QtWidgets.QPushButton()  # 定义游戏按钮
        self.button_start.setFont(QtGui.QFont("Roman times", 20, QtGui.QFont.Bold))
        self.button_start.setShortcut(QtGui.QKeySequence(83))  # 设置快捷键S
        self.button_start.setStyleSheet("QPushButton{background-image: url(./imge/start_game.png);border-radius:5;}")
        self.button_start.setFixedSize(315, 60)  # 设置按键尺寸
        '''结束按键'''
        self.button_close = QtWidgets.QPushButton()  # 定义退出按钮
        self.button_close.setFont(QtGui.QFont("Roman times", 20, QtGui.QFont.Bold))
        self.button_close.setShortcut(QtGui.QKeySequence(68))  # 设置快捷键D
        self.button_close.setStyleSheet("QPushButton{background-image: url(./imge/close.png);border-radius:5;}")
        self.button_close.setFixedSize(315, 60)  # 设置按键尺寸
        '''把结果放进结果布局'''
        self.__layout_result.addItem(QtWidgets.QSpacerItem(20, 40))  # 把玩家标签加到结果控件布局中
        self.__layout_result.addWidget(self.label_result_player)  # 把显示玩家标签加到结果控件布局中
        self.__layout_result.addItem(QtWidgets.QSpacerItem(20, 15))  # 把玩家标签加到结果控件布局中
        self.__layout_result.addWidget(self.label_result_pc)  # 把显示电脑标签加到结果控件布局中
        self.__layout_result.addItem(QtWidgets.QSpacerItem(20, 15))  # 把玩家标签加到结果控件布局中
        self.__layout_result.addWidget(self.label_result)  # 把显示结果标签加到结果控件布局中
        self.__layout_result.addItem(QtWidgets.QSpacerItem(20, 30))  # 把玩家标签加到结果控件布局中
        '''把相机，结果放进显示布局'''
        self.__layout_show.addWidget(self.label_show_camera)
        self.__layout_show.addItem(QtWidgets.QSpacerItem(75, 20))
        self.__layout_show.addLayout(self.__layout_result)
        self.__layout_show.addItem(QtWidgets.QSpacerItem(80, 20))
        '''把按键放进按键布局'''
        self.__layout_button.addWidget(self.button_open_camera)
        self.__layout_button.addItem(QtWidgets.QSpacerItem(55,15))
        self.__layout_button.addWidget(self.button_start)
        self.__layout_button.addItem(QtWidgets.QSpacerItem(55, 15))
        self.__layout_button.addWidget(self.button_close)
        '''把显示，按键放进总布局'''
        self.__layout_main.addItem(QtWidgets.QSpacerItem(20,95))
        self.__layout_main.addLayout(self.__layout_show)  # 把图像布局加到总布局中
        self.__layout_main.addLayout(self.__layout_button)  # 把按键布局加到总布局中
        self.__layout_main.addItem(QtWidgets.QSpacerItem(20, 35))
        '''总布局布置好后就可以把总布局作为参数传入下面函数'''
        self.setLayout(self.__layout_main)  # 到这步才会显示所有控件