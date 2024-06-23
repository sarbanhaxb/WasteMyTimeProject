import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow

import SQL
from UI.MainWindows import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.data = SQL.DataBase()
        self.PrintTree()

        self.ExitButton.clicked.connect(self.closeApp)

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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
