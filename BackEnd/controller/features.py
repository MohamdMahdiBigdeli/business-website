from dao.dataBase import connect_db
from model import Features


def features():
    rows = connect_db('''SELECT * FROM features''')
    data = []
    for row in rows:
        row = Features(row[0], row[1], row[2], row[3])
        data.append(row.__dict__)
    return data
