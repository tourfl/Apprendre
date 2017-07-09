# coding: utf-8

from os import path


def get_len(item):

    (a, b) = item

    return len(b)


def mylen(dic):
    return len(dic['lessons'])


def get_sorted_list(ls):
    dic = {}

    for filepath in ls:
        dirname, filename = path.split(filepath)
        dirname = dirname[7:]
        filename = filename[:-5]

        if dirname not in dic:
            dic[dirname] = []

        dic[dirname].append(filename)

    list = [(k, v) for k, v in dic.items()]

    list = sorted(list, key=get_len, reverse=True)

    return list


if __name__ == '__main__':
    path_list = ["static/English/Air Transport.json", "static/English/Extreme Sports.json", "static/Divers/US Presidents.json", "static/Portuguais/Colle1.json", "static/Portuguais/Colle2.json", "static/Portuguais/Colle3.json"]
    list = get_sorted_list(path_list)

    print(path_list)
    print(list)
