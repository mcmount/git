import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow



class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('cofee.ui', self)

        self.start.clicked.connect(self.run)

    def run(self):
        conn = sqlite3.connect("coffee.sqlite")
        cursor = conn.cursor()
        result = conn.execute('''SELECT * FROM Cofe_base''').fetchall()
        for row in result:
            inx = result.index(row)
            print(result)
            # add more if there is more columns in the database.
           # self.tableWidget_2.setItem(inx, 0, QTableWidgetItem(row[1]))
            #self.tableWidget_2.setItem(inx, 1, QTableWidgetItem(row[2]))
            #self.tableWidget_2.setItem(inx, 2, QTableWidgetItem(row[3]))
        conn.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())



conn = sqlite3.connect("coffee.sqlite")
cursor = conn.cursor()

conn.close()