# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myUi.ui',
# licensing of 'myUi.ui' applies.
#
# Created: Thu Jun 25 13:01:09 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1274, 791)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-6, -1, 1281, 731))
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.target = QtWidgets.QLabel(self.tab1)
        self.target.setGeometry(QtCore.QRect(10, 90, 600, 600))
        self.target.setText("")
        self.target.setObjectName("target")
        self.frame = QtWidgets.QLabel(self.tab1)
        self.frame.setGeometry(QtCore.QRect(650, 90, 600, 600))
        self.frame.setText("")
        self.frame.setObjectName("frame")
        self.targetTxt_2 = QtWidgets.QLabel(self.tab1)
        self.targetTxt_2.setGeometry(QtCore.QRect(260, 30, 121, 16))
        self.targetTxt_2.setObjectName("targetTxt_2")
        self.frameTxt = QtWidgets.QLabel(self.tab1)
        self.frameTxt.setGeometry(QtCore.QRect(900, 30, 111, 16))
        self.frameTxt.setObjectName("frameTxt")
        self.loadBtn = QtWidgets.QPushButton(self.tab1)
        self.loadBtn.setGeometry(QtCore.QRect(550, 10, 171, 28))
        self.loadBtn.setObjectName("loadBtn")
        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.updateBtn = QtWidgets.QPushButton(self.tab2)
        self.updateBtn.setGeometry(QtCore.QRect(650, 10, 111, 28))
        self.updateBtn.setObjectName("updateBtn")
        self.label_5 = QtWidgets.QLabel(self.tab2)
        self.label_5.setGeometry(QtCore.QRect(250, 30, 151, 20))
        self.label_5.setObjectName("label_5")
        self.graficOut = QtWidgets.QLabel(self.tab2)
        self.graficOut.setGeometry(QtCore.QRect(20, 90, 600, 600))
        self.graficOut.setText("")
        self.graficOut.setObjectName("graficOut")
        self.textOut = QtWidgets.QLabel(self.tab2)
        self.textOut.setGeometry(QtCore.QRect(800, 110, 391, 381))
        self.textOut.setText("")
        self.textOut.setObjectName("textOut")
        self.label_8 = QtWidgets.QLabel(self.tab2)
        self.label_8.setGeometry(QtCore.QRect(930, 30, 151, 20))
        self.label_8.setObjectName("label_8")
        self.startBtn = QtWidgets.QPushButton(self.tab2)
        self.startBtn.setGeometry(QtCore.QRect(510, 10, 111, 28))
        self.startBtn.setObjectName("startBtn")
        self.tabWidget.addTab(self.tab2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1274, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.targetTxt_2.setText(QtWidgets.QApplication.translate("MainWindow", "Целевая сборка", None, -1))
        self.frameTxt.setText(QtWidgets.QApplication.translate("MainWindow", "Текущая сборка", None, -1))
        self.loadBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Загрузить целевую сборку", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QtWidgets.QApplication.translate("MainWindow", "Сборки", None, -1))
        self.updateBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Обновить этап", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "Графическая отладка", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("MainWindow", "Текстовая отладка", None, -1))
        self.startBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Старт", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), QtWidgets.QApplication.translate("MainWindow", "Отладка", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

