from .bezier_control_point_quartet import BezierControlPointQuartet
from .bezier_path_point import BezierPathPoint


class BezierPathPointCalculator():

    @staticmethod
    def calculate_path_point(bezier_control_point_quartet:
                             BezierControlPointQuartet, time_to_calculate: float):
        time: float = time_to_calculate - int(time_to_calculate)

        cx: float = 3.0 * (bezier_control_point_quartet.get(1).x - bezier_control_point_quartet.get(0).x)
        cy: float = 3.0 * (bezier_control_point_quartet.get(1).y - bezier_control_point_quartet.get(0).y)

        bx: float = 3.0 * (bezier_control_point_quartet.get(2).x - bezier_control_point_quartet.get(1).x) - cx
        by: float = 3.0 * (bezier_control_point_quartet.get(2).y - bezier_control_point_quartet.get(1).y) - cy

        ax: float = bezier_control_point_quartet.get(3).x - bezier_control_point_quartet.get(0).x - cx - bx
        ay: float = bezier_control_point_quartet.get(3).y - bezier_control_point_quartet.get(0).y - cy - by

        cube: float = time * time * time
        square: float = time * time

        resx: float = (ax * cube) + (bx * square) + (cx * time) + bezier_control_point_quartet.get(0).x
        resy: float = (ay * cube) + (by * square) + (cy * time) + bezier_control_point_quartet.get(0).y

        return BezierPathPoint(resx, resy)
