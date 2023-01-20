from dao.dataBase import connect_db
from model import Funfact


def funfact():
    rows = connect_db('''SELECT * FROM funfact''')
    data = []
    for row in rows:
        row = Funfact(row[0], row[1], row[2])
        data.append(row.__dict__)
    return data
