from dao.dataBase import connect_db
from model import BrandLogo


def brand_logo():
    rows = connect_db('''SELECT * FROM team''')
    data = []
    for row in rows:
        row = BrandLogo(row[0], row[1], row[2])
        data.append(row.__dict__)
    return data
