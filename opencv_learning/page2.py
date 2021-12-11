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

        self.window_pale.setBrush(QPalette.Background, QBrush(QPixmap("./imge/seconder.png")))

        self.setPalette(self.window_pale)
        self.set_ui()  # 初始化程序界面


    def set_ui(self):
        #总体布局
        self.__layout_main = QtWidgets.QVBoxLayout()  # 总布局，垂直布局
        self.__layout_show = QtWidgets.QHBoxLayout()  #显示布局
        self.__layout_button = QtWidgets.QHBoxLayout()  # 按键布局，水平布局

        #定义显示
        self.back1 = QtWidgets.QLabel()  # 定义显示标签
        self.back1.setFixedSize(1600, 900)  # 设置标签尺寸



        #右按钮
        self.right = QtWidgets.QPushButton() #定义进入按钮
        self.right.setFont(QtGui.QFont("Roman times", 20, QtGui.QFont.Bold))
        self.right.setStyleSheet("QPushButton{background-image: url(./imge/right.png);border-radius:5;}")
        self.right.setFixedSize(128, 128)  # 设置按键尺寸
        #左按钮
        self.left = QtWidgets.QPushButton()  # 定义进入按钮
        self.left.setFont(QtGui.QFont("Roman times", 20, QtGui.QFont.Bold))
        self.left.setStyleSheet("QPushButton{background-image: url(./imge/left.png);border-radius:5;}")
        self.left.setFixedSize(128, 128)  # 设置按键尺寸
        #确认按钮
        self.confirm = QtWidgets.QPushButton()  # 定义进入按钮
        self.confirm.setFont(QtGui.QFont("Roman times", 20, QtGui.QFont.Bold))
        self.confirm.setStyleSheet("QPushButton{background-image: url(./imge/confirm.png);border-radius:5;}")
        self.confirm.setFixedSize(480, 128)  # 设置按键尺寸


        '''按键，放进显示布局中'''
        self.__layout_show.addWidget(self.left)
        self.__layout_show.addItem(QtWidgets.QSpacerItem(-780, 0))
        self.__layout_show.addWidget(self.confirm)
        self.__layout_show.addItem(QtWidgets.QSpacerItem(-780, 0))
        self.__layout_show.addWidget(self.right)


        '''将背景图放进显示布局中'''

        self.__layout_button.addWidget(self.back1)
        self.__layout_button.addItem(QtWidgets.QSpacerItem(0, 0))



        '''把显示，按键放进总布局'''
        self.__layout_main.addLayout(self.__layout_button)  # 把按键布局加到总布局中
        self.__layout_main.addItem(QtWidgets.QSpacerItem(10, -190))
        self.__layout_main.addLayout(self.__layout_show)
        self.__layout_main.addItem(QtWidgets.QSpacerItem(10, -190))

        '''总布局布置好后就可以把总布局作为参数传入下面函数'''
        self.setLayout(self.__layout_main)  # 到这步才会显示所有控件




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # 固定的，表示程序应用
    ui = Cover()  # 实例化Game_UI
    ui.show()  # 调用ui的show()以显示。同样show()是源于父类QtWidgets.QWidget的
    sys.exit(app.exec_())  # 不加这句，程序界面会一闪而过


