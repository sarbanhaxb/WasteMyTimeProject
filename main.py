import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QLabel, QMessageBox, QTreeWidgetItem

import SQL
from UI.AddCityWindow import Ui_NewCity
from UI.MainWindows import Ui_MainWindow


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
        self.textEdit.setDisabled(True)

        # Удаление города
        self.DeleteButton.clicked.connect(self.DeleteCity)

        # Обновление поля информации
        self.treeWidget.itemSelectionChanged.connect(self.refreshEditText)

        #сохранение изменения
        self.saveChanges.clicked.connect(self.updateData)

        #отменить изменения
        self.cancelChanges.clicked.connect(self.cabcel)
    def cabcel(self):
        self.refreshEditText()

    def updateData(self):
        self.data.updateCityData(self.textEdit_2.toPlainText(), self.textEdit.toPlainText())
        self.PrintTree()

    def addNewCity(self) -> None:
        self.addCity = AddNewCityWidget()
        self.addCity.show()
        self.addCity.windowsclosed.connect(self.PrintTree)

    def DeleteCity(self) -> None:
        if self.treeWidget.selectedItems():
            msgCommit = QMessageBox(self)
            msgCommit.setIcon(QMessageBox.Warning)
            msgCommit.setWindowTitle("Удаление города")
            msgCommit.setText('Будут удалены все данные о городе. Уверены?')
            msgCommit.addButton("Да", QMessageBox.YesRole)
            msgCommit.addButton("Нет", QMessageBox.NoRole)
            if not msgCommit.exec_():
                self.data.deleteCity(self.treeWidget.selectedItems()[0].text(0))
                self.PrintTree()

    def refreshEditText(self):
        if self.treeWidget.selectedItems():
            self.textEdit.setText(self.data.getIDCity(self.treeWidget.selectedItems()[0].text(0)))
            self.textEdit_2.setText(self.treeWidget.selectedItems()[0].text(0))

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
            s = QtWidgets.QTreeWidgetItem(self.treeWidget)
            s.setIcon(0, CitiesIcon)
            s.setText(0, _translate("MainWindow", k))
            if i in objects.keys():
                for j in objects[i]:
                    b = QtWidgets.QTreeWidgetItem(s)
                    b.setText(0, _translate("MainWindow", j))
                    b.setIcon(0, ObjectIcon)

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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
