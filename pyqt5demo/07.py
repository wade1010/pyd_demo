import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class Window1(QWidget):
    def __init__(self):
        super().__init__()
        QLabel('我是抽屉1要显示的内容', self)
        self.setStyleSheet('background-color:green;')


class Window2(QWidget):
    def __init__(self):
        super().__init__()
        QLabel('我是抽屉2要显示的内容', self)
        self.setStyleSheet('background-color:red;')


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.create_stacked_layout()
        self.init_ui()

    def create_stacked_layout(self):
        # 提供多个页面，一次只能看到一个
        self.stacked_layout = QStackedLayout()
        win1 = Window1()
        win2 = Window2()
        self.stacked_layout.addWidget(win1)
        self.stacked_layout.addWidget(win2)

    def init_ui(self):
        self.setFixedSize(300, 270)

        container = QVBoxLayout()

        widget = QWidget()
        widget.setLayout(self.stacked_layout)
        widget.setStyleSheet('background-color:grey;')

        btn1 = QPushButton('抽屉1')
        btn2 = QPushButton('抽屉2')
        btn1.clicked.connect(self.btn1_click)
        btn2.clicked.connect(self.btn2_click)

        container.addWidget(widget)
        container.addWidget(btn1)
        container.addWidget(btn2)
        self.setLayout(container)

    def btn1_click(self):
        self.stacked_layout.setCurrentIndex(0)

    def btn2_click(self):
        self.stacked_layout.setCurrentIndex(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    w.show()

    app.exec()
