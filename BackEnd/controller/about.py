from dao.dataBase import connect_db
from model import About


def about():
    rows = connect_db('''SELECT * FROM about''')
    data = []
    for row in rows:
        row = About(row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        data.append(row.__dict__)
    return data
