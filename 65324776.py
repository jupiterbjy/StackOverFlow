import typing as t

T = t.TypeVar('T')


def split_on_condition_gen(seq, condition) -> t.Iterable[t.Iterable[T]]:
    def inner_gen(range_: range):
        for n in range_:
            yield seq[n]

    last = 0
    current = 0

    for item in seq:
        if condition(item):
            current += 1
        else:
            yield inner_gen(range(last, current))
            last = current


"""
>>> from this import s as seq_
~~ ZEN OF PYTHON GOES HERE ~~

>>> condition = lambda x: x != ','
>>> output = split_on_condition_gen(seq_, condition)
>>> output
<generator object split_on_condition_gen at 0x000002602C1ECEB0>

>>> list_output = list(output)
>>> list_output[2]
<generator object split_on_condition_gen.<locals>.inner_gen at 0x000002602C1ECEB0>

>>> list(list_output[2])
['l', ',', ' ', 'e', 'r', 's', 'h', 'f', 'r', ' ', ...]
"""
