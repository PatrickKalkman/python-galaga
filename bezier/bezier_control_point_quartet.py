from .bezier_control_point import BezierControlPoint


class BezierControlPointQuartet():
    def __init__(self,
                 x0, y0,
                 x1, y1,
                 x2, y2,
                 x3, y3):

        self.points = []
        self.points.append(BezierControlPoint(x0, y0))
        self.points.append(BezierControlPoint(x1, y1))
        self.points.append(BezierControlPoint(x2, y2))
        self.points.append(BezierControlPoint(x3, y3))

    def get(self, control_point_index):
        return self.points[control_point_index]
