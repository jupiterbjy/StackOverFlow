from tkinter import Tk, Button


class MainWindow:
    def __init__(self, root_tk):

        self.add_button = Button(root_tk, text="add", command=self.add_row)
        self.del_button = Button(root_tk, text="del", command=self.del_row)

        self.add_button.pack()
        self.del_button.pack()

        self.w = 720
        self.h = 150

        self.root = root_tk

        self.update_geometry()
        self.root.mainloop()

    def update_geometry(self):
        self.root.geometry(f"{self.w}x{self.h}")

    def add_row(self):
        self.adjust_height(10)

    def del_row(self):
        self.adjust_height(-10)

    def adjust_height(self, delta: int):
        self.h += delta
        self.update_geometry()


root = Tk()
MainWindow(root)
