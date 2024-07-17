from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QMainWindow, QLabel, QTableWidgetItem, QMessageBox, QMenu, QAction, QShortcut

import SQL
from UI.AddObjectWindow import Ui_NewObject
from UI.calc import Ui_Calc


class WasteCalc(QMainWindow, Ui_Calc):
    def __init__(self, id, PATH, parent=None):
        super(WasteCalc, self).__init__(parent)
        self.setupUi(self)
        self.setWindowModality(2)
        self.data = SQL.DataBase(PATH)
        self.object_ID = id
        self.backButton.clicked.connect(self.close)
        self.backButton.setToolTip("Назад")
        self.ExitAction.triggered.connect(self.close)
        self.data.createObjectTable()

        self.refreshTable()

        self.ButtonAddCalc.clicked.connect(self.addNewCalc)
        self.ButtonAddCalc.setToolTip("Добавить вариант расчета")
        self.AddNewCalc.triggered.connect(self.addNewCalc)

        self.ButtonDelete.clicked.connect(self.DelCalc)
        self.ButtonDelete.setToolTip("Удалить вариант расчета")
        self.DeleteCalc.triggered.connect(self.DelCalc)

        self.tableWidget.cellClicked.connect(self.on_cell_clicked)
        self.choosenPos = None

        self.saveChangeButton.clicked.connect(self.updateTableData)
        self.saveChangeButton.setToolTip("Сохранить изменения")
        self.saveChangeShortcut = QShortcut(QKeySequence("Ctrl+S"), self)
        self.saveChangeShortcut.activated.connect(self.updateTableData)

        self.goCalcButton.setToolTip("Выполнить расчет")
        self.goCalcButton.clicked.connect(self.goCalc)
        self.tableWidget.doubleClicked.connect(self.goCalc)

        self.printButton.setToolTip("Выгрузить отчет")
        self.printButton.clicked.connect(self.printCalc)

        self.contextMenu = QMenu(self.tableWidget)
        action1 = self.contextMenu.addAction("Добавить вариант расчета")
        action2 = self.contextMenu.addAction("Удалить вариант расчета")

        action1.triggered.connect(self.addNewCalc)
        action2.triggered.connect(self.DelCalc)

        self.tableWidget.cellChanged.connect(self.updateTableData)

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(lambda pos: self.contextMenu.exec_(self.mapToGlobal(pos)))

    def showContextMenu(self, pos) -> None:
        if self.tableWidget.itemAt(pos) is not None:
            self.contextMenu.exec_(self.sender().mapToGlobal(pos))
        elif self.treeWidget.itemAt(pos) is not None:
            self.contextMenu.exec_(self.sender().mapToGlobal(pos))

    def printCalc(self):
        if self.tableWidget.selectedItems():
            print("Print")
            pass

    def goCalc(self):
        if self.tableWidget.selectedItems():
            print('CALC')
            pass

    def updateTableData(self) -> None:
        try:
            self.data.updateTable(self.tableWidget.selectedItems()[0].text(), self.choosenPos)
            self.refreshTable()
        except IndexError:
            pass

    def on_cell_clicked(self, row, column) -> None:
        row_data = [self.tableWidget.item(row, column).text()
                    for column in range(self.tableWidget.columnCount())]
        self.choosenPos = row_data[2]

    def addNewCalc(self) -> None:
        self.data.addCalcTablePosition(self.object_ID)
        self.refreshTable()

    def DelCalc(self) -> None:
        if self.tableWidget.selectedItems():
            msgCommit = QMessageBox(self)
            msgCommit.setIcon(QMessageBox.Warning)
            msgCommit.setWindowTitle("Удаление расчета")
            msgCommit.setText('Будут удалены все данные. Уверены?')
            msgCommit.addButton("Да", QMessageBox.YesRole)
            msgCommit.addButton("Нет", QMessageBox.NoRole)
            if len(self.tableWidget.selectedItems()) == 1:
                if not msgCommit.exec_():
                    self.data.delCalcTablePosition(self.choosenPos)
                    self.refreshTable()
            else:
                if not msgCommit.exec_():
                    selected_rows = set()
                    for item in self.tableWidget.selectedItems():
                        selected_rows.add(item.row())

                    values = []
                    for row in selected_rows:
                        row_data = []
                        for column in range(self.tableWidget.columnCount()):
                            item = self.tableWidget.item(row, column)
                            if item is not None:
                                row_data.append(item.text())
                            else:
                                row_data.append('')
                        values.append(row_data[2])
                    self.data.delCalcTablePositions(values)
                    self.refreshTable()


    def refreshTable(self) -> None:
        self.tableWidget.clear()
        data = self.data.CalcTableRefresh(self.object_ID)

        columnTitle = ("Код", "Наименование расчета", "ID")

        self.tableWidget.setWordWrap(True)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(columnTitle)
        self.tableWidget.setColumnWidth(0, 40)
        self.tableWidget.setColumnHidden(2, True)
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.verticalHeader().hide()

        for i in range(len(data)):
            item = QTableWidgetItem(str(data[i][0]))
            item_num = QTableWidgetItem(str(i+1))
            item_id = QTableWidgetItem(str(data[i][1]))
            item_num.setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(i, 0, item_num)
            self.tableWidget.setItem(i, 1, item)
            self.tableWidget.setItem(i, 2, item_id)







