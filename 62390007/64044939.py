from collections.abc import Callable  # just for type hinting.


def handle_error(callable_: Callable, error_dict: dict, *args):
    try:
        callable_(*args)
    except Exception as err:
        print(error_dict[type(err)])


# Testers
def tester(error_type):
    raise error_type()


# Test
handle_error(lambda: tester(ValueError), {ValueError: "bad val", AttributeError: "bad attr"})
handle_error(lambda: tester(AttributeError), {ValueError: "bad val", AttributeError: "bad attr"})

