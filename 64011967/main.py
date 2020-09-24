from PySide2.QtWidgets import QWidget, QApplication, QTextEdit, QVBoxLayout
import sys

import module


class UI(QWidget):
    def __init__(self):
        super(UI, self).__init__()
        self.layout = QVBoxLayout()
        self.text = QTextEdit()
        self.aux = QTextEdit()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.aux)

        self.setLayout(self.layout)


class MainWindow(UI):
    def __init__(self):
        super().__init__()
        self.text.textChanged.connect(self.onChange)

    def onChange(self):
        module.onChange(self.aux, self.text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
