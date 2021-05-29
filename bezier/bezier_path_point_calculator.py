from .bezier_control_point_quartet import BezierControlPointQuartet
from .bezier_path_point import BezierPathPoint


class BezierPathPointCalculator():

    @staticmethod
    def calculate_path_point(bezier_control_point_quartet:
                             BezierControlPointQuartet, time_to_calculate: float):
        time: float = time_to_calculate - int(time_to_calculate)

        cx: float = 3.0 * (bezier_control_point_quartet.x1 - bezier_control_point_quartet.x0)
        cy: float = 3.0 * (bezier_control_point_quartet.y1 - bezier_control_point_quartet.y0)

        bx: float = 3.0 * (bezier_control_point_quartet.x2 - bezier_control_point_quartet.x1) - cx
        by: float = 3.0 * (bezier_control_point_quartet.y2 - bezier_control_point_quartet.y1) - cy

        ax: float = bezier_control_point_quartet.x3 - bezier_control_point_quartet.x0 - cx - bx
        ay: float = bezier_control_point_quartet.y3 - bezier_control_point_quartet.y0 - cy - by

        cube: float = time * time * time
        square: float = time * time

        resx: float = (ax * cube) + (bx * square) + (cx * time) + \
            bezier_control_point_quartet.x0
        resy: float = (ay * cube) + (by * square) + (cy * time) + \
            bezier_control_point_quartet.y0

        return BezierPathPoint(resx, resy)
