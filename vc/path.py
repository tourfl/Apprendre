from os import path
from pprint import pprint


def get_dic(ls):
    dic = {}

    for filepath in ls:
        dirname, filename = path.split(filepath)
        dirname = dirname[7:]
        filename = filename[:-5]

        if dirname not in dic:
            dic[dirname] = []

        dic[dirname].append(filename)

    return dic


if __name__ == '__main__':
    path_list = ["static/English/Air Transport.json", "static/English/Extreme Sports.json"]
    dic = get_dic(path_list)

    print(path_list)
    pprint(dic)