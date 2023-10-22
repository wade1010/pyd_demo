import json
import sys
import time
import requests
from PyQt5.QtWidgets import *
from feiq_ui import Ui_Form
from PyQt5.QtCore import QThread, pyqtSignal


class LoginThread(QThread):
    login_signal = pyqtSignal(str)

    def __init__(self, signal):
        super().__init__()
        self.login_compete_signal = signal

    def run(self) -> None:
        while True:
            print('子线程正在执行....')
            time.sleep(1)

    def login_by_request(self, user_info_json):
        user_info_dict = json.loads(user_info_json)
        print(user_info_dict.get('username'))
        print(user_info_dict.get('password'))
        print('模拟登录中....')
        time.sleep(1)
        if user_info_dict.get('username') == 'admin' and user_info_dict.get('password') == '123456':
            msg = '登录成功'
        else:
            msg = '用户名或密码错误'
        self.login_compete_signal.emit(json.dumps({
            'msg': msg
        }))


class MyWindow(QWidget, Ui_Form):
    login_status_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.login_click)

        self.login_status_signal.connect(self.login_status)

        self.login_thread = LoginThread(self.login_status_signal)
        self.login_thread.login_signal.connect(
            self.login_thread.login_by_request
        )
        self.login_thread.start()

    def login_click(self):
        self.textBrowser.setText('')
        self.textBrowser.repaint()
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        self.login_thread.login_signal.emit(json.dumps({
            'username': username,
            'password': password
        }))

    def login_status(self, status_json):
        print('login status:', status_json)
        status_dict = json.loads(status_json)
        self.textBrowser.setText(status_dict.get('msg'))
        self.textBrowser.repaint()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = MyWindow()
    w.show()

    app.exec()
