from api import db

def get_list_data(title):

    list_ = []

    Association.query.filter_by(title=title).all()

    return list_


def get_list_meta(title):
    pass

