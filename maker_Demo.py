# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import qrcode

class make_QRcode(QtWidgets.QMainWindow):
    
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self,parent)
        self.setsize()
        self.size_= self.geometry()
        self.setWindowIcon(QtGui.QIcon('./icon/icon.ico'))
        self.setWindowTitle("二维码生成器")
        #self.setWindowFlags(Qt.FramelessWindowHint)
        self.setToolTip("...")
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Background, QtGui.QColor(244, 230, 186))
        self.setPalette(palette)
        
        

        exit_ = QtWidgets.QAction(QtGui.QIcon('./icon/icon.ico'), "退出", self)
        exit_.setShortcut("Ctrl+Q")
        exit_.setStatusTip("退出程序")
        exit_.triggered.connect(QtWidgets.qApp.quit)

        # open_file = QtWidgets.QAction(QtGui.QIcon("./icon/icon.ico"), "打开文件", self)
        # open_file.setShortcut("Ctrl+O")
        # open_file.setStatusTip("打开指定文件")
        # open_file.triggered.connect(self.open)

        self.url_input = QtWidgets.QLineEdit()
        

        menubar = self.menuBar()
        file_ = menubar.addMenu("文件")
        # file_.addAction(open_file)
        file_.addAction(exit_)

        main_ground = QtWidgets.QWidget()
        self.setCentralWidget(main_ground)

        self.createbox1()
        self.createbox2()
        
        main_gird = QtWidgets.QGridLayout()
        main_gird.addWidget(self.box1, 0, 0)
        main_gird.addWidget(self.box2, 0, 2)
        
        main_ground.setLayout(main_gird)
        
        


    # def open(self):
    #     file_name = QtWidgets.QFileDialog.getOpenFileName(self, '打开文件', "./")
    #     print(file_name[0])
    #     pic = QtGui.QPixmap(file_name[0]).scaled(300,300)
    #     print(pic)
    #     self.lb1.setPixmap(pic)


    def maker(self):
        url = self.url_input.text()
        # print(url)
        img = qrcode.make(url)
        img.save("01.png")
        pic = QtGui.QPixmap("./01.png").scaled(300,300)
        self.lb1.setPixmap(pic)
    
    
    def setsize(self):
        self.screen = QtWidgets.QDesktopWidget().screenGeometry()
        self.setGeometry(self.screen.width()/4, self.screen.height()/4, self.screen.width()/2, self.screen.height()/2)

    def createbox1(self):

        self.make_bt = QtWidgets.QPushButton("生成二维码", self)
        self.make_bt.clicked.connect(self.maker)

        self.box1 = QtWidgets.QGroupBox()
        gird = QtWidgets.QGridLayout()
        gird.addWidget(QtWidgets.QLabel("网址：") , 0, 0)
        gird.addWidget(self.url_input, 0, 1)
        gird.addWidget(self.make_bt, 0, 2)

        self.box1.setLayout(gird)

    def createbox2(self):
        superman = QtGui.QPixmap('./pic/图层 1.png').scaled(300,300)
        self.lb1 = QtWidgets.QLabel(self)
        self.lb1.setPixmap(superman)
        

        lb2 = QtWidgets.QLabel("生成图片：")
        lb2.setFont(QtGui.QFont("黑体", 30))

        self.box2 = QtWidgets.QGroupBox()
        hbox = QtWidgets.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.lb1)
        hbox.addStretch(1)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(lb2)
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.box2.setLayout(vbox)
















if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    CY = make_QRcode()
    CY.show()
    sys.exit(app.exec_())