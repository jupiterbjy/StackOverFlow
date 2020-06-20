import json


a = {(0, 0): {(0, 0): 0, (1, 0): 1, (0, 1): 1, (1, 1): 2, (0, 2): 2, (1, 2): 3}, (1, 0): {(1, 0): 0, (0, 0): 1, (1, 1): 1, (0, 1): 2, (0, 2): 3, (1, 2): 2}, (0, 1): {(0, 1): 0, (0, 0): 1, (1, 1): 1, (0, 2): 1, (1, 0): 2, (1, 2): 2}, (1, 1): {(1, 1): 0, (1, 0): 1, (0, 1): 1, (1, 2): 1, (0, 0): 2, (0, 2): 2}, (0, 2): {(0, 2): 0, (0, 1): 1, (1, 2): 1, (0, 0): 2, (1, 0): 3, (1, 1): 2}, (1, 2): {(1, 2): 0, (1, 1): 1, (0, 2): 1, (0, 0): 3, (1, 0): 2, (0, 1): 2}}


def dict_key_convert(dic):  # need to convert tuple keys
    converted = {}
    for key, item in dic.items():
        if isinstance(item, dict):
            sub_dict = dict_key_convert(item)
            converted[str(key)] = sub_dict
        else:
            converted[str(key)] = item

    return converted


# print(json.dumps(dict_key_convert(a), indent=2))
with open('temp.json', 'w') as file:
    json.dump(dict_key_convert(a), file, indent=2)
