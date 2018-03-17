# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import qrcode

class make_QRcode(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.initui()

    def initui(self):
        self.setsize1()
        self.setWindowIcon(QtGui.QIcon('./icon/icon.ico'))
        self.setWindowTitle("二维码生成器")
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setToolTip("这是一个生成二维码的软件")
        self.statusBar().showMessage("欢迎使用本软件")
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Background, QtGui.QColor(203, 255, 252))
        self.setPalette(palette)

        self.make_action()
        self.make_Menu()

        self.make_page1()
        # self.make_page2()

        self.setCentralWidget(self.page1_main_ground)


    def make_page1(self):
        self.page1_logo()
        self.page1_input()
        self.page1_show()
        self.page1_toolbt()

        self.page1_box = QtWidgets.QVBoxLayout()
        self.page1_box.addStretch(1)
        self.page1_box.addLayout(self.page1_logo_box)
        self.page1_box.addStretch(1)
        self.page1_box.addLayout(self.page1_input_box)
        self.page1_box.addStretch(1)
        self.page1_box.addLayout(self.page1_show_box)
        self.page1_box.addStretch(1)
        self.page1_box.addLayout(self.page1_toolbt_box)
        # self.page1_box.addStretch(1)

        self.page1_main_ground = QtWidgets.QWidget()
        self.page1_main_ground.setLayout(self.page1_box)


    def page1_logo(self):
        self.page1_logo_lb = QtWidgets.QLabel("二维码生成器")
        self.page1_logo_lb.setFont(QtGui.QFont("黑体", self.size_.width()*0.06))

        self.page1_logo_box = QtWidgets.QHBoxLayout()
        self.page1_logo_box.addStretch(1)
        self.page1_logo_box.addWidget(self.page1_logo_lb)
        self.page1_logo_box.addStretch(1)

    def page1_input(self):
        self.page1_input_words = QtWidgets.QLabel(r"网址/内容")
        self.page1_input_words.setFont(QtGui.QFont("黑体", 10))

        self.page1_input_text = QtWidgets.QLineEdit()

        self.page1_input_box = QtWidgets.QHBoxLayout()
        # self.page1_input_box.addStretch(1)
        self.page1_input_box.addWidget(QtWidgets.QLabel("     "))
        self.page1_input_box.addWidget(self.page1_input_words)
        self.page1_input_box.addWidget(self.page1_input_text)
        self.page1_input_box.addWidget(QtWidgets.QLabel("       "))
        # self.page1_input_box.addStretch(1)

    def page1_show(self):
        self.page1_show_pic = QtGui.QPixmap('./pic/Cynosure.png').scaled(self.size_.width()*0.7, self.size_.width()*0.7)
        self.page1_show_pic_lb = QtWidgets.QLabel(self)
        self.page1_show_pic_lb.setPixmap(self.page1_show_pic)
        self.page1_show_pic_lb.setToolTip("快扫一下吧")
        
        self.page1_show_make_bt = QtWidgets.QPushButton("生成二维码", self)
        self.page1_show_make_bt.setFont(QtGui.QFont("黑体", 20))
        self.page1_show_make_bt.clicked.connect(self.maker1)
        self.page1_show_make_bt.setToolTip("摁一下")
        

        self.page1_show_hbox1 = QtWidgets.QHBoxLayout()
        self.page1_show_hbox1.addStretch(1)
        self.page1_show_hbox1.addWidget(self.page1_show_pic_lb)
        self.page1_show_hbox1.addStretch(1)

        self.page1_show_hbox2 = QtWidgets.QHBoxLayout()
        self.page1_show_hbox2.addStretch(1)
        self.page1_show_hbox2.addWidget(self.page1_show_make_bt)
        self.page1_show_hbox2.addStretch(1)

        self.page1_show_box = QtWidgets.QVBoxLayout()
        self.page1_show_box.addLayout(self.page1_show_hbox1)
        self.page1_show_box.addStretch(1)
        self.page1_show_box.addLayout(self.page1_show_hbox2)

    def page1_toolbt(self):
        self.page1_toolbt_change_bt = QtWidgets.QPushButton("特别模式", self)
        self.page1_toolbt_change_bt.setStatusTip("敬请期待")
        self.page1_toolbt_change_bt.setToolTip("还没做好")
        # self.page1_toolbt_change_bt.clicked.connect(self.change_to_page2)

        self.page1_toolbt_help_bt = QtWidgets.QPushButton("显示帮助", self)
        self.page1_toolbt_help_bt.setStatusTip("敬请期待")
        self.page1_toolbt_help_bt.setToolTip("还没做好")
        # self.page1_toolbt_help_bt.clicked.connect(self.show_help)

        self.page1_toolbt_box = QtWidgets.QHBoxLayout()
        self.page1_toolbt_box.addStretch(1)
        self.page1_toolbt_box.addWidget(self.page1_toolbt_change_bt)
        self.page1_toolbt_box.addWidget(self.page1_toolbt_help_bt)

    def maker1(self):
        self.url = self.page1_input_text.text()
        img = qrcode.make(self.url)
        img.save("01.png")
        self.page1_show_pic = QtGui.QPixmap('./01.png').scaled(self.size_.width()*0.7, self.size_.width()*0.7)
        self.page1_show_pic_lb.setPixmap(self.page1_show_pic)


    def setsize1(self):
        self.screen = QtWidgets.QDesktopWidget().screenGeometry()
        self.setGeometry(self.screen.width()*0.5 - self.screen.height()*0.24, self.screen.height()*0.14, self.screen.height()*0.48 , self.screen.height()*0.72)
        self.size_= self.geometry()

    def make_action(self):
        self.ac_exit = QtWidgets.QAction(QtGui.QIcon('./icon/icon.ico'), "退出", self)
        self.ac_exit.setShortcut("Ctrl+Q")
        self.ac_exit.setStatusTip("退出程序")
        self.ac_exit.triggered.connect(QtWidgets.qApp.quit)

        # self.ac_open_file = QtWidgets.QAction(QtGui.QIcon("./icon/icon.ico"), "打开文件", self)
        # self.ac_open_file.setShortcut("Ctrl+O")
        # self.ac_open_file.setStatusTip("打开指定文件")
        # self.ac_open_file.triggered.connect(self.open)

        self.ac_makeqr1 = QtWidgets.QAction(QtGui.QIcon('./icon/icon.ico'), "生成二维码", self)
        self.ac_makeqr1.setShortcut("Ctrl+M")
        self.ac_makeqr1.setStatusTip("生成二维码")
        self.ac_makeqr1.triggered.connect(self.maker1)

    def make_Menu(self):
        
        self.menubar = self.menuBar()
        self.menu_file = self.menubar.addMenu("文件")
        # file_.addAction(open_file)
        self.menu_file.addAction(self.ac_makeqr1)
        self.menu_file.addAction(self.ac_exit)


    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, '退出', '你要离开我了吗 QAQ', QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()








if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    CY = make_QRcode()
    CY.show()
    sys.exit(app.exec_())