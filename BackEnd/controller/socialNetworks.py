from dao.dataBase import connect_db
from model import SocialNetworks


def social_networks():
    rows = connect_db('''SELECT * FROM social_networks''')
    data = []
    for row in rows:
        row = SocialNetworks(row[0], row[1], row[2])
        data.append(row.__dict__)
    return data
