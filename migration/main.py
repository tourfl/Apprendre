# from files to db


import json
import glob


path = '../data/'


def main():
    list_fn = get_filenames()

    for filename in list_fn:
        print(filename)
        with open(path + filename) as data:
            put_in_db(json.load(data))


def get_filenames():
    list_fn = []

    for file in glob.glob(path + "*/*.json"):
        list_fn.append(file)

    return list_fn


def put_in_db(data_json):
    pass


if __name__ == '__main__':
    main()
