import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout, QPushButton, QApplication)

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        names = ['橊', '藅', '殛', '囖',
                 '藞', '刘', '垰', '掱',
                 '逼', '鲾', '謯', '杰',
                 '傻', '鬻', '鵼', '瀔',
                 '戽', '逼', '釐', '廤']
        positions = [(i, j) for i in range(5) for j in range(4)]
        for position,name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)
        self.move(300, 150)
        self.setWindowTitle('读出认识的字')
        self.show()


app = QApplication(sys.argv)
ex = Calculator()
sys.exit(app.exec_())
