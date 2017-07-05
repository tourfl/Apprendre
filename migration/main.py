# from files to db


import json
import glob
import os
import requests
import datetime


path = "../data/"


def main():
    list_fn = get_filenames()

    for filename in list_fn:
        print(filename)
        with open(path + filename) as data:
            new_data = miseEnForme(json.load(data), filename)
            put_in_db(new_data)


def get_filenames():
    list_fn = []

    for file in glob.glob(path + "*/*.json"):
        list_fn.append(file)

    return list_fn


def miseEnForme(data, filename):
    # general
    new_data = {}

    new_data["data"] = data["Vocabulary"]
    new_data["header"] = data["header"]
    new_data.update(data["description"])

    # date
    new_data["date"] = datetime.datetime.strptime(new_data["date"], '%Y-%d-%m').strftime('%Y-%m-%dT06:00:00Z')

    # title and category
    path, title = os.path.split(os.path.splitext(filename)[0])
    path = os.path.normpath(path)
    cat = path.split(os.sep)[-1]

    new_data["title"] = title
    new_data["category"] = cat

    return new_data


def put_in_db(data_json):
    r = requests.post('http://127.0.0.1:5000/lessons/', json=data_json)

    return r


if __name__ == "__main__":
    main()
