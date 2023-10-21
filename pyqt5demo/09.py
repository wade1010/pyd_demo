import sys
import time

from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal


class MyWindow(QWidget):
    my_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(500, 300)
        btn = QPushButton('点我', self)
        btn.setGeometry(200, 200, 100, 30)
        btn.clicked.connect(self.btn_click)

        # 绑定信号和槽
        self.my_signal.connect(self.my_slot)
        pass

    def my_slot(self, msg):
        print(msg)

    def btn_click(self):
        for i, ip in enumerate(["192.168.1.%d" % x for x in range(1, 255)]):
            print("模拟，正在检查 %s 上的漏洞..." % ip, end="")
            if i % 5 == 0:
                self.my_signal.emit("发现漏洞")
            else:
                self.my_signal.emit('')
            time.sleep(0.01)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    app.exec()
