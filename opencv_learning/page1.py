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

        self.window_pale.setBrush(QPalette.Background, QBrush(QPixmap("./imge/first.png")))

        self.setPalette(self.window_pale)
        self.set_ui()  # 初始化程序界面


    def set_ui(self):
        #总体布局
        self.__layout_main = QtWidgets.QVBoxLayout()  # 总布局，垂直布局

        self.__layout_button = QtWidgets.QHBoxLayout()  # 按键布局，水平布局


        #进入按钮
        self.into = QtWidgets.QPushButton() #定义进入按钮
        self.into.setFont(QtGui.QFont("Roman times", 20, QtGui.QFont.Bold))
        self.into.setStyleSheet("QPushButton{background-image: url(./imge/into.png);border-radius:5;}")
        self.into.setFixedSize(480, 128)  # 设置按键尺寸

        '''按键，放进显示布局中'''
        self.__layout_button.addWidget(self.into)
        self.__layout_button.addItem(QtWidgets.QSpacerItem(-220, -100))



        '''把显示，按键放进总布局'''

        self.__layout_main.addLayout(self.__layout_button)  # 把按键布局加到总布局中
        self.__layout_main.addItem(QtWidgets.QSpacerItem(-635, -635))
        '''总布局布置好后就可以把总布局作为参数传入下面函数'''
        self.setLayout(self.__layout_main)  # 到这步才会显示所有控件


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # 固定的，表示程序应用
    ui = Cover()  # 实例化Game_UI
    ui.show()  # 调用ui的show()以显示。同样show()是源于父类QtWidgets.QWidget的
    sys.exit(app.exec_())  # 不加这句，程序界面会一闪而过


