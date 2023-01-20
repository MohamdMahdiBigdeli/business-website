from dao.dataBase import connect_db
from model import Slider


def slider():
    rows = connect_db('''SELECT * FROM slider''')
    data = []
    for row in rows:
        a = Slider(row[0], row[1], row[2], row[3], row[4], row[5])
        data.append(a.__dict__)
    return data
