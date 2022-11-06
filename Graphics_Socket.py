from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class QDMGraphicSocket(QGraphicsItem):
    def __init__(self, parent=None, socket_type=1):
        super().__init__(parent)

        self.radius = 6
        self.outline_width = 0
        self._color_background = QColor("#ED8936")
        self._color_outline = QColor("#ED8936")

        # self._colors = [
        #     QColor("#FFFFFFFF"),
        #     QColor("#FFFFFFFF"),
        #     QColor("#FF0056a6"),
        #     QColor("#FFa86db1"),
        #     QColor("#FFb54747"),
        #     QColor("#FFdbe220"),
        # ]
        #self._color_background = self._colors[socket_type]

        self._pen = QPen(self._color_outline)
        self._brush = QBrush(self._color_background)
        self._pen.setWidthF(self.outline_width)

    def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
        # painting circle
        painter.setBrush(self._brush)
        painter.setPen(self._pen)
        painter.drawEllipse(-self.radius, -self.radius, 2 * self.radius, 2 * self.radius)

    def boundingRect(self):
        return QRectF(
            - self.radius - self.outline_width,
            - self.radius - self.outline_width,
            2 * (self.radius + self.outline_width),
            2 * (self.radius + self.outline_width),
        )

