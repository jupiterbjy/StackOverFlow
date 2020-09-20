from sys import modules
from os.path import abspath
from os import getcwd, chdir
import inspect

from Module import a
import timeit


def closure():
    original_working_dir = abspath(__file__)  # store absolute path for linux

    def _get_path(obj):
        nonlocal original_working_dir

        try:
            return abspath(obj.__file__)

        except AttributeError:  # it's probably not a module
            if obj.__module__ == '__main__':  # check if module is same as local:
                return abspath(original_working_dir)

            return abspath(modules[obj.__module__].__file__)
    return _get_path


get_path = closure()


def test_func():
    pass


def test_output():
    print(f"\nworking directory: {getcwd()}")
    print(f"import from: {get_path(a)}")
    print(f"simple import: {get_path(timeit)}")
    print(f"local function: {get_path(test_func)}")


if __name__ == '__main__':
    test_output()
    chdir('/')
    test_output()
    print(inspect.stack())
