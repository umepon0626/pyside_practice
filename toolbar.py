from PySide2.QtWidgets import (QLineEdit, QPushButton, QToolBar)
class Browser_Toolbar(QToolBar):
    def __init__(self):
        QToolBar.__init__(self)
        self.back = QPushButton("back")
        self.next = QPushButton("next")
        self.reload = QPushButton("reload")
        self.url_box = QLineEdit(self)
        self.url_box.setClearButtonEnabled(True)
        
        self.addWidget(self.back)
        self.addWidget(self.next)
        self.addWidget(self.reload)
        self.addWidget(self.url_box)