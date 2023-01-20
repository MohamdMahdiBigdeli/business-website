import pyodbc
import os


def connect_db(select):
    conn = pyodbc.connect(
        r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + str(os.getcwd()) + "\dao\DB.accdb;")
    cursor = conn.cursor()
    cursor.execute(str(select))
    json = cursor.fetchall()
    conn.close()
    return json

