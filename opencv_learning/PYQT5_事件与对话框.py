import sys
from PyQt5.QtWidgets import (QWidget, QInputDialog, QPushButton, QApplication, QLabel)

class Name(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.le = QLabel('名字                  ', self)
        self.le.move(50, 60)
        self.btn = QPushButton('修改名字', self)
        self.btn.move(50, 80)
        self.btn.clicked.connect(self.showDialog)

        self.setGeometry(500, 500, 350, 200)
        self.setWindowTitle('你的名字')
        self.show()


    def showDialog(self):
        text, ok = QInputDialog.getText(self, '你的名字', '请输入你的名字：')

        if ok:
            self.le.setText(str(text))

app = QApplication(sys.argv)
ex = Name()
sys.exit(app.exec_())

