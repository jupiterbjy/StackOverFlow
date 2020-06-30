from functools import singledispatch
import timeit

words = ["Ekke", "ekke", "Ptang", "Zoo", "Boing"]
args_list = [("arg1", "Ni!"), ("arg2", "Peng!"), ("arg3", "Neee-Wom!"), ("arg4", words)]


def do_something(a, b):
    pass


# ---------------------------------
@singledispatch
def func(a, b):
    do_something(a, b)


@func.register(list)
def func_list(a, b):
    for i in b:
        do_something(a, i)


def single_dispatched():
    for arg, item in args_list:
        func(arg, item)


# ---------------------------------
def is_instance_method():
    for arg, item in args_list:
        if isinstance(item, list):
            for i in item:
                do_something(arg, i)
        else:
            do_something(arg, item)


# ---------------------------------
def try_except_method():
    for arg, item in args_list:
        try:
            for i in item:
                do_something(arg, i)
        except TypeError:
            do_something(arg, item)


# ---------------------------------

single_result = timeit.timeit(single_dispatched, number=100)
is_instance_result = timeit.timeit(is_instance_method, number=100)
try_except_result = timeit.timeit(try_except_method, number=100)

print(single_result, is_instance_result, try_except_result, sep='\n')
