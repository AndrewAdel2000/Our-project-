from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class QDMGraphicSocket(QGraphicsItem):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.radius = 6
        self.outline_width = 5
        self._color_background = QColor("#4A5568")
        self._color_outline = QColor("#FF000000")

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
