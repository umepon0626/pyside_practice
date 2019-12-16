import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import (QApplication,QMainWindow, QToolBar)
from PySide2.QtWebEngineWidgets import QWebEngineView
from toolbar import Browser_Toolbar


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("tutorial")
        self._page = page()
        self._page.resize(800,500)
        self._page.load(self._page.initial_url)
        self._page.loadStarted.connect(lambda :self.toolbar.url_box.setText(self._page.url().url()))
        self.toolbar = Browser_Toolbar()

        self.toolbar.url_box.returnPressed.connect(lambda :self._page.setUrl(self.toolbar.url_box.text()))
        self.toolbar.reload.clicked.connect(lambda :self._page.reload())
        self.toolbar.back.clicked.connect(lambda :self._page.back())
        self.toolbar.next.clicked.connect(lambda :self._page.forward())

        self.addToolBar(Qt.TopToolBarArea,self.toolbar)
        self.setCentralWidget(self._page)

        
    
class page(QWebEngineView):
    def __init__(self):
        QWebEngineView.__init__(self)
        self.initial_url = "https://www.rutilea.com/"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

