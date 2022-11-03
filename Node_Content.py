from PyQt5.QtWidgets import *


class NodeContent(QWidget):
    def __int__(self, parent=None):
        super().__init__(parent)

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        vbox.addLayout()
        label = QLabel("This is a label")
        vbox.addWidget(label)
        self.setLayout(vbox)
        self.show()
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
