import random
import string
import sys
import time

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import pyqtSignal, Qt, QRect
from PyQt5.QtWidgets import QMainWindow, QLabel, QMessageBox, QTreeWidgetItem, QMenu, QAction, QTableWidget, \
    QTableWidgetItem, QHeaderView, QFileDialog, QDialog, QVBoxLayout, QLineEdit, QProgressBar, QWidget, QComboBox

import SQL
from UI.AddCityWindow import Ui_NewCity
from UI.MainWindows import Ui_MainWindow
from UI.AddObjectWindow import Ui_NewObject
from screeninfo import get_monitors

def ref(item, count):
    c = count
    while item.parent() != None:
        c += 1
        item = item.parent()
        ref(item, c)
    return c

PATH = 'DataBase.db'

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.addCity = None
        self.setupUi(self)
        self.data = None
        self.connectDB()
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
        self.addOrg.triggered.connect(self.newObject)
        self.deleteOrg.triggered.connect(self.DeletePos)


        #ОКНО РАСЧЕТА
        self.treeWidget.doubleClicked.connect(self.OpenWasteCalc)

        #просмотр БДО
        self.showBDO.triggered.connect(self.openBDO)

        #выбор базы данных
        self.DBPlaceMenu.triggered.connect(self.OpenFileDB)

    def connectDB(self, path = PATH):
        self.data = SQL.DataBase(path)
        self.PrintTree()

    def OpenFileDB(self):
        global PATH
        dialog = QFileDialog(self)
        dialog.setWindowTitle("Выбрать базу данных")
        dialog.setNameFilter("Файл базы данных (*.db)")
        if dialog.exec_():
            self.connectDB(dialog.selectedFiles()[0])

    def openBDO(self):
        self.bdo = TableBDO(self.data.getTableSize('bdo'), 14)
        self.bdo.show()

    def newObject(self):
        self.addObject = AddNewObjectWidget(self.CityIDField.toPlainText())
        self.addObject.show()
        self.addObject.windowsclosed.connect(self.PrintTree)

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
        try:
            if ref(self.treeWidget.selectedItems()[0], 0) == 0:
                title = self.CityTitleField.toPlainText()
                id = self.CityIDField.toPlainText()
                self.data.updateCityData(title, id)
                self.PrintTree()
            elif ref(self.treeWidget.selectedItems()[0], 0) == 1:
                # тут нужно сделать проверку не поменял ли пользователь название объекта на такое, которое уже есть в таблице objects, иначе крашится программа, так как в таблице objects title уникальное.
                id = self.ObjectIDField.toPlainText()
                title = self.ObjectTitleField.toPlainText()
                self.data.updateObjectData(title, id)
                self.PrintTree()
        except IndexError:
            pass

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
        self.data = SQL.DataBase(PATH)

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
        self.data = SQL.DataBase(PATH)

    def addObject(self):
        try:
            self.data.addNewOrganization(self.ID, self.ObjectTitleField.text())
            self.close()
        except IndexError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка")
            msg.setText("Объект с таким названием существует.")
            msg.setWindowTitle('Ошибка')
            msg.exec_()

    def closeEvent(self, event):
        self.windowsclosed.emit()
        event.accept()

