import sys
from PyQt5 import QtWidgets
# from PyQt5.QtCore import *
# from PyQt5.QtWidgets import *  # QFileDialog, QMessageBox, QDockWidget, QListWidget
# from PyQt5.QtGui import *
import random

from GUI import Ui_MainWindow  # 导入创建的GUI类

class mywindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)

        # setting main window geometry
        desktop_geometry = QtWidgets.QApplication.desktop()  # 获取屏幕大小
        main_window_width = desktop_geometry.width()  # 屏幕的宽
        main_window_height = desktop_geometry.height()  # 屏幕的高
        rect = self.geometry()  # 获取窗口界面大小
        window_width = rect.width()  # 窗口界面的宽
        window_height = rect.height()  # 窗口界面的高
        x = (main_window_width - window_width) // 2  # 计算窗口左上角点横坐标
        y = (main_window_height - window_height) // 2  # 计算窗口左上角点纵坐标
        self.setGeometry(x, y, window_width, window_height)  # 设置窗口界面在屏幕上的位置
        self.pushButton.clicked.connect(self.pushbutton_fuction)

    def pushbutton_fuction(self):
        # 定义一个空列表存储随机数
        try:
            a = int(self.lineEdit.text())
            b = int(self.lineEdit_2.text())
            c = int(self.lineEdit_3.text())
        except ValueError:
            return

        a_list = []
        while len(a_list) < c:
            d_int = random.randint(a, b)
            if (d_int not in a_list):
                a_list.append(d_int)
            else:
                pass
        # 将生成的随机数列表转换成元组并返回
        # print(tuple(a_list))
        a_list.sort(reverse=True)
        str1 = ""
        for gift in a_list:
            str1 = str(gift)+" "+str1
        # print(int_random(a_int, b_int, c_int))
        self.lineEdit_4.setText(str1)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())




