import sys
from PyQt5.QtWidgets import *
from login_ui import Ui_Form

# 使用vscode生成的调用方法


class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = MyWindow()
    w.show()

    app.exec()


# 在课程后半段的加载制作好的ui文件那部分，老师使用uic中的的方法进行导入没有自动补全，
# 上网查找资料才得知，这个ui加载方法有很多种，其中一种是可继承的，可以将ui文件转为py文件
# 然后把这个py文件中定义窗口的类导入 具体可以看一看导出的py。我这里显示的定义窗口的类名是Ui_MainWindow
# 然后再把class MyWindows(QMainWindow): 改成 class MyWindows(QMainWindow, Ui_MainWindow): 添加一下父类，
# 最后在初始化函数里面写一下 转化的py文件中的绘制窗口的函数就可以了 我的是self.setupUi(self)