class TableBDO(QDialog):
    def __init__(self, row_count, col_count):
        super().__init__()
        self.data = SQL.DataBase(PATH)
        self.bdo = self.data.getBDO()
        self.initUI(row_count, col_count)

    def initUI(self, row, col):
        columnTitle = ("Код по ФККО",
                       "Наименование вида отхода",
                       "Происхождение (Производство)",
                       "Происхождение (Исходная продукция (товар)",
                       "Происхождение (Процесс)",
                       "Состав (Наименование компонентов)",
                       "Состав (Содержание, % масс. (минимум)",
                       "Состав (Содержание, % масс. (максимум)",
                       "Примечание о компонентном составе",
                       "Примечание к виду отхода",
                       "Агрегатное состояние и физическая форма",
                       "Класс опасности",
                       "Критерии отнесения",
                       "Документ (основание)")

        self.setWindowTitle("Банк данных об отходах")
        self.setGeometry(0, 0, 1800, 800)
        self.setWindowModality(2)

        self.table_widget = QTableWidget()
        self.table_widget.setWordWrap(True)
        self.table_widget.setColumnCount(col)
        self.table_widget.setHorizontalHeaderLabels(columnTitle)
        self.table_widget.setRowCount(row)
        self.table_widget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)


        for i in range(row):
            for j in range(col):
                if str(self.bdo[i][j]) == 'nan':
                    el = ''
                else:
                    el = str(self.bdo[i][j]).strip('\n')
                item = QTableWidgetItem(el)
                item.setTextAlignment(0x0001)
                item.setFlags(item.flags() | 0x0002)
                item.setFlags(item.flags() | 0x0004)
                self.table_widget.setItem(i, j, item)
            # self.table_widget.verticalHeader().setSectionResizeMode(i, QHeaderView.ResizeToContents)
        self.table_widget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.table_widget)


        # Названия фильтров
        self.FkkoLineLabel = QLabel()
        self.FkkoLineLabel.setText('Фильтр по коду ФККО')
        self.TitleLineLabel = QLabel()
        self.TitleLineLabel.setText('Фильтр по наименованию отхода')
        self.OriginLineLabel = QLabel()
        self.OriginLineLabel.setText('Фильтр по происхождению')
        self.CompoundLineLabel = QLabel()
        self.CompoundLineLabel.setText('Фильтр по составу')
        self.HazardClass = QLabel()
        self.HazardClass.setText('Фильтр по классу опасности')

        # строки ввода фильтров
        self.fkko_line = QLineEdit()
        self.title_line = QLineEdit()
        self.origin_line = QLineEdit()
        self.compound_line = QLineEdit()
        self.hazard_box = QComboBox()
        self.hazard_box.addItems(('I', 'II', "III", "IV", "V"))

        # подключение фильтра к событию изменения текста в line
        self.fkko_line.textChanged.connect(self.filterTable)
        self.title_line.textChanged.connect(self.filterTable)
        self.origin_line.textChanged.connect(self.filterTable)
        self.compound_line.textChanged.connect(self.filterTable)
        self.hazard_box.currentTextChanged.connect(self.filterTable)

        # добавление на слой LabelLine и Line
        self.layout.addWidget(self.FkkoLineLabel)
        self.layout.addWidget(self.fkko_line)
        self.layout.addWidget(self.TitleLineLabel)
        self.layout.addWidget(self.title_line)
        self.layout.addWidget(self.OriginLineLabel)
        self.layout.addWidget(self.origin_line)
        self.layout.addWidget(self.CompoundLineLabel)
        self.layout.addWidget(self.compound_line)
        self.layout.addWidget(self.HazardClass)
        self.layout.addWidget(self.hazard_box)

        self.setLayout(self.layout)

    def filterTable(self):
        fkko_filter_text = self.fkko_line.text()
        title_filter_text = self.title_line.text()
        origin_filter_text = self.origin_line.text()
        compound_filter_list = [i.lower() for i in self.compound_line.text().split()]
        hazard_filter_text = self.hazard_box.currentText()

        for row in range(self.table_widget.rowCount()):
            fkko_item = self.table_widget.item(row, 0)
            title_item = self.table_widget.item(row, 1)
            origin1_item = self.table_widget.item(row, 2)
            origin2_item = self.table_widget.item(row, 3)
            origin3_item = self.table_widget.item(row, 4)
            compound_list = [i.lower() for i in self.table_widget.item(row, 5).text().split()]
            hazard_item = self.table_widget.item(row, 11)

            if (fkko_filter_text.lower() in fkko_item.text().lower()
                    and title_filter_text.lower() in title_item.text().lower())\
                    and (origin_filter_text.lower() in origin1_item.text().lower() or origin_filter_text.lower() in origin2_item.text().lower() or origin_filter_text.lower() in origin3_item.text().lower())\
                    and set(compound_filter_list).issubset(compound_list)\
                    and hazard_filter_text.lower() == hazard_item.text().lower():
                self.table_widget.setRowHidden(row, False)
            else:
                self.table_widget.setRowHidden(row, True)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
