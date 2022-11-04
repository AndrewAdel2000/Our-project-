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
        self.myLayout.setContentsMargins(5, 5, 5, 5)
        self.setLayout(self.myLayout)

        # create the scene
        self.myScene = Scene()

        node = Node(self.myScene, "Node Undefined" , inputs=[1, 2, 3], outputs=[1]) #k

        #self.myGrScene =self.myScene.myGrScene

        # create the graphic view
        self.view = CrGraphicsView(self.myScene.myGrScene,self)
        self.myLayout.addWidget(self.view)

        self.setWindowIcon(QIcon("C:\\Users\\Asem_\\Desktop\\11.png"))
        self.setWindowTitle("VP")

        node = Node(self.myScene, "MY ONLY NODE")

        #self.addDebCont()
        self.show()

    def addDebCont(self):
        greenBrush = QBrush(Qt.green)
        outLinePen = QPen(Qt.black)
        outLinePen.setWidth(2)

        rect = self.myGrScene.addRect(50, 50, 150, 150, outLinePen, greenBrush)
        rect.setFlag(QGraphicsItem.ItemIsMovable)

        text = self.myGrScene.addText("HELLO")
