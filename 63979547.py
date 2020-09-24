from functools import wraps


def typed_decorator(target_type):

    def decorator_inner(func):
        @wraps(func)  # this copy signature of given function to wrapper for easier debugging.
        def wrapper(*args):
            return target_type(func(*args))

        return wrapper

    return decorator_inner


@typed_decorator(int)
def do_something(val):
    return val


@typed_decorator(bool)
def do_other(val):
    return val


print(type(do_something("20")))
print(type(do_other("30")))
