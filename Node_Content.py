from PyQt5.QtWidgets import *


class NodeContent(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.layout)

        self.wdg_label = QLabel("Some Title")
        self.layout.addWidget(self.wdg_label)
        self.layout.addWidget(QTextEdit("foo"))



        '''
        self.myLayout = QVBoxLayout()
        self.myLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.myLayout)
        .addLayout(grid)
        self.nLabel = QLabel("some title")
        self.myLayout.addWidget(self.nLabel)
        self.myLayout.addWidget(QTextEdit("fool"))
        self.show()
        '''
