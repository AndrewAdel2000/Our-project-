from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtGui
from Graphic_View import *
from Node_Scene import *
from Draw_Node import  *


class WindowEditor(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.MyUI()

    def MyUI(self):
        self.setGeometry(50, 80, 800, 600)
        self.myLayout = QVBoxLayout()
        self.myLayout.setContentsMargins(0,0,0,0)
        self.setLayout(self.myLayout)

        # create the scene
        self.myScene = Scene()
        #self.myGrScene =self.myScene.myGrScene
        node = Node(self.myScene, "My Awesome Node")
        nodeContent = NodeContent()
        # create the graphic view
        self.view = CrGraphicsView(self.myScene.myGrScene, self)
        self.myLayout.addWidget(self.view)

        self.setWindowIcon(QIcon("C:\\Users\\Asem_\\Desktop\\11.png"))
        self.setWindowTitle("VP")

        self.show()
