import sys
import time
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
        self.login_btn = self.ui.pushButton
        self.forget_btn = self.ui.pushButton_2
        self.text_browser = self.ui.textBrowser

        self.login_btn.clicked.connect(self.login_click)

    def login_click(self):
        print('do login ing...')
        username = self.user_name.text()
        password = self.password.text()
        # 单线程 执行期间会卡
        for i in range(10):
            print('正在登录服务器...%d' % (i+1))
            time.sleep(1)
        print(username, password)
        if username == "admin" and password == '123456':
            self.text_browser.setText('欢迎%s' % username)
        else:
            self.text_browser.setText('用户名或密码错误...请重试')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = MyWindow()
    w.ui.show()

    app.exec()
