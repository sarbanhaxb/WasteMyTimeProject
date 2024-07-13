from PyQt5.QtWidgets import QMainWindow

import SQL
from UI.calc import Ui_Calc


class WasteCalc(QMainWindow, Ui_Calc):
    def __init__(self, object:str, PATH, parent=None):
        super(WasteCalc, self).__init__(parent)
        self.setupUi(self)
        self.setWindowModality(2)
        self.data = SQL.DataBase(PATH)
        self.object = object
        self.statusbar.setObjectName(object)

        self.back.clicked.connect(self.close)
        self.ExitAction.triggered.connect(self.close)
