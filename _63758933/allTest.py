from . import GetModuleReference


class Test:
    def __init__(self):
        pass

    func_list = {
        'method_1': (1, 2, 3),
        'method_2': ('a', 'b', 'c')
    }

    @classmethod
    def gen_func(cls):
        for name, arg in cls.func_list.items():
            cls.name = lambda: print(arg)
