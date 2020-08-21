import json
from pprint import pprint

relative_loc = "./file_data.json"


def write():
    some_list = [i for i in range(3)]
    some_dict = {i: n for i, n in enumerate(range(0, 6, 2))}
    some_name = [i * 2 for i in 'abcd']

    to_file = {"list": some_list,
               "dict": some_dict,
               "name": some_name}

    with open(relative_loc, 'w') as f:
        json.dump(to_file, f, indent=2)


def read():
    with open(relative_loc, 'r') as f:
        file = json.load(f)

    pprint(file)


write()
read()
