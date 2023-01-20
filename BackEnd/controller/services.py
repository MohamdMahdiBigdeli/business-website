from dao.dataBase import connect_db
from model import Services


def services():
    rows = connect_db('''SELECT * FROM services''')
    data = []
    for row in rows:
        PREVIEW_IMAGES = connect_db('''SELECT previewImages FROM sliderPreviewImages WHERE ID = ''' + str(row[0]))
        preview_images = []
        for i in PREVIEW_IMAGES:
            preview_images.append(i[0])
        FEATURES = connect_db('''SELECT features FROM sliderFeatures WHERE ID = ''' + str(row[0]))
        features = []
        for i in FEATURES:
            features.append(i[0])
        row = Services(row[0], row[1], row[2], row[3], preview_images, row[4], features)
        data.append(row.__dict__)
    return data
