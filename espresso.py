import sqlite3

conn = sqlite3.connect("coffee.sqlite")
cursor = conn.cursor()

conn.close()