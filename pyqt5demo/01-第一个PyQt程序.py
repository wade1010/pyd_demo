# https://doc.qt.io/qt-5/classes.html
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QDesktopWidget
from PyQt5.QtGui import QIcon
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("第一个PyQt")
    # btn = QPushButton('按钮')
    # btn.setParent(w)
    # label = QLabel("账号：")
    # label.setParent(w)
    w.setWindowIcon(QIcon('icon.png'))

    label = QLabel("账号：", w)
    label.setGeometry(20, 20, 30, 30)

    edit = QLineEdit(w)
    edit.setPlaceholderText('请输入账号')
    edit.setGeometry(55, 20, 200, 20)

    btn = QPushButton('注册', w)
    btn.setGeometry(50, 80, 70, 30)

    w.resize(300, 200)
    w.move(0, 0)

    # 调整窗口在屏幕中央显示

    center_pointer = QDesktopWidget().availableGeometry().center()
    print(center_pointer)
    x = center_pointer.x()
    y = center_pointer.y()
    # w.move(x, y)

    old_x, old_y, width, height = w.frameGeometry().getRect()
    w.move(x-int(width/2), y-int(height/2))
    w.show()
    app.exec_()
