from .bezier_control_point import BezierControlPoint


class BezierControlPointQuartet():
    def __init__(self,
                 x0, y0,
                 x1, y1,
                 x2, y2,
                 x3, y3):

        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

        self.point = []
        self.point.append(BezierControlPoint(x0, y0))
        self.point.append(BezierControlPoint(x1, y1))
        self.point.append(BezierControlPoint(x2, y2))
        self.point.append(BezierControlPoint(x3, y3))

    def get(self, control_point_index):
        return self.point[control_point_index]
