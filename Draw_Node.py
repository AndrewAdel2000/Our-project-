from Graphics_Node import *
from Node_Content import *

class Node():
    def __init__(self, scene, title="Node Undefined"):

        self.scene = scene

        self.title = title

        self.content = NodeContent()
        self.content = NodeContent()
        self.grNode = GraphicsNode(self)

        self.scene.addNode(self)
        self.scene.myGrScene.addItem(self.grNode)

        self.input = []
        self.output = []