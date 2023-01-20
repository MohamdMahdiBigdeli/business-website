from dao.dataBase import connect_db
from model import PricingTable


def pricing_table():
    rows = connect_db('''SELECT * FROM pricing_table''')
    data = []
    for row in rows:
        PLAN_FEATURES = connect_db('''SELECT planFeatures FROM pricing_table_plan_features WHERE ID = ''' + str(row[0]))
        plan_features = []
        for i in PLAN_FEATURES:
            plan_features.append(i[0])
        row = PricingTable(row[0], row[1], row[2], row[3], row[4], plan_features)
        data.append(row.__dict__)
    return data
