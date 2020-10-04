from PySide2.QtWidgets import QMainWindow, QApplication
from .ui_main import Ui_MainWindow
import threading
import sys


def function_to_be_run(event: threading.Event):
    while not event.is_set():
        # Do your stuff here. We'll just print and wait using event.wait().

        print("Alive 'n kickin'")
        event.wait(1)

    print('Good bye!')


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.released.connect(self.starter)

    def stopper(self, thread_event: threading.Event, thread: threading.Thread):
        thread_event.set()
        thread.join()  # Wait for thread to finish

        self.pushButton.released.connect(self.starter)  # connect button back to starter

    def starter(self):
        event = threading.Event()
        t = threading.Thread(target=function_to_be_run, args=[event])
        t.start()

        self.pushButton.released.connect(lambda x: self.stopper(event, t))  # connect to stopper so it can stop.

    def if_button_is_toggle(self):
        if self.pushButton.isChecked():
            pass  # stop thread here
        else:
            pass  # run thread here


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
