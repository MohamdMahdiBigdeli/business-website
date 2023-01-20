from dao.dataBase import connect_db
from model import HowWeWorks


def how_we_works():
    rows = connect_db('''SELECT * FROM how_we_works''')
    data = []
    for row in rows:
        row = HowWeWorks(row[0], row[1], row[2], row[3])
        data.append(row.__dict__)
    return data
