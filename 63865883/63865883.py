from sys import modules
from os.path import abspath
from os import getcwd, chdir

from Module import a
import timeit


def get_path(obj):
    try:
        return abspath(obj.__file__)
    except AttributeError:  # it's probably not a module
        return abspath(modules[obj.__module__].__file__)


print(f"working directory: {getcwd()}")
print(get_path(a))
print(get_path(timeit))

chdir('/')

print(f"working directory: {getcwd()}")
print(get_path(a))
print(get_path(timeit))
