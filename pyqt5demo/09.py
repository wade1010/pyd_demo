import sys
import time

from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal, Qt


class MyWindow(QWidget):
    my_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.msg_history = list()

    def init_ui(self):
        self.resize(500, 200)
        self.msg = QLabel('')
        self.msg.resize(440, 15)
        self.msg.setWordWrap(True)
        self.msg.setAlignment(Qt.AlignTop)
        self.msg.setStyleSheet('background-color:yellow;color:black;')

        # 创建一个滚动对象
        scroll = QScrollArea()
        scroll.setWidget(self.msg)

        v_layout = QVBoxLayout()
        v_layout.addWidget(scroll)

        # 创建水平布局
        h_layout = QHBoxLayout()
        btn = QPushButton('开始检测',self)
        btn.clicked.connect(self.btn_click)
        h_layout.addStretch(1)
        h_layout.addWidget(btn)
        h_layout.addStretch(1)

        container = QVBoxLayout()
        container.addLayout(v_layout)
        container.addLayout(h_layout)
        self.setLayout(container)

        # 绑定信号和槽
        self.my_signal.connect(self.my_slot)
        pass

    def my_slot(self, msg):
        print(msg)
        self.msg_history.append(msg)
        self.msg.setText("<br>".join(self.msg_history))
        self.msg.resize(440, self.msg.frameSize().height() + 15)
        self.msg.repaint()  # 更新内容，如果不更新可能没有显示新内容

    def btn_click(self):
        # 后期需要放到线程，现在是同步代码，界面会卡
        self.msg_history.clear()
        for i, ip in enumerate(["192.168.1.%d" % x for x in range(1, 255)]):
            msg = "模拟，正在检查 %s 上的漏洞..." % ip
            # print("模拟，正在检查 %s 上的漏洞..." % ip, end="")
            if i % 5 == 0:
                self.my_signal.emit(msg + "【发现漏洞】")
            time.sleep(0.01)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    app.exec()
