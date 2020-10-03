import sys
from PySide2.QtWidgets import QApplication, QGridLayout, QWidget, QTextEdit
from PySide2.QtCore import QUrl
from PySide2.QtWebEngineWidgets import QWebEngineView


class WebWidget(QWebEngineView):
    def __init__(self, url="https://google.com"):
        QWebEngineView.__init__(self)
        self.load(QUrl(url))


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.web_widget = WebWidget()
        self.text_edit = QTextEdit()

        self.layout = QGridLayout()
        self.layout.addWidget(self.web_widget)
        self.layout.addWidget(self.text_edit)
        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    web = MainWidget()
    web.show()
    sys.exit(app.exec_())
