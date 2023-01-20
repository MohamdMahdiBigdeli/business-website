from dao.dataBase import connect_db
from model import Team


def team():
    rows = connect_db('''SELECT * FROM team''')
    data = []
    for row in rows:
        row = Team(row[0], row[1], row[2],row[3])
        data.append(row.__dict__)
    return data
