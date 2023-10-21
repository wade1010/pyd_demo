import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi('pyqt5demo\designer\login.ui')
        print(self.ui.__dict__)
        print(self.ui.label.text())
        self.user_name = self.ui.lineEdit
        self.password = self.ui.lineEdit_2
        login_btn = self.ui.pushButton
        forget_btn = self.ui.pushButton_2
        text_browser = self.ui.textBrowser

        login_btn.clicked.connect(self.login_click)

    def login_click(self):
        print('do login ing...')
        username = self.user_name.text()
        password = self.password.text()
        print(username, password)
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = MyWindow()
    w.ui.show()

    app.exec()
