# -*- coding: utf-8 -*-

__title__ = "Kurdish Characters Convertor"
__version__ = "1.0.0"
__build__ = __version__
__author__ = "Azhy Slemany"

aboutText = """
<h3 style="text-align: center;margin:12px">Kurdish Character Convertor</h3>
<p>&nbsp;</p>
<p style="margin:6px">This is a simple program for converting text for/to kurdish with some features which introduced <a href="https://github.com/dolanskurd/kurdish">here</a> created by <a href="https://twitter.com/dolanskurd">Dolan H&ecirc;riş</a>&nbsp;using python language, and GUI created by <a href="https://www.facebook.com/azhy.sulemany">Azhy Slemany</a>&nbsp;using python language with PyQt framework, and we hope you benefit it.</p>
<p style="text-align: right;">&nbsp;</p>
<p style="text-align: right;font-family:NRT Reg;margin:6px">ئەم بەرنامەیە تایبەتە بە گۆڕینی تێکست لە\بۆ کوردی لەگەڵ هەندێ جێبەجێکردنی تر کە <a href="https://github.com/dolanskurd/kurdish">لێرەدا</a> ڕوونکراوەتەوە وە دروستکراوە لەلایەن&nbsp; <a href="https://twitter.com/dolanskurd">دۆلان هێرش</a>ەوە بە بەکارهێنانی زمانی پایثن، وە ڕووکارەکەی دروستکراوە لەلایەن <a href="https://www.facebook.com/azhy.sulemany">ئەژی سلێمانی</a>ەوە بە بەکارهێنانی زمانی&nbsp; پایثن لەگەڵ فرەیموۆرکی پایکیوتی، وە هیوادارین سودی هەبێت</p>
<p style="text-align: right;">&nbsp;</p>
<p style="text-align: center;"><a href="https://github.com/dolanskurd/kurdish">https://github.com/dolanskurd/kurdish</a>&nbsp;- Source</p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: right; font-size: 8px;margin:6px">10/4/2020 written by Azhy Slemany, All Rights Reserved</p>
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QDialog
import subprocess, sys, os
from kurdish import ku
from unicodedata import name
import json

def get_resource(path):
	return 'res/' + path

fontfileName = 'NRT-Reg.ttf'
fontName = 'NRT Reg'
inputFontSize, outputFontSize = 18, 22

#Global Methods
def readFile(filePath):
    file = open(filePath, 'r')
    r = file.read()
    file.close()
    return r
    
def writeFile(filePath, data):
    file = open(filePath, 'w+')
    file.write(data)
    file.flush()
    file.close()

def settings():
	return QtCore.QSettings('azhy.org', 'Kurdish Character Convertor')

def getLanguage():
    return settings().value('language', 'e')

def setLanguage(lang):
    settings().setValue('language', lang)

def getWrapMode():
	mode = settings().value('wrapMode', 'noWrap')
	if mode == 'wrap':
		return QtWidgets.QTextEdit.WidgetWidth
	else:
		return QtWidgets.QTextEdit.NoWrap

def setWrapMode(mode):
	settings().setValue('wrapMode', mode)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(884, 655)
        MainWindow.setMinimumSize(QtCore.QSize(884, 655))
        MainWindow.setMaximumSize(QtCore.QSize(884, 655))

        # Load the font: 
        font_db = QtGui.QFontDatabase()
        font_id = font_db.addApplicationFont(get_resource(fontfileName))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 861, 471))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.c_b_tab1 = QtWidgets.QPushButton(self.tab)
        self.c_b_tab1.setGeometry(QtCore.QRect(200, 380, 201, 41))
        self.c_b_tab1.setObjectName("c_b_tab1")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(19, 10, 821, 211))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.cktol = QtWidgets.QRadioButton(self.groupBox_3)
        self.cktol.setGeometry(QtCore.QRect(20, 20, 351, 20))
        self.cktol.setChecked(True)
        self.cktol.setObjectName("cktol")
        self.caktok = QtWidgets.QRadioButton(self.groupBox_3)
        self.caktok.setGeometry(QtCore.QRect(20, 70, 351, 20))
        self.caktok.setObjectName("caktok")
        self.catok = QtWidgets.QRadioButton(self.groupBox_3)
        self.catok.setGeometry(QtCore.QRect(440, 20, 351, 20))
        self.catok.setObjectName("catok")
        self.cetok = QtWidgets.QRadioButton(self.groupBox_3)
        self.cetok.setGeometry(QtCore.QRect(20, 120, 591, 20))
        self.cetok.setObjectName("cetok")
        self.cktoe = QtWidgets.QRadioButton(self.groupBox_3)
        self.cktoe.setGeometry(QtCore.QRect(20, 170, 591, 20))
        self.cktoe.setObjectName("cktoe")
        self.s_b_tab1 = QtWidgets.QPushButton(self.tab)
        self.s_b_tab1.setGeometry(QtCore.QRect(460, 380, 191, 41))
        self.s_b_tab1.setObjectName("s_b_tab1")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_6.setGeometry(QtCore.QRect(20, 220, 821, 141))
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.ti_tab1 = QtWidgets.QRadioButton(self.groupBox_6)
        self.ti_tab1.setGeometry(QtCore.QRect(250, 10, 100, 20))
        self.ti_tab1.setChecked(True)
        self.ti_tab1.setObjectName("ti_tab1")
        self.paste_tab1 = QtWidgets.QPushButton(self.groupBox_6)
        self.paste_tab1.setGeometry(QtCore.QRect(520, 50, 31, 31))
        self.paste_tab1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(get_resource("paste.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.paste_tab1.setIcon(icon)
        self.paste_tab1.setObjectName("paste_tab1")
        self.te_tab1 = QtWidgets.QTextEdit(self.groupBox_6)
        self.te_tab1.setGeometry(QtCore.QRect(90, 40, 411, 91))
        self.te_tab1.setObjectName("te_tab1")
        self.te_tab1.setFont(QtGui.QFont(fontName, inputFontSize))
        self.label_6 = QtWidgets.QLabel(self.groupBox_6)
        self.label_6.setGeometry(QtCore.QRect(10, 40, 81, 91))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.file_t_tab1 = QtWidgets.QLineEdit(self.groupBox_6)
        self.file_t_tab1.setGeometry(QtCore.QRect(610, 100, 191, 21))
        self.file_t_tab1.setReadOnly(True)
        self.file_t_tab1.setObjectName("file_t_tab1")
        self.fi_tab1 = QtWidgets.QRadioButton(self.groupBox_6)
        self.fi_tab1.setGeometry(QtCore.QRect(660, 10, 100, 20))
        self.fi_tab1.setObjectName("fi_tab1")
        self.file_b_tab1 = QtWidgets.QPushButton(self.groupBox_6)
        self.file_b_tab1.setGeometry(QtCore.QRect(650, 50, 113, 41))
        self.file_b_tab1.setObjectName("file_b_tab1")
        self.line = QtWidgets.QFrame(self.groupBox_6)
        self.line.setGeometry(QtCore.QRect(559, 0, 41, 141))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_4 = QtWidgets.QFrame(self.groupBox_6)
        self.line_4.setGeometry(QtCore.QRect(-3, -10, 821, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.clear_t = QtWidgets.QToolButton(self.groupBox_6)
        self.clear_t.setGeometry(QtCore.QRect(520, 90, 31, 31))
        self.clear_t.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(get_resource('trash.png')), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear_t.setIcon(icon1)
        self.clear_t.setObjectName("clear_t")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.c_b_tab2 = QtWidgets.QPushButton(self.tab_3)
        self.c_b_tab2.setGeometry(QtCore.QRect(190, 370, 191, 41))
        self.c_b_tab2.setObjectName("c_b_tab2")
        self.s_b_tab2 = QtWidgets.QPushButton(self.tab_3)
        self.s_b_tab2.setGeometry(QtCore.QRect(460, 370, 181, 41))
        self.s_b_tab2.setObjectName("s_b_tab2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_2.setGeometry(QtCore.QRect(19, 19, 821, 181))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.cdetok = QtWidgets.QRadioButton(self.groupBox_2)
        self.cdetok.setGeometry(QtCore.QRect(20, 40, 351, 20))
        self.cdetok.setChecked(True)
        self.cdetok.setObjectName("cdetok")
        self.cdktoe = QtWidgets.QRadioButton(self.groupBox_2)
        self.cdktoe.setGeometry(QtCore.QRect(20, 110, 351, 20))
        self.cdktoe.setObjectName("cdktoe")
        self.cdktop = QtWidgets.QRadioButton(self.groupBox_2)
        self.cdktop.setGeometry(QtCore.QRect(440, 40, 351, 20))
        self.cdktop.setObjectName("cdktop")
        self.cdptok = QtWidgets.QRadioButton(self.groupBox_2)
        self.cdptok.setGeometry(QtCore.QRect(440, 110, 361, 20))
        self.cdptok.setObjectName("cdptok")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 200, 821, 141))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 81, 71))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.te_tab2 = QtWidgets.QTextEdit(self.groupBox_4)
        self.te_tab2.setGeometry(QtCore.QRect(91, 50, 361, 71))
        self.te_tab2.setObjectName("te_tab2")
        self.te_tab2.setFont(QtGui.QFont(fontName, inputFontSize))
        self.file_t_tab2 = QtWidgets.QLineEdit(self.groupBox_4)
        self.file_t_tab2.setGeometry(QtCore.QRect(611, 100, 191, 21))
        self.file_t_tab2.setReadOnly(True)
        self.file_t_tab2.setObjectName("file_t_tab2")
        self.file_b_tab2 = QtWidgets.QPushButton(self.groupBox_4)
        self.file_b_tab2.setGeometry(QtCore.QRect(651, 50, 113, 41))
        self.file_b_tab2.setObjectName("file_b_tab2")
        self.paste_tab2 = QtWidgets.QPushButton(self.groupBox_4)
        self.paste_tab2.setGeometry(QtCore.QRect(490, 50, 31, 31))
        self.paste_tab2.setText("")
        self.paste_tab2.setIcon(icon)
        self.paste_tab2.setObjectName("paste_tab2")
        self.ti_tab2 = QtWidgets.QRadioButton(self.groupBox_4)
        self.ti_tab2.setGeometry(QtCore.QRect(220, 10, 100, 20))
        self.ti_tab2.setChecked(True)
        self.ti_tab2.setObjectName("ti_tab2")
        self.fi_tab2 = QtWidgets.QRadioButton(self.groupBox_4)
        self.fi_tab2.setGeometry(QtCore.QRect(660, 10, 100, 20))
        self.fi_tab2.setObjectName("fi_tab2")
        self.line_2 = QtWidgets.QFrame(self.groupBox_4)
        self.line_2.setGeometry(QtCore.QRect(545, 0, 21, 141))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.groupBox_4)
        self.line_3.setGeometry(QtCore.QRect(-3, -10, 821, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.clear_t_2 = QtWidgets.QToolButton(self.tab_3)
        self.clear_t_2.setGeometry(QtCore.QRect(510, 290, 31, 31))
        self.clear_t_2.setText("")
        self.clear_t_2.setIcon(icon1)
        self.clear_t_2.setObjectName("clear_t_2")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(30, 10, 791, 231))
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.te_tab3 = QtWidgets.QTextEdit(self.groupBox)
        self.te_tab3.setGeometry(QtCore.QRect(90, 90, 251, 41))
        self.te_tab3.setObjectName("te_tab3")
        self.te_tab3.setFont(QtGui.QFont(fontName, inputFontSize))
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(9, 90, 81, 41))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.c_b_tab3 = QtWidgets.QPushButton(self.groupBox)
        self.c_b_tab3.setGeometry(QtCore.QRect(190, 180, 151, 41))
        self.c_b_tab3.setObjectName("c_b_tab3")
        self.s_b_tab3 = QtWidgets.QPushButton(self.groupBox)
        self.s_b_tab3.setGeometry(QtCore.QRect(390, 180, 191, 41))
        self.s_b_tab3.setObjectName("s_b_tab3")
        self.file_b_tab3 = QtWidgets.QPushButton(self.groupBox)
        self.file_b_tab3.setGeometry(QtCore.QRect(550, 70, 113, 41))
        self.file_b_tab3.setObjectName("file_b_tab3")
        self.file_t_tab3 = QtWidgets.QLineEdit(self.groupBox)
        self.file_t_tab3.setGeometry(QtCore.QRect(510, 120, 191, 21))
        self.file_t_tab3.setReadOnly(True)
        self.file_t_tab3.setObjectName("file_t_tab3")
        self.ti_tab3 = QtWidgets.QRadioButton(self.groupBox)
        self.ti_tab3.setGeometry(QtCore.QRect(140, 30, 100, 20))
        self.ti_tab3.setChecked(True)
        self.ti_tab3.setObjectName("ti_tab3")
        self.fi_tab3 = QtWidgets.QRadioButton(self.groupBox)
        self.fi_tab3.setGeometry(QtCore.QRect(560, 30, 100, 20))
        self.fi_tab3.setObjectName("fi_tab3")
        self.line_5 = QtWidgets.QFrame(self.groupBox)
        self.line_5.setGeometry(QtCore.QRect(420, 20, 20, 141))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.groupBox)
        self.line_6.setGeometry(QtCore.QRect(0, 150, 791, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.paste_tab3 = QtWidgets.QPushButton(self.groupBox)
        self.paste_tab3.setGeometry(QtCore.QRect(360, 90, 51, 41))
        self.paste_tab3.setText("")
        self.paste_tab3.setIcon(icon)
        self.paste_tab3.setObjectName("paste_tab3")
        self.gk = QtWidgets.QPushButton(self.tab_2)
        self.gk.setGeometry(QtCore.QRect(50, 280, 311, 41))
        self.gk.setObjectName("gk")
        self.gl = QtWidgets.QPushButton(self.tab_2)
        self.gl.setGeometry(QtCore.QRect(470, 280, 311, 41))
        self.gl.setObjectName("gl")
        self.gv = QtWidgets.QPushButton(self.tab_2)
        self.gv.setGeometry(QtCore.QRect(210, 360, 431, 41))
        self.gv.setObjectName("gv")
        self.tabWidget.addTab(self.tab_2, "")
        self.out = QtWidgets.QTextEdit(self.centralwidget)
        self.out.setGeometry(QtCore.QRect(10, 478, 821, 131))
        self.out.setReadOnly(True)
        self.out.setObjectName("out")
        self.out.setFont(QtGui.QFont(fontName, outputFontSize))
        self.copy = QtWidgets.QToolButton(self.centralwidget)
        self.copy.setGeometry(QtCore.QRect(840, 490, 31, 31))
        self.copy.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(get_resource("sheet.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.copy.setIcon(icon2)
        self.copy.setObjectName("copy")
        self.save = QtWidgets.QToolButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(840, 530, 31, 31))
        self.save.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(get_resource("floppy-disk.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save.setIcon(icon3)
        self.save.setObjectName("save")
        self.clear_out = QtWidgets.QToolButton(self.centralwidget)
        self.clear_out.setGeometry(QtCore.QRect(840, 570, 31, 31))
        self.clear_out.setText("")
        self.clear_out.setIcon(icon1)
        self.clear_out.setObjectName("clear_out")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 884, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuLanguage = QtWidgets.QMenu(self.menuFile)
        self.menuLanguage.setObjectName("menuLanguage")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionEnglish = QtWidgets.QAction(MainWindow)
        self.actionEnglish.setCheckable(True)
        self.actionEnglish.setChecked(True)
        self.actionEnglish.setObjectName("actionEnglish")
        self.actionKurdish = QtWidgets.QAction(MainWindow)
        self.actionKurdish.setCheckable(True)
        self.actionKurdish.setObjectName("actionKurdish")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionTextWrap = QtWidgets.QAction(MainWindow)
        self.actionTextWrap.setObjectName("actionTextWrap")
        self.actionTextWrap.setCheckable(True)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuLanguage.addAction(self.actionEnglish)
        self.menuLanguage.addAction(self.actionKurdish)
        self.menuFile.addAction(self.menuLanguage.menuAction())
        self.menuFile.addAction(self.actionTextWrap)
        self.menuFile.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())

        MainWindow.setWindowTitle("Kurdish Character Convertor")
        if getLanguage() == 'e':
            self.retranslateUi(MainWindow)
        else:
            self.translateUi()
            self.actionKurdish.setChecked(True)
            self.actionEnglish.setChecked(False)

        #our defined method
        self.MainWindow = MainWindow
        self.userDefinedMethod()
        if(getWrapMode() == QtWidgets.QTextEdit.WidgetWidth):
        	self.actionTextWrap.setChecked(True)
        self.setWrapModes()
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.c_b_tab1.setText(_translate("MainWindow", "Convert and print output"))
        self.cktol.setText(_translate("MainWindow", "Convert Arabic-based Kurdish to Latin-based Kurdish"))
        self.caktok.setText(_translate("MainWindow", "Converting Ali-k style to unicode"))
        self.catok.setText(_translate("MainWindow", "Converting Arabic Characters to Kurdish"))
        self.cetok.setText(_translate("MainWindow", "Converting English Characters to Arabic-based Kurdish Based on KRG Unicode System"))
        self.cktoe.setText(_translate("MainWindow", "Converting Arabic-based Kurdish Characters to English Based on KRG Unicode System"))
        self.s_b_tab1.setText(_translate("MainWindow", "Convert and save to file"))
        self.ti_tab1.setText(_translate("MainWindow", "Text input"))
        self.label_6.setText(_translate("MainWindow", "Input :"))
        self.fi_tab1.setText(_translate("MainWindow", "File input"))
        self.file_b_tab1.setText(_translate("MainWindow", "Choose File"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Converting Text"))
        self.c_b_tab2.setText(_translate("MainWindow", "Convert and print output"))
        self.s_b_tab2.setText(_translate("MainWindow", "Convert and save to file"))
        self.cdetok.setText(_translate("MainWindow", "Convert English Digits to Arabic-based Kurdish Digits"))
        self.cdktoe.setText(_translate("MainWindow", "Convert Arabic-based Kurdish Digits to English Digits"))
        self.cdktop.setText(_translate("MainWindow", "Convert Arabic-based Kurdish Digits to Persian (Farsi)"))
        self.cdptok.setText(_translate("MainWindow", "Convert Persian (Farsi)  Digits to Arabic-based Kurdish"))
        self.label_3.setText(_translate("MainWindow", "Input :"))
        self.file_b_tab2.setText(_translate("MainWindow", "Choose file"))
        self.ti_tab2.setText(_translate("MainWindow", "Text input"))
        self.fi_tab2.setText(_translate("MainWindow", "File input"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Converting Number"))
        self.groupBox.setTitle(_translate("MainWindow", "Getting Unicode code for any Character or Digit"))
        self.label.setText(_translate("MainWindow", "Input :"))
        self.c_b_tab3.setText(_translate("MainWindow", "Get Unicode code"))
        self.s_b_tab3.setText(_translate("MainWindow", "Save Unicode code to file"))
        self.file_b_tab3.setText(_translate("MainWindow", "Choose file"))
        self.ti_tab3.setText(_translate("MainWindow", "Text input"))
        self.fi_tab3.setText(_translate("MainWindow", "File input"))
        self.gk.setText(_translate("MainWindow", "Get Arabic-based Kurdish Letters in a json list"))
        self.gl.setText(_translate("MainWindow", "Get Latin-based Kurdish Letters in a json list"))
        self.gv.setText(_translate("MainWindow", "Get all Latin-based and Arabic-based Kurdish vowels in a json list"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Get Characters Data"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuLanguage.setTitle(_translate("MainWindow", "Language"))
        self.actionEnglish.setText(_translate("MainWindow", "English"))
        self.actionKurdish.setText(_translate("MainWindow", "Kurdish"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionTextWrap.setText(_translate("MainWindow", "Text Wrap"))


    def translateUi(self):
        self.c_b_tab1.setText('گۆڕین و پیشاندان')
        self.cktol.setText('گۆڕینی کوردی بۆ لاتینی')
        self.caktok.setText('گۆڕینی عەلی-کەی بۆ یونیکۆد')
        self.catok.setText('گۆرینی پیتی عەرەبی بۆ کوردی')
        self.cetok.setText('گۆڕینی پیتی ئینگلیزی بۆ کوردی بە پێی سیستەمی KRG Unicode System')
        self.cktoe.setText('گۆڕینی پیتی کوردی بۆ ئینگلیزی بە پێی سیستەمی KRG Unicode System')
        self.s_b_tab1.setText('گۆڕین و پاراستنی لە فایلدا')
        self.ti_tab1.setText('تێکست')
        self.label_6.setText('ئینپوت')
        self.fi_tab1.setText('فایل')
        self.file_b_tab1.setText('هەڵبژاردنی فایل')
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), 'گۆڕینی تێکست')
        self.c_b_tab2.setText('گۆڕین و پیشاندان')
        self.s_b_tab2.setText('گۆڕین و پاراستنی لە فایلدا')
        self.cdetok.setText('گۆڕینی ژمارەی ئینگلیزی بۆ ژمارەی کوردی')
        self.cdktoe.setText('گۆڕینی ژمارەی کوردی بۆ ژمارەی ئینگلیزی')
        self.cdktop.setText('گۆڕینی ژمارەی کوردی بۆ ژمارەی فارسی')
        self.cdptok.setText('گۆڕینی ژمارەی فارسی بۆ ژمارەی کوردی')
        self.label_3.setText('ئینپوت')
        self.file_b_tab2.setText('هەڵبژاردن فایل')
        self.ti_tab2.setText('تێکست')
        self.fi_tab2.setText('فایل')
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), 'گۆڕینی ژمارە')
        self.groupBox.setTitle('وەرگرتنی کۆدی یونیکۆد بۆ هەر کاراکتەر یان ڕەنوسێک')
        self.label.setText('ئینپوت')
        self.c_b_tab3.setText('پیشاندانی کۆدی یونیکۆد')
        self.s_b_tab3.setText('پاراستنی کۆدی یونیکۆد لە فایلدا')
        self.file_b_tab3.setText('هەڵبژاردنی فایل')
        self.ti_tab3.setText('تێکست')
        self.fi_tab3.setText('فایل')
        self.gk.setText('پیشاندانی هەموو پیتە کوردیەکان لە لیستێکدا')
        self.gl.setText('پیشاندانی هەموو پیتە لاتینیەکان لە لیستێکدا')
        self.gv.setText('پیشاندانی پیتە بزوێنەکانی کوردی و لاتینی لە لیستێکدا')
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), 'پیشاندانی داتای پیتەکان')
        self.menuFile.setTitle('فایل')
        self.menuLanguage.setTitle('زمان')
        self.actionEnglish.setText('ئینگلیزی')
        self.actionKurdish.setText('کوردی')
        self.actionClose.setText('لابردن')
        self.actionAbout.setText('دەربارەی')
        self.actionTextWrap.setText('Text Wrap')


    def userDefinedMethod(self):
        self.actionEnglish.triggered.connect(self.translateToEnglish)
        self.actionKurdish.triggered.connect(self.translateToKurdish)
        self.actionClose.triggered.connect(QtCore.QCoreApplication.instance().quit)
        self.actionAbout.triggered.connect(self.showdialog)
        self.actionTextWrap.triggered.connect(self.actionTextWrap_clicked)

        self.copy.clicked.connect(self.copyClicked)
        self.save.clicked.connect(self.saveClicked)
        self.clear_out.clicked.connect(self.clear_out_clicked)
        
        self.paste_tab1.clicked.connect(self.tab1InputPaste)
        self.file_b_tab1.clicked.connect(self.file_b_tab1_clicked)
        self.c_b_tab1.clicked.connect(self.c_b_tab1_clicked)
        self.s_b_tab1.clicked.connect(self.file_s_tab1_clicked)
        self.clear_t.clicked.connect(self.clear_t_clicked)

        self.paste_tab2.clicked.connect(self.tab2InputPaste)
        self.file_b_tab2.clicked.connect(self.file_b_tab2_clicked)
        self.c_b_tab2.clicked.connect(self.c_b_tab2_clicked)
        self.s_b_tab2.clicked.connect(self.file_s_tab2_clicked)
        self.clear_t_2.clicked.connect(self.clear_t2_clicked)

        self.paste_tab3.clicked.connect(self.tab3InputPaste)
        self.file_b_tab3.clicked.connect(self.file_b_tab3_clicked)
        self.c_b_tab3.clicked.connect(self.c_b_tab3_clicked)
        self.s_b_tab3.clicked.connect(self.file_s_tab3_clicked)
        self.gk.clicked.connect(self.gk_clicked)
        self.gl.clicked.connect(self.gl_clicked)
        self.gv.clicked.connect(self.gv_clicked)

    def actionTextWrap_clicked(self):
    	if(getWrapMode() == QtWidgets.QTextEdit.WidgetWidth):
    		setWrapMode('noWrap')
    		self.actionTextWrap.setChecked(False)
    	else:
    		setWrapMode('wrap')
    		self.actionTextWrap.setChecked(True)
    	self.setWrapModes()

    def setWrapModes(self):
    	self.te_tab1.setLineWrapMode(getWrapMode())
    	self.te_tab2.setLineWrapMode(getWrapMode())
    	self.te_tab3.setLineWrapMode(getWrapMode())
    	self.out.setLineWrapMode(getWrapMode())
        
    def showdialog(self):
        d = QDialog()
        b1 = QtWidgets.QTextEdit(aboutText,d)
        b1.setGeometry(QtCore.QRect(5, 5, 390, 300))
        b1.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        d.setWindowTitle("About")
        d.setWindowModality(QtCore.Qt.ApplicationModal)
        d.setFixedSize(400,320)
        d.exec_()

    def translateToEnglish(self):
        setLanguage('e')
        self.retranslateUi(self.MainWindow)
        self.actionKurdish.setChecked(False)
        self.actionEnglish.setChecked(True)

    def translateToKurdish(self):
        setLanguage('k')
        self.translateUi()
        self.actionKurdish.setChecked(True)
        self.actionEnglish.setChecked(False)

    def copyClicked(self):
        self.out.selectAll()
        self.out.copy()
        
        #deselect
        my_text_cursor = self.out.textCursor()
        my_text_cursor.clearSelection()
        self.out.setTextCursor(my_text_cursor)

    def saveClicked(self):
        self.saveFileNameDialog(4)

    def clear_out_clicked(self):
        self.out.clear()

    def clear_t_clicked(self):
        self.te_tab1.clear()

    def clear_t2_clicked(self):
        self.te_tab2.clear()
        
    def tab1InputPaste(self):
        self.te_tab1.clear()
        self.te_tab1.paste()

    def tab2InputPaste(self):
        self.te_tab2.clear()
        self.te_tab2.paste()

    def tab3InputPaste(self):
        self.te_tab3.clear()
        self.te_tab3.paste()
    
    def openFileNameDialog(self, tabNum):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self.MainWindow,"Open Text Document", "","All Files (*);;Text Documents (*.txt)", options=options)
        if fileName:
            if tabNum == 1:
                self.file_tab1 = fileName
                self.file_t_tab1.setText(os.path.basename(fileName))
            elif tabNum == 2:
                self.file_tab2 = fileName
                self.file_t_tab2.setText(os.path.basename(fileName))
            else:
                self.file_tab3 = fileName
                self.file_t_tab3.setText(os.path.basename(fileName))
            
    def convertData(self, tabNum, data):
        result = data
        if tabNum == 1:
            if self.cktol.isChecked():
                result = ku.Hemwar().transliterate(result)
            elif self.cktoe.isChecked():
                result = ku.Hemwar().Ku_Char_to_En(result)
            elif self.cetok.isChecked():
                result = ku.Hemwar().En_Char_to_Ku(result)
            elif self.catok.isChecked():
                result = ku.Hemwar().Ar_Char_to_Ku(result)
            elif self.caktok.isChecked():
                result = ku.Hemwar().ali_k_to_uni(result)
        elif tabNum == 2:
            if self.cdetok.isChecked():
                result = ku.Hemwar().En_Digit_to_Ku(result)
            elif self.cdktoe.isChecked():
                result = ku.Hemwar().Ku_Digit_to_En(result)
            elif self.cdptok.isChecked():
                result = ku.Hemwar().Fa_Digit_to_Ku(result)
            elif self.cdktop.isChecked():
                result = ku.Hemwar().Ku_Digit_to_Fa(result)
        else:
            #Reusing kurdish.ku.Hemwar().getUniNum(self, x)
            # to get output instead of priting it to the console
            #
            #result = ku.Hemwar().getUniNum(result)
            result_ = result
            result = ''
            for i, char in enumerate(result_, start=1):
                try:
                    result += str(i) + ". " + char + " = U+%04x " % ord(char) + name(char)
                except:
                    result += str(i) + ". " + ' Error we couldn\'t get the Unicode code.'
                result += '\n'
        return result
            
    def saveFileNameDialog(self, tabNum):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self.MainWindow,"Save Text As File", "","Text Document (*.txt)", options=options)
        if fileName:
            fileName += '.txt'
            if tabNum == 1:
                data = self.te_tab1.toPlainText()
                if self.fi_tab1.isChecked() and hasattr(self, 'file_tab1'):
                    data = readFile(self.file_tab1)
                writeFile(fileName, self.convertData(1, data))
            elif tabNum == 2:
                data = self.te_tab2.toPlainText()
                if self.fi_tab2.isChecked() and hasattr(self, 'file_tab2'):
                    data = readFile(self.file_tab2)
                writeFile(fileName, self.convertData(2, data))
            elif tabNum == 3:
                data = self.te_tab3.toPlainText()
                if self.fi_tab3.isChecked() and hasattr(self, 'file_tab3'):
                    data = readFile(self.file_tab3)
                writeFile(fileName, self.convertData(3, data))
            else:
                writeFile(fileName, self.out.toPlainText())
    
    def file_b_tab1_clicked(self):
        self.openFileNameDialog(1)

    def file_b_tab2_clicked(self):
        self.openFileNameDialog(2)

    def file_b_tab3_clicked(self):
        self.openFileNameDialog(3)

    def file_s_tab1_clicked(self):
        self.saveFileNameDialog(1)

    def file_s_tab2_clicked(self):
        self.saveFileNameDialog(2)

    def file_s_tab3_clicked(self):
        self.saveFileNameDialog(3)
        
    def c_b_tab1_clicked(self):
        data = self.te_tab1.toPlainText()
        if self.fi_tab1.isChecked() and hasattr(self, 'file_tab1'):
            data = readFile(self.file_tab1)
        result = self.convertData(1, data)
        self.out.setPlainText(result)

    def c_b_tab2_clicked(self):
        data = self.te_tab2.toPlainText()
        if self.fi_tab2.isChecked() and hasattr(self, 'file_tab2'):
            data = readFile(self.file_tab2)
        result = self.convertData(2, data)
        self.out.setPlainText(result)

    def c_b_tab3_clicked(self):
        data = self.te_tab3.toPlainText()
        if self.fi_tab3.isChecked() and hasattr(self, 'file_tab3'):
            data = readFile(self.file_tab3)
        result = self.convertData(3, data)
        self.out.setPlainText(result)

    def gk_clicked(self):
        result = [str(x) for x in ku.Hemwar().ku_alphabet_Ar]
        self.out.setPlainText(json.dumps(result, ensure_ascii=False))

    def gl_clicked(self):
        result = [str(x) for x in ku.Hemwar().ku_alphabet_La_uppercase]
        self.out.setPlainText(json.dumps(result, ensure_ascii=False))

    def gv_clicked(self):
        result = [str(x) for x in ku.Hemwar().ku_all_V]
        self.out.setPlainText(json.dumps(result, ensure_ascii=False))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
