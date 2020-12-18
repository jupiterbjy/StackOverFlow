from itertools import tee


def split_on_condition_gen(seq, condition):
    seq_copy, seq_current = tee(seq)
    counter = 0

    def inner_gen(seq_, start, end):
        nonlocal counter

        for _ in range(counter, start):  # Skip from counter to start
            next(seq_)

        for _ in range(start, end):  # yield from start to end
            yield next(seq_)

            counter = end

    last = 0

    for idx, item in enumerate(seq_current):
        if condition(item):
            continue

        yield inner_gen(seq_copy, last, idx)
        last = idx + 1

    yield inner_gen(seq_copy, last, idx + 1)


class NonIndexAble:
    def __init__(self, initial: str):
        self.source = initial
        self.list_ = list(initial)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.list_.pop(0)
        except IndexError:
            raise StopIteration()


def test_non_index_able():
    """
    >>> non_index_able = NonIndexAble('aabaaaba')
    >>> condition = lambda x: x == "a"

    >>> for part in split_on_condition_gen(non_index_able, condition):
    ...     print("Part start")
    ...     for item in part:
    ...         print(item, end=' ')
    ...     print("\\nEnd")
    Part start
    a a
    End
    Part start
    a a a
    End
    Part start
    a
    End

    >>> non_index_able = NonIndexAble('asdf adsfa ds sdfdf adf')
    >>> condition = lambda x: x != ' '

    >>> for part in split_on_condition_gen(non_index_able, condition):
    ...     print("Part start")
    ...     for item in part:
    ...         print(item, end=' ')
    ...     print("\\nEnd")
    Part start
    a s d f
    End
    Part start
    a d s f a
    End
    Part start
    d s
    End
    Part start
    s d f d f
    End
    Part start
    a d f
    End

    """


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # Why this fails? how?
