from tkinter import Tk, Button


class MainWindow:
    def __init__(self, root_tk):
        self._functions_to_run = [self.a, self.b, self.c]

        self.add_button = Button(root_tk, text="run next", command=self.without_closure)
        self.add_button.pack()

        self.root = root_tk
        self.root.mainloop()

    def without_closure(self):
        try:
            self._functions_to_run.pop(0)()
        except IndexError:
            print("empty!")

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
