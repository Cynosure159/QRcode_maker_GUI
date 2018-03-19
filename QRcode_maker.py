# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import qrcode
import shutil
import ctypes  
from MyQR import myqr
import os




ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")  # 解决任务栏图标问题

class make_QRcode(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.initui()
        qss_file = open('style.qss').read()
        self.setStyleSheet(qss_file)

    def initui(self):
        self.setsize1()
        self.setWindowIcon(QtGui.QIcon('./icon/icon.ico'))
        self.setWindowTitle("二维码生成器")
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setToolTip("这是一个生成二维码的软件")
        self.statusBar().showMessage("欢迎使用本软件")
        # self.palette = QtGui.QPalette()
        # self.palette.setBrush(QtGui.QPalette.Background, QtGui.QColor(203, 255, 252))
        # self.setPalette(self.palette)

        self.make_action()
        self.make_Menu()

        self.make_page1()

        self.setCentralWidget(self.page1_main_ground)


    def make_page1(self):
        self.pic1_ad = "./pic/Cynosure.png"

        self.page1_logo()
        self.page1_input()
        self.page1_show()
        self.page1_toolbt()

        self.page1_box = QtWidgets.QVBoxLayout()
        self.page1_box.addStretch(2)
        self.page1_box.addLayout(self.page1_logo_box)
        self.page1_box.addStretch(2)
        self.page1_box.addLayout(self.page1_input_box)
        self.page1_box.addStretch(1)
        self.page1_box.addLayout(self.page1_show_box)
        self.page1_box.addStretch(2)
        self.page1_box.addLayout(self.page1_toolbt_box)
        # self.page1_box.addStretch(1)

        self.page1_main_ground = QtWidgets.QWidget()
        self.page1_main_ground.setLayout(self.page1_box)


    def page1_logo(self):
        self.page1_logo_lb = QtWidgets.QLabel("二维码生成器")
        self.page1_logo_lb.setFont(QtGui.QFont("黑体", self.size_.width()*0.05))

        self.page1_logo_box = QtWidgets.QHBoxLayout()
        self.page1_logo_box.addStretch(1)
        self.page1_logo_box.addWidget(self.page1_logo_lb)
        self.page1_logo_box.addStretch(1)

    def page1_input(self):
        self.page1_input_words = QtWidgets.QLabel(r"网址/内容")
        self.page1_input_words.setFont(QtGui.QFont("黑体", 13))

        self.page1_input_text = QtWidgets.QLineEdit()
        self.page1_input_text.textChanged.connect(self.maker1)

        self.page1_input_box = QtWidgets.QHBoxLayout()
        # self.page1_input_box.addStretch(1)
        self.page1_input_box.addWidget(QtWidgets.QLabel("     "))
        self.page1_input_box.addWidget(self.page1_input_words)
        self.page1_input_box.addWidget(self.page1_input_text)
        self.page1_input_box.addWidget(QtWidgets.QLabel("       "))
        # self.page1_input_box.addStretch(1)

    def page1_show(self):
        self.page1_show_pic = QtGui.QPixmap(self.pic1_ad).scaled(self.size_.width()*0.7, self.size_.width()*0.7)
        self.page1_show_pic_lb = QtWidgets.QLabel(self)
        self.page1_show_pic_lb.setPixmap(self.page1_show_pic)
        self.page1_show_pic_lb.setToolTip("快扫一下吧")
        
        # self.page1_show_make_bt = QtWidgets.QPushButton("生成二维码", self)
        # self.page1_show_make_bt.setFont(QtGui.QFont("黑体", 20))
        # self.page1_show_make_bt.clicked.connect(self.maker1)
        # self.page1_show_make_bt.setToolTip("摁一下")

        self.page1_show_save_bt = QtWidgets.QPushButton("保存二维码", self)
        self.page1_show_save_bt.setObjectName("page1_show_save_bt")
        self.page1_show_save_bt.setFont(QtGui.QFont("黑体", 20))
        self.page1_show_save_bt.clicked.connect(self.save1)
        self.page1_show_save_bt.setToolTip("保存至本地")

        

        self.page1_show_hbox1 = QtWidgets.QHBoxLayout()
        self.page1_show_hbox1.addStretch(1)
        self.page1_show_hbox1.addWidget(self.page1_show_pic_lb)
        self.page1_show_hbox1.addStretch(1)

        self.page1_show_hbox2 = QtWidgets.QHBoxLayout()
        self.page1_show_hbox2.addStretch(1)
        # self.page1_show_hbox2.addWidget(self.page1_show_make_bt)
        self.page1_show_hbox2.addWidget(self.page1_show_save_bt)
        self.page1_show_hbox2.addStretch(1)

        self.page1_show_box = QtWidgets.QVBoxLayout()
        self.page1_show_box.addLayout(self.page1_show_hbox1)
        self.page1_show_box.addStretch(1)
        self.page1_show_box.addLayout(self.page1_show_hbox2)

    def page1_toolbt(self):
        self.page1_toolbt_change_bt = QtWidgets.QPushButton("特别模式", self)
        self.page1_toolbt_change_bt.setStatusTip("转到特别模式")
        self.page1_toolbt_change_bt.setToolTip("转到特别模式")
        self.page1_toolbt_change_bt.clicked.connect(self.change_to_page2)

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
        self.pic1_ad = "./pic/01.png"
        img.save(self.pic1_ad)
        self.page1_show_pic = QtGui.QPixmap(self.pic1_ad).scaled(self.size_.width()*0.7, self.size_.width()*0.7)
        self.page1_show_pic_lb.setPixmap(self.page1_show_pic)

    def save1(self):
        self.filename1 , self.ok1 = QtWidgets.QFileDialog.getSaveFileName(self, "保存二维码", "C:/", "图片 (*.png)")
        if self.ok1:
            shutil.copy(self.pic1_ad, self.filename1)


    def setsize1(self):
        self.screen = QtWidgets.QDesktopWidget().screenGeometry()
        self.setGeometry(self.screen.width()*0.5 - self.screen.height()*0.24, self.screen.height()*0.14, self.screen.height()*0.48 , self.screen.height()*0.72)
        self.size_= self.geometry()

    def change_to_page1(self):
        
        self.setsize1()
        self.make_page1()
        self.setCentralWidget(self.page1_main_ground)

    def change_to_page2(self):
        self.setsize2()
        self.make_page2()
        self.setCentralWidget(self.page2_main_ground)
        

    def make_page2(self):
        self.pic2_ad = "./pic/Cynosure.png"
        self.pic2_ad_ = "./pic/Cynosure_.jpg"

        self.page2_logo()
        self.page2_input()
        self.page2_show()
        self.page2_toolbt()
        
        self.page2_box = QtWidgets.QVBoxLayout()
        self.page2_box.addStretch(2)
        self.page2_box.addLayout(self.page2_logo_box)
        self.page2_box.addStretch(2)
        self.page2_box.addLayout(self.page2_input_box)
        self.page2_box.addStretch(1)
        self.page2_box.addLayout(self.page2_show_box)
        self.page2_box.addStretch(2)
        self.page2_box.addLayout(self.page2_toolbt_box)
        # self.page1_box.addStretch(1)

        self.page2_main_ground = QtWidgets.QWidget()
        self.page2_main_ground.setLayout(self.page2_box)


    def page2_logo(self):
        self.page2_logo_lb = QtWidgets.QLabel("特别二维码生成器")
        self.page2_logo_lb.setFont(QtGui.QFont("黑体", self.size_.width()*0.05))

        self.page2_logo_box = QtWidgets.QHBoxLayout()
        self.page2_logo_box.addStretch(1)
        self.page2_logo_box.addWidget(self.page2_logo_lb)
        self.page2_logo_box.addStretch(1)

    def page2_input(self):
        self.page2_input_words = QtWidgets.QLabel(r"网址/内容(不支持中文)")
        self.page2_input_words.setFont(QtGui.QFont("黑体", 13))

        self.page2_input_text = QtWidgets.QLineEdit()
        self.page2_input_text.textChanged.connect(self.maker2)

        self.page2_input_box = QtWidgets.QHBoxLayout()
        # self.page1_input_box.addStretch(1)
        self.page2_input_box.addWidget(QtWidgets.QLabel("     "))
        self.page2_input_box.addWidget(self.page2_input_words)
        self.page2_input_box.addWidget(self.page2_input_text)
        self.page2_input_box.addWidget(QtWidgets.QLabel("       "))
        # self.page1_input_box.addStretch(1)

    def page2_show(self):
        self.page2_from_pic = QtGui.QPixmap(self.pic2_ad_).scaled(self.size_.width()*0.4, self.size_.width()*0.4)
        self.page2_from_pic_lb = QtWidgets.QLabel(self)
        self.page2_from_pic_lb.setPixmap(self.page2_from_pic)
        self.page2_from_pic_lb.setToolTip("你要合成的图片")

        self.page2_show_pic = QtGui.QPixmap(self.pic2_ad).scaled(self.size_.width()*0.4, self.size_.width()*0.4)
        self.page2_show_pic_lb = QtWidgets.QLabel(self)
        self.page2_show_pic_lb.setPixmap(self.page2_show_pic)
        self.page2_show_pic_lb.setToolTip("快扫一下吧")


        self.page2_show_save_bt = QtWidgets.QPushButton("保存二维码", self)
        self.page2_show_save_bt.setFont(QtGui.QFont("黑体", 20))
        self.page2_show_save_bt.clicked.connect(self.save2)
        self.page2_show_save_bt.setToolTip("保存至本地")
        self.page2_show_save_bt.setObjectName("page2_show_save_bt")

        self.page2_show_from_bt = QtWidgets.QPushButton("选择原图片", self)
        self.page2_show_from_bt.setFont(QtGui.QFont("黑体", 20))
        self.page2_show_from_bt.clicked.connect(self.open2)
        self.page2_show_from_bt.setToolTip("选择你要合成的图片")
        self.page2_show_from_bt.setObjectName("page2_show_from_bt")

        

        self.page2_show_hbox1 = QtWidgets.QHBoxLayout()
        self.page2_show_hbox1.addStretch(1)
        self.page2_show_hbox1.addWidget(self.page2_from_pic_lb)
        self.page2_show_hbox1.addWidget(QtWidgets.QLabel("   "))
        self.page2_show_hbox1.addWidget(self.page2_show_pic_lb)
        self.page2_show_hbox1.addStretch(1)

        self.page2_show_hbox2 = QtWidgets.QHBoxLayout()
        self.page2_show_hbox2.addStretch(1)
        self.page2_show_hbox2.addWidget(self.page2_show_from_bt)
        self.page2_show_hbox2.addWidget(QtWidgets.QLabel("                                     "))
        self.page2_show_hbox2.addWidget(self.page2_show_save_bt)
        self.page2_show_hbox2.addStretch(1)

        self.page2_show_box = QtWidgets.QVBoxLayout()
        self.page2_show_box.addLayout(self.page2_show_hbox1)
        self.page2_show_box.addStretch(1)
        self.page2_show_box.addLayout(self.page2_show_hbox2)

    def open2(self):
        self.pic2_ad_ , self.ok2_ = QtWidgets.QFileDialog.getOpenFileName(self, "打开图片", "C:/", "图片 (*.jpg)")
        if self.ok2_ :
            self.maker2()
            self.page2_from_pic = QtGui.QPixmap(self.pic2_ad_).scaled(self.size_.width()*0.40, self.size_.width()*0.40)
            self.page2_from_pic_lb.setPixmap(self.page2_from_pic)

        

    def save2(self):
        self.filename2 , self.ok2 = QtWidgets.QFileDialog.getSaveFileName(self, "保存二维码", "C:/", "图片 (*.png)")
        if self.ok2:
            shutil.copy(self.pic2_ad, self.filename2)

    def maker2(self):
        self.url_ = self.page2_input_text.text()
        version, level, qr_name = myqr.run(
	        self.url_,
            version=1,
            level='H',
            picture=self.pic2_ad_,
            colorized=True,
            contrast=1.0,
            brightness=1.0,
            save_name="./pic/02.png",
            save_dir=os.getcwd()
        )

        self.pic2_ad = "./pic/02.png"
        self.page2_show_pic = QtGui.QPixmap(self.pic2_ad).scaled(self.size_.width()*0.40, self.size_.width()*0.40)
        self.page2_show_pic_lb.setPixmap(self.page2_show_pic)

    def page2_toolbt(self):
        self.page2_toolbt_change_bt = QtWidgets.QPushButton("普通模式", self)
        self.page2_toolbt_change_bt.setStatusTip("转到普通模式")
        self.page2_toolbt_change_bt.setToolTip("转到普通模式")
        self.page2_toolbt_change_bt.clicked.connect(self.change_to_page1)

        self.page2_toolbt_help_bt = QtWidgets.QPushButton("显示帮助", self)
        self.page2_toolbt_help_bt.setStatusTip("敬请期待")
        self.page2_toolbt_help_bt.setToolTip("还没做好")
        # self.page1_toolbt_help_bt.clicked.connect(self.show_help)

        self.page2_toolbt_box = QtWidgets.QHBoxLayout()
        self.page2_toolbt_box.addStretch(1)
        self.page2_toolbt_box.addWidget(self.page2_toolbt_change_bt)
        self.page2_toolbt_box.addWidget(self.page2_toolbt_help_bt)


    def setsize2(self):
        self.screen = QtWidgets.QDesktopWidget().screenGeometry()
        self.setGeometry(self.screen.width()*0.5 - self.screen.height()*0.30, self.screen.height()*0.14, self.screen.height()*0.60, self.screen.height()*0.72)
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

        self.ac_to_1 = QtWidgets.QAction(QtGui.QIcon('./icon/icon.ico'), "普通模式", self)
        self.ac_to_1.setShortcut("Ctrl+1")
        self.ac_to_1.setStatusTip("普通模式")
        self.ac_to_1.triggered.connect(self.change_to_page1)

        self.ac_to_2 = QtWidgets.QAction(QtGui.QIcon('./icon/icon.ico'), "特别模式", self)
        self.ac_to_2.setShortcut("Ctrl+2")
        self.ac_to_2.setStatusTip("普通模式")
        self.ac_to_2.triggered.connect(self.change_to_page2)

    def make_Menu(self):
        
        self.menubar = self.menuBar()
        self.menu_file = self.menubar.addMenu("文件")
        # file_.addAction(open_file)
        self.menu_file.addAction(self.ac_makeqr1)
        self.menu_file.addAction(self.ac_to_1)
        self.menu_file.addAction(self.ac_to_2)
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