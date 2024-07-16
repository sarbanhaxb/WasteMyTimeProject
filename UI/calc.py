# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calc(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(700, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(700, 480))
        MainWindow.setMaximumSize(QtCore.QSize(700, 480))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 250, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.backButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.backButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI/icon/WasteCalc/back.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backButton.setIcon(icon)
        self.backButton.setObjectName("backButton")
        self.horizontalLayout.addWidget(self.backButton)
        self.lineBetweenBackAndAdd = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.lineBetweenBackAndAdd.setFrameShape(QtWidgets.QFrame.VLine)
        self.lineBetweenBackAndAdd.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineBetweenBackAndAdd.setObjectName("lineBetweenBackAndAdd")
        self.horizontalLayout.addWidget(self.lineBetweenBackAndAdd)
        self.ButtonAddCalc = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.ButtonAddCalc.setText("")
        self.ButtonAddCalc.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("UI/icon/WasteCalc/page_add.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonAddCalc.setIcon(icon1)
        self.ButtonAddCalc.setObjectName("ButtonAddCalc")
        self.horizontalLayout.addWidget(self.ButtonAddCalc)
        self.ButtonDelete = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.ButtonDelete.setText("")
        self.ButtonDelete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("UI/icon/WasteCalc/page_delete.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonDelete.setIcon(icon2)
        self.ButtonDelete.setObjectName("ButtonDelete")
        self.horizontalLayout.addWidget(self.ButtonDelete)

        self.saveChangeButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.saveChangeButton.setText("")
        self.saveChangeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("UI/icon/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveChangeButton.setIcon(icon5)
        self.saveChangeButton.setObjectName("saveChangeButton")
        self.horizontalLayout.addWidget(self.saveChangeButton)

        self.lineBetweenDelAndCalc = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.lineBetweenDelAndCalc.setFrameShape(QtWidgets.QFrame.VLine)
        self.lineBetweenDelAndCalc.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineBetweenDelAndCalc.setObjectName("lineBetweenDelAndCalc")
        self.horizontalLayout.addWidget(self.lineBetweenDelAndCalc)

        self.goCalcButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.goCalcButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("UI/icon/WasteCalc/calc.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.goCalcButton.setIcon(icon3)
        self.goCalcButton.setObjectName("goCalcButton")
        self.goCalcButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalLayout.addWidget(self.goCalcButton)

        self.printButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.printButton.setText("")
        self.printButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("UI/icon/WasteCalc/print.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.printButton.setIcon(icon4)
        self.printButton.setObjectName("printButton")
        self.horizontalLayout.addWidget(self.printButton)
        self.lineBetweenButtonsAndTable = QtWidgets.QFrame(self.centralwidget)
        self.lineBetweenButtonsAndTable.setGeometry(QtCore.QRect(10, 36, 681, 20))
        self.lineBetweenButtonsAndTable.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineBetweenButtonsAndTable.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineBetweenButtonsAndTable.setObjectName("line")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 50, 681, 351))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 440, 160, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)
        self.AddNewCalc = QtWidgets.QAction(MainWindow)
        self.AddNewCalc.setObjectName("AddNewCalc")
        self.EditCalc = QtWidgets.QAction(MainWindow)
        self.EditCalc.setObjectName("EditCalc")
        self.DeleteCalc = QtWidgets.QAction(MainWindow)
        self.DeleteCalc.setObjectName("DeleteCalc")
        self.ExitAction = QtWidgets.QAction(MainWindow)
        self.ExitAction.setObjectName("ExitAction")
        self.menu.addAction(self.AddNewCalc)
        self.menu.addAction(self.EditCalc)
        self.menu.addAction(self.DeleteCalc)
        self.menu.addSeparator()
        self.menu.addAction(self.ExitAction)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Расчет образования отходов"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Код"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Название расчета"))
        self.menu.setTitle(_translate("MainWindow", "Данные"))
        self.AddNewCalc.setText(_translate("MainWindow", "Добавить вариант расчета"))
        self.EditCalc.setText(_translate("MainWindow", "Редактировать вариант расчета"))
        self.DeleteCalc.setText(_translate("MainWindow", "Удалить вариант расчета"))
        self.ExitAction.setText(_translate("MainWindow", "Выход"))
