from dao.dataBase import connect_db
from model import Testimonial


def testimonials():
    rows = connect_db('''SELECT * FROM testimonial''')
    data = []
    for row in rows:
        row = Testimonial(row[0], row[1], row[2], row[3], row[4])
        data.append(row.__dict__)
    return data
