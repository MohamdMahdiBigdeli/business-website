from dao.dataBase import connect_db
from model import CallToAction


def call_to_actiondata():
    rows = connect_db('''SELECT * FROM call_to_action''')
    data = []
    for row in rows:
        row = CallToAction(row[1], row[2], row[3], row[4])
        data.append(row.__dict__)
    return data
