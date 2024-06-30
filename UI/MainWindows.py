# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(650, 550)
        MainWindow.setMinimumSize(QtCore.QSize(650, 550))
        MainWindow.setMaximumSize(QtCore.QSize(650, 550))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 661, 61))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("UI/fon.jpg"))
        self.label.setObjectName("label")
        self.ButtonFrame = QtWidgets.QFrame(self.centralwidget)
        self.ButtonFrame.setGeometry(QtCore.QRect(0, 70, 661, 61))
        self.ButtonFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ButtonFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ButtonFrame.setObjectName("ButtonFrame")
        self.DeleteButton = QtWidgets.QPushButton(self.ButtonFrame)
        self.DeleteButton.setGeometry(QtCore.QRect(70, 10, 40, 40))
        self.DeleteButton.setText("")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI/icon/close"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DeleteButton.setIcon(icon)
        self.DeleteButton.setIconSize(QtCore.QSize(36, 36))

        self.DeleteButton.setObjectName("DeleteButton")
        self.AddButton = QtWidgets.QPushButton(self.ButtonFrame)
        self.AddButton.setGeometry(QtCore.QRect(10, 10, 40, 40))
        self.AddButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.AddButton.setText("")

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("UI/icon/ADD"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AddButton.setIcon(icon1)
        self.AddButton.setIconSize(QtCore.QSize(36, 36))

        # Кнопка добавления нового объекта + линии
        self.AddButton.setObjectName("AddButton")
        self.line = QtWidgets.QFrame(self.ButtonFrame)
        self.line.setGeometry(QtCore.QRect(50, 10, 20, 41))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.ButtonFrame)
        self.line_2.setGeometry(QtCore.QRect(110, 10, 20, 41))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        #кнопка выхода из программы
        self.ExitButton = QtWidgets.QPushButton(self.ButtonFrame)
        self.ExitButton.setGeometry(QtCore.QRect(130, 10, 40, 40))
        self.ExitButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap('UI/icon/exit'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ExitButton.setIcon(icon2)
        self.ExitButton.setIconSize(QtCore.QSize(43, 43))
        self.ExitButton.setObjectName("ExitButton")

        # Линии
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 60, 661, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(0, 130, 661, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")

        #ТРИВЬЮ
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(0, 140, 256, 351))
        self.treeView.setObjectName("treeView")

        # ПОЛЕ ИНФОРМАЦИИ
        self.InfoFrame = QtWidgets.QFrame(self.centralwidget)
        self.InfoFrame.setGeometry(QtCore.QRect(260, 140, 381, 351))
        self.InfoFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.InfoFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.InfoFrame.setObjectName("InfoFrame")
        self.InfoFrame.setEnabled(False)

        # Лейбл и поле ID города
        self.CityIDLabel = QtWidgets.QLabel(self.InfoFrame)
        self.CityIDLabel.setGeometry(QtCore.QRect(10, 10, 61, 23))
        self.CityIDLabel.setObjectName("CityIDLabel")
        self.CityIDField = QtWidgets.QTextEdit(self.InfoFrame)
        self.CityIDField.setGeometry(QtCore.QRect(100, 10, 100, 23))
        self.CityIDField.setObjectName("CityIDField")

        # Лейбл и поле ввода с наименованием города
        self.CityTitleLabel = QtWidgets.QLabel(self.InfoFrame)
        self.CityTitleLabel.setGeometry(QtCore.QRect(10, 40, 80, 23))
        self.CityTitleLabel.setObjectName("CityTitleLabel")
        self.CityTitleField = QtWidgets.QTextEdit(self.InfoFrame)
        self.CityTitleField.setGeometry(QtCore.QRect(100, 40, 211, 23))
        self.CityTitleField.setAcceptRichText(True)
        self.CityTitleField.setObjectName("CityTitleField")

        # Лейбл и поле ввода с ID объекта
        self.ObjectIDLabel = QtWidgets.QLabel(self.InfoFrame)
        self.ObjectIDLabel.setGeometry(QtCore.QRect(10, 70, 80, 23))
        self.ObjectIDLabel.setObjectName("ObjectIDLabel")
        self.ObjectIDField = QtWidgets.QTextEdit(self.InfoFrame)
        self.ObjectIDField.setGeometry(QtCore.QRect(100, 70, 211, 23))
        self.ObjectIDField.setObjectName("ObjectIDField")

        # Лейбл и поле ввода с наименованием объекта
        self.ObjectTitleLabel = QtWidgets.QLabel(self.InfoFrame)
        self.ObjectTitleLabel.setGeometry(QtCore.QRect(10, 100, 80, 23))
        self.ObjectTitleLabel.setObjectName("ObjectTitleLabel")
        self.ObjectTitleField = QtWidgets.QTextEdit(self.InfoFrame)
        self.ObjectTitleField.setGeometry(QtCore.QRect(100, 100, 211, 23))
        self.ObjectTitleField.setObjectName("ObjectTitleField")


        # Кнопка сохранения изменений
        self.saveChanges = QtWidgets.QPushButton(self.InfoFrame)
        self.saveChanges.setGeometry(QtCore.QRect(320, 310, 31, 31))
        self.saveChanges.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("UI/icon/save"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveChanges.setIcon(icon3)
        self.saveChanges.setIconSize(QtCore.QSize(24, 24))
        self.saveChanges.setObjectName("pushButton")

        # Кнопка отмены изменений
        self.cancelChanges = QtWidgets.QPushButton(self.InfoFrame)
        self.cancelChanges.setGeometry(QtCore.QRect(350, 310, 31, 31))
        self.cancelChanges.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("UI/icon/return"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelChanges.setIcon(icon4)
        self.cancelChanges.setIconSize(QtCore.QSize(24, 24))
        self.cancelChanges.setObjectName("pushButton_2")

        # Линии
        self.line_6 = QtWidgets.QFrame(self.InfoFrame)
        self.line_6.setGeometry(QtCore.QRect(0, 343, 381, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(250, 140, 20, 350))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")

        # Дерево
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setEnabled(True)
        self.treeWidget.setGeometry(QtCore.QRect(0, 140, 255, 350))
        font = QtGui.QFont()
        font.setKerning(True)
        self.treeWidget.setFont(font)
        self.treeWidget.setStatusTip("")
        self.treeWidget.setObjectName("treeWidget")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("UI/icon/city"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("UI/icon/organization"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 650, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu_2.addAction(self.action_3)
        self.menu_2.addAction(self.action_4)
        self.menu_3.addAction(self.action_5)
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Эколог-Отходы"))
        self.CityIDLabel.setText(_translate("MainWindow", "Код города:"))
        self.CityIDField.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\"></span></p></body></html>"))
        self.CityTitleField.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>"))
        self.ObjectIDField.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"right\" style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\"></span></p></body></html>"))
        self.ObjectTitleField.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"right\" style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\"></span></p></body></html>"))
        self.CityTitleLabel.setText(_translate("MainWindow", "Наименование:"))
        self.ObjectIDLabel.setText(_translate("MainWindow", "Код объекта:"))
        self.CityIDLabel.setText(_translate("MainWindow", "Код города:"))
        self.ObjectTitleLabel.setText(_translate("MainWindow", "Наименование:"))



        self.menu.setTitle(_translate("MainWindow", "Справочники"))
        self.menu_2.setTitle(_translate("MainWindow", "Настройки"))
        self.menu_3.setTitle(_translate("MainWindow", "Справка"))
        self.action.setText(_translate("MainWindow", "Просмотр ФККО"))
        self.action_2.setText(_translate("MainWindow", "Просмотр БДО"))
        self.action_3.setText(_translate("MainWindow", "Параметры программы"))
        self.action_4.setText(_translate("MainWindow", "Расположение базы данных"))
        self.action_5.setText(_translate("MainWindow", "О программе"))

