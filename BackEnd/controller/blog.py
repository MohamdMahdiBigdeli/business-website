from dao.dataBase import connect_db
from model import Blog, BlogAuthor, BlogAuthorSocials


def blog():
    # rows = connect_db('''SELECT * FROM pricing_table''')
    # data = []
    # for row in rows:
    #     PLAN_FEATURES = connect_db('''SELECT planFeatures FROM pricing_table_plan_features WHERE ID = ''' + str(row[0]))
    #     plan_features = []
    #     for i in PLAN_FEATURES:
    #         plan_features.append(i[0])
    #     row = Blog(row[0], row[1], row[2], row[3], row[4], plan_features)
    #     data.append(row.__dict__)
    # return data
    rows = connect_db('''SELECT * FROM blog''')
    data = []
    for row in rows:
        SOCIALS = connect_db('''SELECT facebook,twitter,linkedin FROM blog_author_socials WHERE ID = ''' + str(row[0]))
        socials = BlogAuthorSocials(SOCIALS[0][0], SOCIALS[0][1], SOCIALS[0][2])
        AUTHOR = connect_db('''SELECT name,designation,proPic FROM blog_author WHERE ID = ''' + str(row[0]))
        author = BlogAuthor(AUTHOR[0][0], AUTHOR[0][1], AUTHOR[0][2], socials.__dict__)
        row = Blog(row[0], row[1], row[2], row[3], row[4], author.__dict__)
        data.append(row.__dict__)
    return data