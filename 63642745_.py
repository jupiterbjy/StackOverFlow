from tkinter import Tk, Button


class MainWindow:
    def __init__(self, root_tk):

        self.add_button = Button(root_tk, text="run next", command=self.closure_example())
        self.add_button.pack()

        self.root = root_tk
        self.root.mainloop()

    def closure_example(self):
        function_iter = iter((self.a, self.b, self.c))

        def wrapper():
            nonlocal function_iter
            try:
                return next(function_iter)()
            except StopIteration:
                print('empty!')

        return wrapper

    @staticmethod
    def a():
        print('a')

    @staticmethod
    def b():
        print('b')

    @staticmethod
    def c():
        print('c')


root = Tk()
MainWindow(root)
