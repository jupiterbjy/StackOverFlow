from collections.abc import MutableSequence, Iterable


class PrintingMutable(MutableSequence):
    def __init__(self, source: (MutableSequence, Iterable) = None):
        try:
            self.arr = list(source)
        except TypeError:
            self.arr = []

    def __repr__(self):
        return repr(self.arr)

    def insert(self, index: int, o) -> None:
        self.arr.insert(index, o)  # fail-fast
        self.on_insert(index, o)

    def __getitem__(self, i: (int, slice)):
        val = self.arr[i]  # creating unnecessary name to fail-fast.

        if isinstance(i, slice):
            for idx in range(i.start, i.stop, i.step if i.step else 1):
                self.on_get(idx)
        else:
            self.on_get(i)

        return val

    def __setitem__(self, i: int, o) -> None:
        self.arr[i] = o
        self.on_set(i)

    def __delitem__(self, i: int) -> None:  # I don't think I'm gonna use it.
        del self.arr[i]
        self.on_del(i)

    def __len__(self) -> int:
        return len(self.arr)

    def on_insert(self, idx, item):
        print(f"insert item {item} at {idx}")
        self.print_statistics()

    def on_get(self, idx):
        print(f"get item {self.arr[idx]} at {idx}")
        self.print_statistics()

    def on_set(self, idx):
        print(f"set item {self.arr[idx]} at {idx}")
        self.print_statistics()

    def on_del(self, idx):
        print(f"del item {self.arr[idx]} at {idx}")
        self.print_statistics()

    def print_statistics(self):
        print(self)
