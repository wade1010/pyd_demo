import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread


class MyThread(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(10):
            print('是MyThread线程中执行...%d' % i)
            time.sleep(1)


class MyWin(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(500, 200)
        self.setWindowTitle('Form')
        line_edit = QLineEdit()
        line_edit.setPlaceholderText('请输入内容')

        h_layout = QHBoxLayout()
        btn1 = QPushButton('按钮1-卡')
        btn2 = QPushButton('按钮2-卡')
        h_layout.addStretch(1)
        h_layout.addWidget(btn1)
        h_layout.addWidget(btn2)
        h_layout.addStretch(1)

        container = QVBoxLayout()
        container.addWidget(line_edit)
        container.addLayout(h_layout)

        self.setLayout(container)

        btn1.clicked.connect(self.btn1_click)
        btn2.clicked.connect(self.btn2_click)

    def btn1_click(self):
        for i in range(10):
            print('是UI线程中执行...%d' % (i+1))
            time.sleep(1)

    def btn2_click(self):
        self.th = MyThread()
        self.th.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = MyWin()
    w.show()

    app.exec()
