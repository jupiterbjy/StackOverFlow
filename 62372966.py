from PySide2.QtWidgets import QWidget, QApplication, QTextEdit, QVBoxLayout
import sys


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.layout = QVBoxLayout()
        self.texts = [QTextEdit() for _ in range(12)]

        for widget in self.texts:
            widget.setTabChangesFocus(True)
            self.layout.addWidget(widget)

        self.setLayout(self.layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
