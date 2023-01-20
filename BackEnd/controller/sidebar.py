from dao.dataBase import connect_db
from model import Sidebar


def sidebar():
    rows = connect_db('''SELECT * FROM sidebar''')
    data = []
    for row in rows:
        row = Sidebar(row[0], row[1], row[2])
        data.append(row.__dict__)
    return data
