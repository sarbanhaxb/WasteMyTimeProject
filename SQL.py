import sqlite3
from typing import List, Any

import pandas as pd

class DataBase:
    def __init__(self):
        self.DB = sqlite3.connect('DataBase.db')
        self.cursor = self.DB.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON;")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS cities ("
                            "id INTEGER PRIMARY KEY,"
                            "title VARCHAR(100) NOT NULL)"
                            "")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS objects("
                            "id INTEGER PRIMARY KEY,"
                            "id_city INTEGER,"
                            "title VARCHAR(100) NOT NULL UNIQUE,"
                            "FOREIGN KEY (id_city) REFERENCES cities(id) ON DELETE CASCADE" 
                            ")")
        if not self.cursor.execute("SELECT EXISTS(SELECT 1 FROM sqlite_master WHERE type='table' AND name='fkko');").fetchone()[0]:
            self.createFKKO()
        self.DB.commit()

    def updateCityData(self, title, id) -> None:
        self.cursor.execute("UPDATE cities SET title=? WHERE id=?", (title, id))
        self.DB.commit()

    def updateObjectData(self, title, id) -> None:
        self.cursor.execute("UPDATE objects SET title=? WHERE id=?", (title, id))
        self.DB.commit()

    def deleteCity(self, title) -> None:
        self.cursor.execute(f"DELETE FROM cities WHERE title='{title}'")
        self.DB.commit()

    def deleteObject(self, title, id):
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

    def addNewCity(self, title:str):
        self.cursor.execute("INSERT INTO cities (title) VALUES (?)", (title,))
        self.DB.commit()

    def addNewOrganization(self, id_city, title:str):
        self.cursor.execute(f"INSERT INTO objects (id_city, title) VALUES ('{int(id_city)}', '{title}')")
        self.DB.commit()

    def getIDObject(self, title) -> str:
        return str(self.cursor.execute(f"SELECT id FROM objects WHERE title='{title}'").fetchall()[0][0])

    def createFKKO(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS fkko ("
                            "id INTEGER PRIMARY KEY, "
                            "num VARCHAR(30) NOT NULL, "
                            "title VARCHAR(300) NOT NULL"
                            ")")

        BDO = pd.read_excel(
            "https://rpn.gov.ru/upload/iblock/22b/6kwwkka1n6d2r4yznwz2dqqlhlzrxy60/bank_dannykh_ob_otkhodakh-_3_.xlsx",
            skiprows=3)
        for row in BDO.itertuples():
            self.cursor.execute(f"INSERT INTO fkko (num, title) VALUES (?, ?)", (str(row[1]), str(row[2])))
            self.DB.commit()

"""testing command"""
bd = DataBase()
# bd.getObjects().values()
# print(bd.getDataCount())