
import json

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text # more comfortable with textual SQL


def get_titles(db, category):
    if category=="all" or category==None:
        condition = None

        return my_query(db, columns="category, title", model="List", condition=condition)

    else:
        return {'English': ['Money', 'Corporate_world']}


def my_query(db, columns, model, condition):
    if condition==None:
        where_condition = ""

    else:
        where_condition = " WHERE " + condition

    txt = text("SELECT " + columns + " FROM " + model + where_condition)

    return data_to_dict(db.engine.execute(txt).fetchall())


def data_to_dict(data):

    if type(data) is list:
        return list_of_rowproxy_to_dict(data)

    else:
        return {"Problem": "this is not a list"}


def list_of_rowproxy_to_dict(lst):

    dic = {}

    for element in lst:
        print(type(element))
        vals = element.values()

        print(vals)

        if dic.has_key(vals[0]):
            dic[vals[0]].append(vals[1])
        else:
            dic[vals[0]]=[vals[1]]

    return dic

    # return {'English': ['Money', 'Corporate_world'], 'Divers': ['Stratégie', 'Marketing']}


if __name__ == '__main__':
    pass

