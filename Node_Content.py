from PyQt5.QtWidgets import *

class NodeContent():
    def __int__(self,parent=None):
        super().__init__(parent)

        self.initUI()

    def initUI(self):
        self.myLayout = QVBoxLayout()
        self.myLayout.setContentsMargins(0,0,0,0)
        self.setLayout(self.myLayout)

        self.nLabel = QLabel("some title")
        self.myLayout.addWidget(self.nLabel)
        self.myLayout.addWidget(QTextEdit("fool"))
