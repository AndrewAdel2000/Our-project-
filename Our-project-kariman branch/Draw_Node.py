from Graphics_Node import *
from Node_Content import *
from socket import *
class Node():
    def __init__(self, scene, title="Node Undefined",inputs=[],outputs=[]): #k

        self.scene = scene

        self.title = title

        self.content = NodeContent()
        self.grNode = GraphicsNode(self)

        self.scene.addNode(self)
        self.scene.myGrScene.addItem(self.grNode)

        self.inputs = []
        self.outputs = []
        #k
        counter = 0
        for item in inputs:
            socket = Socket(node=self, index=counter, position=LEFT_TOP)
            counter += 1
            self.inputs.append(socket)

        counter = 0
        for item in outputs:
            socket = Socket(node=self, index=counter, position=RIGHT_TOP)
            counter += 1
            self.outputs.append(socket)

    def getSocketPosition(self, index, position):
        x = 0 if (position in (LEFT_TOP,LEFT_BOTTOM)) else self.grNode.width
        y = self.grNode.title_height + self.grNode.edge_padding + index * 22

        return x, y




