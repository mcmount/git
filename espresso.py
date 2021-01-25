import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem



class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('cofee.ui', self)

        conn = sqlite3.connect("coffee.sqlite")
        cursor = conn.cursor()
        result = cursor.execute('''SELECT * FROM Tea''').fetchall()

        #for row in result:
        #    inx = result.index(row)

        print(result)
        self.start.clicked.connect(self.run)

    def run(self):
        QTableWidget.setItem(1, 1, QTableWidgetItem('test'))

            # add more if there is more columns in the database.
           # self.tableWidget_2.setItem(inx, 0, QTableWidgetItem(row[1]))
            #self.tableWidget_2.setItem(inx, 1, QTableWidgetItem(row[2]))
            #self.tableWidget_2.setItem(inx, 2, QTableWidgetItem(row[3]))
        #conn.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())



conn = sqlite3.connect("coffee.sqlite")
cursor = conn.cursor()

conn.close()