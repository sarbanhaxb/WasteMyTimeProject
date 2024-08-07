import sqlite3
from typing import List, Any

import pandas as pd
from PyQt5.QtWidgets import QMessageBox


class DataBase:
    def __init__(self, path):
        PATH = path
        self.DB = sqlite3.connect(PATH)
        self.cursor = self.DB.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON;")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS cities ("
                            "id INTEGER PRIMARY KEY,"
                            "title VARCHAR(100) NOT NULL UNIQUE)"
                            "")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS objects("
                            "id INTEGER PRIMARY KEY,"
                            "id_city INTEGER,"
                            "title VARCHAR(100) NOT NULL UNIQUE,"
                            "FOREIGN KEY (id_city) REFERENCES cities(id) ON DELETE CASCADE"
                            ")")
        if not \
        self.cursor.execute("SELECT EXISTS(SELECT 1 FROM sqlite_master WHERE type='table' AND name='bdo');").fetchone()[
            0]:
            self.createBDO()
        self.DB.commit()

        self.createObjectTable()

    def updateCityData(self, title, id) -> None:
        self.cursor.execute("UPDATE cities SET title=? WHERE id=?", (title, id))
        self.DB.commit()

    def updateObjectData(self, title, id) -> None:
        self.cursor.execute("UPDATE objects SET title=? WHERE id=?", (title, id))
        self.DB.commit()

    def deleteCity(self, title) -> None:
        self.cursor.execute(f"DELETE FROM cities WHERE title='{title}'")
        self.DB.commit()

    def deleteObject(self, title, id) -> None:
        self.cursor.execute(f"DELETE FROM objects WHERE title='{title}' AND id='{id}'")
        self.DB.commit()

    def getCities(self) -> dict:
        di = dict()
        for i in self.cursor.execute("SELECT * FROM cities").fetchall():
            di[i[0]] = i[1]
        return di

    def getObjects(self) -> dict:
        d = dict()
        for i in self.cursor.execute("SELECT * FROM objects").fetchall():
            if i[1] in d:
                d[i[1]].append(i[2])
            else:
                d[i[1]] = [i[2]]
        return d

    def getIDCity(self, title) -> str:
        return str(self.cursor.execute(f"SELECT id FROM cities WHERE title='{title}'").fetchall()[0][0])

    def getTitleCity(self, id) -> str:
        return str(self.cursor.execute(f"SELECT title FROM cities WHERE id='{id}'").fetchall()[0][0])

    def addNewCity(self, title: str) -> None:
        if self.DB.execute(f"SELECT * FROM cities WHERE title='{title}'").fetchall():
            raise NameError
        else:
            self.cursor.execute("INSERT INTO cities (title) VALUES (?)", (title,))
            self.DB.commit()

    def addNewOrganization(self, id_city, title: str) -> None:
        if self.DB.execute(f"SELECT * FROM objects WHERE title='{title}'").fetchall():
            raise NameError
        else:
            self.cursor.execute(f"INSERT INTO objects (id_city, title) VALUES ('{int(id_city)}', '{title}')")
            self.DB.commit()

    def getIDObject(self, title) -> str:
        return str(self.cursor.execute(f"SELECT id FROM objects WHERE title='{title}'").fetchall()[0][0])

    def createBDO(self) -> None:
        self.cursor.execute("CREATE TABLE IF NOT EXISTS bdo ("
                            "id INTEGER PRIMARY KEY, "
                            "num VARCHAR(30), "
                            "title VARCHAR(300),"
                            "originManufacturing VARCHAR(300), "
                            "originProducts VARCHAR (300),"
                            "originProcess VARCHAR (300),"
                            "compound VARCHAR (300),"
                            "compoundPercentMin FLOAT,"
                            "compoundPercentMax FLOAT,"
                            "compoundNotice VARCHAR (300),"
                            "wasteNotice VARCHAR(300),"
                            "physicalState VARCHAR(300),"
                            "hazardClass VARCHAR(3),"
                            "attributionCriteria VARCHAR(5),"
                            "docs VARCHAR(300)"
                            ")")

        BDO = pd.read_excel(
            'BDO/bank_dannykh_ob_otkhodakh-_3_.xlsx',
            skiprows=3)
        for row in BDO.itertuples():
            self.cursor.execute(
                f"INSERT INTO bdo (num, title, originManufacturing, originProducts, originProcess, compound, compoundPercentMin, compoundPercentMax, compoundNotice, wasteNotice, physicalState, hazardClass, attributionCriteria, docs) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8]),
                 str(row[9]), str(row[10]), str(row[11]), str(row[12]), str(row[13]), str(row[14])))
            self.DB.commit()

    def getTableSize(self, name: str) -> int:
        return self.DB.execute(f"SELECT count (*) FROM '{name}'").fetchall()[0][0]

    def getFKKO(self) -> list:
        return self.DB.execute("SELECT num, title, hazardClass from bdo").fetchall()

    def getBDO(self) -> list:
        return self.DB.execute("SELECT num, title, originManufacturing, originProducts, originProcess, compound, compoundPercentMin, compoundPercentMax, compoundNotice, wasteNotice, physicalState, hazardClass, attributionCriteria, docs FROM bdo").fetchall()

    def createObjectTable(self) -> None:
        self.DB.execute(f"CREATE TABLE IF NOT EXISTS calcObjectsInfo "
                       f"(id INTEGER PRIMARY KEY, "
                        f"id_object INTEGER, "
                        f"title VARCHAR(100), "
                        f"FOREIGN KEY (id_object) REFERENCES objects(id) ON DELETE CASCADE)")

    def CalcTableRefresh(self, id) -> list:
        return self.DB.execute(f"SELECT title, id FROM calcObjectsInfo WHERE id_object = '{id}'").fetchall()

    def addCalcTablePosition(self, id, title="") -> None:
        self.DB.execute(f"INSERT INTO calcObjectsInfo (id_object, title) VALUES ('{id}', '{title}')")
        self.DB.commit()

    def delCalcTablePosition(self, id) -> None:
        if id:
            self.DB.execute(f"DELETE FROM calcObjectsInfo WHERE id={id}")
            self.DB.commit()

    def delCalcTablePositions(self, ids) -> None:
        if ids:
            for id in ids:
                self.delCalcTablePosition(id)

    def updateTable(self, title, id) -> None:
        self.DB.execute(f"UPDATE calcObjectsInfo SET title='{title}' WHERE id='{id}'")
        self.DB.commit()


"""testing command"""
bd = DataBase('DataBase.db')
# bdo = bd.getBDO()
# for i in range(2):
#     for j in range(14):
#         print(bdo[i][j])
# bd.getObjects().values()
# print(bd.getDataCount())
