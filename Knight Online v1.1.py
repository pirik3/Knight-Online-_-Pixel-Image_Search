
from PIL.ImageOps import grayscale
from numpy import uintp
import pyautogui as ag
import win32gui as wn
import pytesseract as pt
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLCDNumber

#========================================#

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\python_proj\ko.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
hwnd = wn.FindWindow(None, "Knight OnLine Client")  # pencere ismi
xy = left, top, right, bottom = wn.GetWindowRect(hwnd)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(796, 399)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\python_proj\\../Downloads/oh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 451, 291))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMaximumSize(QtCore.QSize(571, 301))
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.groupBox = QtWidgets.QGroupBox(self.tab_1)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 451, 81))
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(10, 40, 187, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.widget)
        self.lcdNumber_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lcdNumber_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lcdNumber_3.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_3.setProperty("intValue", 1000)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.horizontalLayout.addWidget(self.lcdNumber_3)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.widget)
        self.lcdNumber_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lcdNumber_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lcdNumber_4.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_4.setProperty("intValue", 1000)
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.horizontalLayout.addWidget(self.lcdNumber_4)
        self.widget1 = QtWidgets.QWidget(self.groupBox)
        self.widget1.setGeometry(QtCore.QRect(11, 11, 186, 25))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lcdNumber = QtWidgets.QLCDNumber(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.lcdNumber.setAutoFillBackground(True)
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lcdNumber.setLineWidth(1)
        self.lcdNumber.setMidLineWidth(0)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setProperty("intValue", 1000)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout_2.addWidget(self.lcdNumber)
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.widget1)
        self.lcdNumber_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lcdNumber_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lcdNumber_2.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_2.setProperty("intValue", 1000)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.horizontalLayout_2.addWidget(self.lcdNumber_2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:\\python_proj\\pictures/oh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_1, icon1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, icon1, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, icon1, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget.addTab(self.tab_5, icon1, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, icon1, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tabWidget.addTab(self.tab_6, icon1, "")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 300, 301, 21))
        self.graphicsView.setMinimumSize(QtCore.QSize(301, 21))
        self.graphicsView.setMaximumSize(QtCore.QSize(16777215, 16))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(0, 330, 301, 21))
        self.graphicsView_2.setMinimumSize(QtCore.QSize(301, 21))
        self.graphicsView_2.setMaximumSize(QtCore.QSize(301, 21))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 300, 131, 51))
        self.pushButton.setObjectName("pushButton")
        self.dockWidget_3 = QtWidgets.QDockWidget(self.centralwidget)
        self.dockWidget_3.setGeometry(QtCore.QRect(460, 0, 331, 358))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_3.sizePolicy().hasHeightForWidth())
        self.dockWidget_3.setSizePolicy(sizePolicy)
        self.dockWidget_3.setAutoFillBackground(True)
        self.dockWidget_3.setFeatures(QtWidgets.QDockWidget.NoDockWidgetFeatures)
        self.dockWidget_3.setObjectName("dockWidget_3")
        self.dockWidgetContents_6 = QtWidgets.QWidget()
        self.dockWidgetContents_6.setObjectName("dockWidgetContents_6")
        self.listWidget = QtWidgets.QListWidget(self.dockWidgetContents_6)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 331, 331))
        self.listWidget.setObjectName("listWidget")
        self.dockWidget_3.setWidget(self.dockWidgetContents_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 796, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KO Helper"))
        self.tabWidget.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.groupBox.setTitle(_translate("MainWindow", "HP / MP"))
        self.label_3.setText(_translate("MainWindow", "MP ->"))
        self.label_4.setText(_translate("MainWindow", "of"))
        self.label.setText(_translate("MainWindow", "HP ->"))
        self.label_2.setText(_translate("MainWindow", "of"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Genel"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "General to all kind other settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Attack"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Attack to mob select settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Archer"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Archer / Asas setting"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Mage"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Mage settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Priest"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Priest settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Warrior"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Warrior settings"))
        self.pushButton.setToolTip(_translate("MainWindow", "OnlineHile.com _ pirik3 _"))
        self.pushButton.setText(_translate("MainWindow", "Durdur/Baslat \n"
" Stop/Start"))
        self.dockWidget_3.setWindowTitle(_translate("MainWindow", "Logs"))


        self.pushButton.clicked.connect(self.Genel_HPread2)

    def Genel_HPread2(self):
        wn.SetForegroundWindow(hwnd)
        ag.sleep(2)
        im_hp = ag.screenshot(region=(left+88, top+62, 35, 11)) # burasi weight ve hight olarak alinacak, point(dimension) olarak degil.
        im_hp.save("D:/python_proj/pictures/hpchangable.png")
        hpread = print(("HP = ", pt.image_to_string(im_hp)))
        self.lcdNumber.display(str(hpread))
        #wn.MessageBox(0, str(hpread), str(hpread),1) 

#=============#

#region -> Genel Fonksiyonlar
    def Genel_PencereKoordinatAL():
        hwnd = wn.FindWindow(None, "Knight OnLine Client")  # pencere ismi
        xy = left, top, right, bottom = wn.GetWindowRect(hwnd)

    def Genel_PetFeed():
        pass
    def Genel_HPpot():
        pass
    def Genel_HPread(self):
        wn.SetForegroundWindow(hwnd)
        ag.sleep(2)
        im_hp = ag.screenshot(region=(left+90, top+62, 35, 11)) # burasi weight ve hight olarak alinacak, point(dimension) olarak degil.
        im_hp.save("D:/python_proj/pictures/hpchangable.png")
        hpread = print(("HP = ", pt.image_to_string(im_hp, config='digits')))
        #hpread2 = print(str(hpread[:-2]))
        #self.lcdNumber.display(str(hpread))  
    def Genel_MPpot():
        pass
    def Genel_MPread(self):
        wn.SetForegroundWindow(hwnd)
        ag.sleep(2)
        im_mp = ag.screenshot(region=(left+93, top+79, 30, 10)) # burasi weight ve hight olarak alinacak, point(dimension) olarak degil.
        im_mp.save("D:/python_proj/pictures/mpchangable.png")
        hpread = print(("MP = ", pt.image_to_string(im_mp)))
    def Genel_Repair():
        pass
    def Genel_TSscroll():
        pass
    def Genel_PartyOut():
        pass
    def Genel_CoordinateChanged(self):
        wn.SetForegroundWindow(hwnd)
        ag.sleep(2)
        im_coor = ag.screenshot(region=(left+106, top+102, 50, 12)) # burasi weight ve hight olarak alinacak, point(dimension) olarak degil.
        im_coor.save("D:/python_proj/pictures/im_coor_changed.png")
        hpread = print(("coor = ", pt.image_to_string(im_coor)))
    def Genel_GetCoordinates():
        pass
    def Genel_GetCharNick():
        pass
    def Genel_Event_JR():
        pass
    def Genel_Event_FT():
        pass
    def Genel_Event_BDW():
        pass
#endregion -> Genel Fonksiyonlar

#region -> Archer/Rogue Fonksiyonlari

def Archer_Wolf():
    pass
def Archer_LightFeet():
    pass
def Archer_AC():
    pass
def Archer_CureAL():
    pass

#endregion -> Archer/Rogue Fonksiyonlari

#region -> Priest Fonksiyonlari

def PriestKitap():
    pass
def Priest_Buff_Undy():
    pass
def Priest_AC_300():
    pass
def Priest_str15():
    pass
def Priest_str30():
    pass
def Priest_CureAL():
    pass
def Priest_Heal_1920():
    pass
def Priest_GroupHeal():
    pass
def Priest_Fresh():
    pass

#endregion -> Priest Fonksiyonlari
Ui_MainWindow().Genel_MPread()
Ui_MainWindow().Genel_HPread()
Ui_MainWindow().Genel_CoordinateChanged()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



while True:

    pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


    hwnd = wn.FindWindow(None, "Knight OnLine Client")  # pencere ismi
    xy = left, top, right, bottom = wn.GetWindowRect(hwnd)

    example1 = ag.locateCenterOnScreen('D:/python_proj/pictures/Forst_bite.png', region = xy, confidence=0.9)
    #asd2 = ag.locateOnWindow('C:/Users/volkan/Pictures/8.png', "Untitled - Notepad")

    im_hp = ag.screenshot(region=(left+29, top+60, 192, 15)) # burasi weight ve hight olarak alinacak, point(dimension) olarak degil.
    im_hp.save("D:/python_proj/pictures/hp.png") # saves the screenshot in a file

    im_mp = ag.screenshot(region=(left+29, top+77, 192, 14))
    im_mp.save("D:/python_proj/pictures/mp.png") # saves the screenshot in a file

    
    if not hwnd:
        print("window not found")
    else:
        if example1 == None:
            pass
            #ag.sleep(0.1)
            #print(xy)
            print("not found")
        else:
            #ag.sleep(0.01)
            #print(xy)
            #print(example1, "found")
            #print(asd2, "asd2")
            #print("HP = ", pt.image_to_string(im_hp), "\r")
            #print("MP = ", pt.image_to_string(im_mp))
            #example1x, example1y = example1
            #ag.mouseDown(example1)
            #ag.sleep(0.01)
            #ag.mouseUp()
            #ag.sleep(2)
            continue
        


