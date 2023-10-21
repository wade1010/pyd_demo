import sys
from PyQt5.QtWidgets import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        data = {
            0: ['7', '8', '9', '+', '('],
            1: ['4', '5', '6', '-', ')'],
            2: ['1', '2', '3', '*', '<-'],
            3: ['0', '.', '=', '/', 'C']
        }
        self.setWindowTitle('计算器')
        layout = QVBoxLayout()
        edit = QLineEdit()
        edit.setPlaceholderText('请输入内容')
        layout.addWidget(edit)

        grid = QGridLayout()
        for line_num, line_data in data.items():
            for col_num, text in enumerate(line_data):
                btn = QPushButton(text)
                grid.addWidget(btn, line_num, col_num)
        layout.addLayout(grid)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    w.show()

    app.exec()
