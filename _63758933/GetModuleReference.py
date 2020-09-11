from sys import modules
from inspect import getmembers, isclass, isfunction
# import re


def ListTarget(name, target, blacklist, return_dict):

    if blacklist is None:
        blacklist = {}

    try:
        members = getmembers(modules[name], target)
    except KeyError:
        members = getmembers(modules[name.__name__], target)

    filtered = [i for i in members if i[0] not in blacklist and not i[0].startswith('_')]

    return FunctionToDict([i for _, i in filtered]) if return_dict else [i for i, _ in filtered]


def ListClass(name, blacklist=None, return_dict=False):
    return ListTarget(name, isclass, blacklist, return_dict)


def ListFunction(name, blacklist=None, return_dict=False):
    return ListTarget(name, isfunction, blacklist, return_dict)


def FunctionToDict(func_list):
    return dict((i.__name__, i) for i in func_list)
