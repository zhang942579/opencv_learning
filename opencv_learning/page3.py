from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QPalette, QBrush, QPixmap
import sys


class Cover(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("火星合影")  # 设置窗口标题
        self.setWindowIcon(QtGui.QIcon('./imge/tubiao.png'))  # 设置窗口的图标
        self.setFixedSize(2560, 1440)
        self.window_pale = QtGui.QPalette()

        self.window_pale.setBrush(QPalette.Background, QBrush(QPixmap("./imge/third.png")))

        self.setPalette(self.window_pale)
        self.set_ui()  # 初始化程序界面


    def set_ui(self):
        #总体布局
        self.__layout_main = QtWidgets.QVBoxLayout()  # 总布局，垂直布局
        self.__layout_show = QtWidgets.QHBoxLayout()  # 显示和返回按键布局
        self.__layout_button = QtWidgets.QHBoxLayout()  # 按键布局，水平布局
        self.__layout_f = QtWidgets.QHBoxLayout()
        #定义视频
        self.label_show_camera = QtWidgets.QLabel()  # 定义显示视频标签
        self.label_show_camera.setFrameShape(QtWidgets.QFrame.Box)
        self.label_show_camera.setFixedSize(1840, 1036)  # 设置标签尺寸
        self.label_show_camera.setStyleSheet("QLabel{border-radius:75;}")
        # self.shows = QtWidgets.QPushButton()  # 定义进入按钮
        # self.shows.setFont(QtGui.QFont("Roman times", 20, QtGui.QFont.Bold))
        # self.shows.setStyleSheet("QPushButton{background-image: url(./imge/show.png);border-radius:5;}")
        # self.shows.setFixedSize(1840, 1036)  # 设置按键尺寸
        #返回按钮
        self.returns = QtWidgets.QPushButton()  # 定义进入按钮
        self.returns.setFont(QtGui.QFont("Roman times", 20, QtGui.QFont.Bold))
        self.returns.setStyleSheet("QPushButton{background-image: url(./imge/returns.png);border-radius:5;}")
        self.returns.setFixedSize(100, 101)  # 设置按键尺寸



        #拍照按钮
        self.photograph = QtWidgets.QPushButton() #定义进入按钮
        self.photograph.setFont(QtGui.QFont("Roman times", 20, QtGui.QFont.Bold))
        self.photograph.setStyleSheet("QPushButton{background-image: url(./imge/photograph.png);border-radius:5;}")
        self.photograph.setFixedSize(480, 128)  # 设置按键尺寸

        '''按键，放进显示布局中'''
        self.__layout_button.addWidget(self.photograph)
        self.__layout_button.addItem(QtWidgets.QSpacerItem(0, 0))
        '''返回按键和视频放进显示布局'''
        # self.__layout_show.addWidget(self.returns)
        # self.__layout_show.addItem(QtWidgets.QSpacerItem(30, 300))
        self.__layout_show.addWidget(self.label_show_camera)
        self.__layout_show.addItem(QtWidgets.QSpacerItem(0, 0))
        self.__layout_f.addWidget(self.returns)
        self.__layout_f.addItem(QtWidgets.QSpacerItem(2300, 0))

        '''把显示，按键放进总布局'''
        self.__layout_main.addLayout(self.__layout_f)  # 把按键布局加到总布局中
        self.__layout_main.addItem(QtWidgets.QSpacerItem(20, -50))
        self.__layout_main.addLayout(self.__layout_show)  # 把按键布局加到总布局中
        self.__layout_main.addItem(QtWidgets.QSpacerItem(20, 20))
        self.__layout_main.addLayout(self.__layout_button)  # 把按键布局加到总布局中
        self.__layout_main.addItem(QtWidgets.QSpacerItem(20, 90))



        '''总布局布置好后就可以把总布局作为参数传入下面函数'''
        self.setLayout(self.__layout_main)  # 到这步才会显示所有控件



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # 固定的，表示程序应用
    ui = Cover()  # 实例化Game_UI
    ui.show()  # 调用ui的show()以显示。同样show()是源于父类QtWidgets.QWidget的
    sys.exit(app.exec_())  # 不加这句，程序界面会一闪而过













