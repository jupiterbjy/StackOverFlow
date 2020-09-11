from PySide2.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QLabel, QStackedWidget
import sys

# PyQt5 대신 PySide2 사용, 임포트 경로는 달라도 결과는 유사합니다.
# Using PySide2 as an alternative to PyQt5 - Only difference would be import route.


class Base(QWidget):

    def __init__(self, label):
        super().__init__()

        self.label = QLabel(label)
        self.previous_button = QPushButton("Next")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.previous_button)

        self.setLayout(self.layout)


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.widgets = [Base(f"{i}번 화면") for i in range(3)]

        self.stack = QStackedWidget()
        for widget in self.widgets:
            widget.previous_button.released.connect(self.onSignal)
            self.stack.addWidget(widget)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.stack)

        self.setLayout(self.layout)

    def onSignal(self):
        current_idx = self.stack.currentIndex()
        idx_next = 0 if current_idx == self.stack.count() - 1 else current_idx + 1
        self.stack.setCurrentIndex(idx_next)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
