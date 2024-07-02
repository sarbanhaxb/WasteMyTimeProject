import random
import string
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QMainWindow, QLabel, QMessageBox, QTreeWidgetItem, QMenu, QAction


import SQL
from UI.AddCityWindow import Ui_NewCity
from UI.MainWindows import Ui_MainWindow
from UI.AddObjectWindow import Ui_NewObject


def ref(item, count):
    c = count
    while item.parent() != None:
        c += 1
        item = item.parent()
        ref(item, c)
    return c

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.addCity = None
        self.setupUi(self)
        self.data = SQL.DataBase()
        self.PrintTree()
        self.ExitButton.clicked.connect(self.closeApp)
        self.AddButton.clicked.connect(self.addNewCity)
        WinIcon = QtGui.QIcon()
        WinIcon.addPixmap(QtGui.QPixmap('UI/icon/trash-svgrepo-com.svg'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(QtGui.QIcon('UI/icon/trash-svgrepo-com.svg'))
        # self.CityIDField.setDisabled(True)

        # Удаление города/объекта
        self.DeleteButton.clicked.connect(self.DeletePos)

        # Обновление поля информации
        self.treeWidget.itemSelectionChanged.connect(self.refreshEditText)

        #сохранение изменения
        self.saveChanges.clicked.connect(self.updateData)

        #отменить изменения
        self.cancelChanges.clicked.connect(self.cancel)

        #Контекст меню на City
        self.contextMenu = QMenu(self.treeWidget)
        self.addOrg = QAction("Добавить новый объект", self)
        self.addOrg.setIcon(QtGui.QIcon("UI/icon/organization.svg"))
        self.deleteOrg = QAction("Удалить строку", self)
        self.deleteOrg.setIcon(QtGui.QIcon("UI/icon/basket-svgrepo-com.svg"))
        self.treeWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.treeWidget.customContextMenuRequested.connect(self.showContextMenu)
        self.contextMenu.addAction(self.addOrg)
        self.contextMenu.addAction(self.deleteOrg)
        self.addOrg.triggered.connect(self.newOrganization)
        self.deleteOrg.triggered.connect(self.DeletePos)


        #ОКНО РАСЧЕТА
        self.treeWidget.doubleClicked.connect(self.OpenWasteCalc)

    def newOrganization(self):
        self.addOrganization = AddNewObjectWidget(self.CityIDField.toPlainText())
        self.addOrganization.show()
        self.addOrganization.windowsclosed.connect(self.PrintTree)

    def OpenWasteCalc(self):
        if ref(self.treeWidget.selectedItems()[0], 0) == 1:
            print('YES')
        else:
            print("NOTHING")

    def showContextMenu(self, pos):
        if self.treeWidget.itemAt(pos) is not None and ref(self.treeWidget.selectedItems()[0], 0) == 0:
            self.contextMenu.exec_(self.sender().mapToGlobal(pos))
        elif self.treeWidget.itemAt(pos) is not None and ref(self.treeWidget.selectedItems()[0], 0) == 1:
            # нужно поработать над контекст меню
            self.contextMenu.exec_(self.sender().mapToGlobal(pos))

    def cancel(self) -> None:
        self.refreshEditText()

    def updateData(self) -> None:
        if ref(self.treeWidget.selectedItems()[0], 0) == 0:
            title = self.CityTitleField.toPlainText()
            id = self.CityIDField.toPlainText()
            self.data.updateCityData(title, id)
            self.PrintTree()
        elif ref(self.treeWidget.selectedItems()[0], 0) == 1:
            id = self.ObjectIDField.toPlainText()
            title = self.ObjectTitleField.toPlainText()
            self.data.updateObjectData(title, id)
            self.PrintTree()

    #Добавляет новый город
    def addNewCity(self) -> None:
        self.addCity = AddNewCityWidget()
        self.addCity.show()
        self.addCity.windowsclosed.connect(self.PrintTree)

    #Удаляет город
    def DeletePos(self) -> None:
        if self.treeWidget.selectedItems() and ref(self.treeWidget.selectedItems()[0], 0) == 0:
            msgCommit = QMessageBox(self)
            msgCommit.setIcon(QMessageBox.Warning)
            msgCommit.setWindowTitle("Удаление города")
            msgCommit.setText('Будут удалены все данные о городе. Уверены?')
            msgCommit.addButton("Да", QMessageBox.YesRole)
            msgCommit.addButton("Нет", QMessageBox.NoRole)
            if not msgCommit.exec_():
                self.data.deleteCity(self.treeWidget.selectedItems()[0].text(0))
                self.PrintTree()
        elif self.treeWidget.selectedItems() and ref(self.treeWidget.selectedItems()[0], 0) == 1:
            title = self.treeWidget.selectedItems()[0].text(0)
            id = self.data.getIDObject(title)
            msgCommit = QMessageBox(self)
            msgCommit.setIcon(QMessageBox.Warning)
            msgCommit.setWindowTitle("Удаление объекта")
            msgCommit.setText("Будут удалены все данные об организации. Уверены?")
            msgCommit.addButton("Да", QMessageBox.YesRole)
            msgCommit.addButton("Нет", QMessageBox.NoRole)
            if not msgCommit.exec_():
                self.data.deleteObject(title, id)
                self.PrintTree()


    #Печать дерева
    def PrintTree(self) -> None:
        self.treeWidget.clear()
        _translate = QtCore.QCoreApplication.translate
        CitiesIcon = QtGui.QIcon()
        CitiesIcon.addPixmap(QtGui.QPixmap("UI/icon/city"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ObjectIcon = QtGui.QIcon()
        ObjectIcon.addPixmap(QtGui.QPixmap("UI/icon/organization.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Город"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        objects = self.data.getObjects()
        cities = self.data.getCities()
        for i, k in zip(cities.keys(), cities.values()):
            item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
            item_0.setIcon(0, CitiesIcon)
            item_0.setText(0, _translate("MainWindow", k))
            if i in objects.keys():
                for j in objects[i]:
                    item_1 = QtWidgets.QTreeWidgetItem(item_0)
                    item_1.setText(0, _translate("MainWindow", j))
                    item_1.setIcon(0, ObjectIcon)
        self.treeWidget.expandAll()

    def refreshEditText(self) -> None:
        pass
        self.InfoFrame.setEnabled(True)
        if self.treeWidget.selectedItems() and ref(self.treeWidget.selectedItems()[0], 0) == 0:
            id = self.data.getIDCity(self.treeWidget.selectedItems()[0].text(0))
            title = self.data.getTitleCity(id)
            self.CityIDField.setEnabled(True)
            self.CityTitleField.setEnabled(True)
            self.CityIDField.setText(id)
            self.CityIDField.setEnabled(False)
            self.CityTitleField.setText(title)
            self.ObjectIDField.setEnabled(False)
            self.ObjectTitleField.setEnabled(False)
            self.ObjectTitleField.setText("")
            self.ObjectIDField.setText("")
        elif self.treeWidget.selectedItems() and ref(self.treeWidget.selectedItems()[0], 0) == 1:
            id = self.data.getIDCity(self.treeWidget.selectedItems()[0].parent().text(0))
            titleCity = self.data.getTitleCity(id)
            title = self.treeWidget.selectedItems()[0].text(0)
            self.CityIDField.setText(id)
            self.CityIDField.setEnabled(False)
            self.CityTitleField.setText(titleCity)
            self.CityTitleField.setEnabled(False)
            self.ObjectIDField.setText(self.data.getIDObject(title))
            self.ObjectIDField.setEnabled(False)
            self.ObjectTitleField.setEnabled(True)
            self.ObjectTitleField.setText(title)
        else:
            pass

    def closeApp(self) -> None:
        self.close()


class AddNewCityWidget(QLabel, Ui_NewCity):
    windowsclosed = pyqtSignal()

    def __init__(self, parent=None):
        super(AddNewCityWidget, self).__init__(parent)
        self.setupUi(self)
        self.setWindowModality(2)
        self.ReturnBTN.clicked.connect(self.close)
        self.addCityBTN.clicked.connect(self.addCity)
        self.setWindowIcon(QtGui.QIcon("UI/icon/city.svg"))
        self.data = SQL.DataBase()

    def addCity(self):
        self.data.addNewCity(self.CityTitleField.text())
        self.close()

    def closeEvent(self, event):
        self.windowsclosed.emit()
        event.accept()

class AddNewObjectWidget(QLabel, Ui_NewObject):
    windowsclosed = pyqtSignal()

    def __init__(self, ID, parent=None):
        super(AddNewObjectWidget, self).__init__(parent)
        self.setupUi(self)
        self.ID = ID
        self.setWindowModality(2)
        self.ReturnBTN.clicked.connect(self.close)
        self.addObjectBTN.clicked.connect(self.addObject)
        self.setWindowIcon(QtGui.QIcon("UI/icon/organization.svg"))
        self.data = SQL.DataBase()

    def addObject(self):
        self.data.addNewOrganization(self.ID, self.ObjectTitleField.text())
        self.close()

    def closeEvent(self, event):
        self.windowsclosed.emit()
        event.accept()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
