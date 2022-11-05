from Graphics_Socket import *

LEFT_TOP = 1
LEFT_BOTTOM = 2
RIGHT_TOP = 3
RIGHT_BOTTOM = 4


class Socket():
    def __init__(self, node, index=0, position=LEFT_TOP):
        self.position = LEFT_TOP
        self.node = node
        self.index = index

        self.grSockets = QDMGraphicSocket(self.node.grNode)
        self.grSockets.setPos(*self.node.getSocketPosition(index, position))

        def setConnectedEdge(self, edge=None):
            self.edge = edge
            self.edge = edge

        def hasEdge(self):
            return self.edge is not None

