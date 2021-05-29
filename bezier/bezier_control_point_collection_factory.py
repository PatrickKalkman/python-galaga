from .bezier_control_point_quartet import BezierControlPointQuartet


class BezierControlPointCollectionFactory():

    @staticmethod
    def create_demo_collection():
        bezier_point_quartet_collection = []

        bezier_point_quartet_collection.append(BezierControlPointQuartet(
            400.0, 119.0,
            560.0, 17.0,
            1599.0, 254.0,
            240.0, 364.0
        ))

        bezier_point_quartet_collection.append(BezierControlPointQuartet(
            240.0, 364.0,
            259.0, 504.0,
            1599.0, 604.0,
            400.0, 119.0,
        ))

        bezier_point_quartet_collection.append(BezierControlPointQuartet(
            400.0, 119.0,
            159.0, 304.0,
            199.0, 304.0,
            139.0, 264.0
        ))

        bezier_point_quartet_collection.append(BezierControlPointQuartet(
            139.0, 264.0,
            259.0, 204.0,
            299.0, 204.0,
            40.0, 164.0
        ))

        bezier_point_quartet_collection.append(BezierControlPointQuartet(
            40.0, 164.0,
            259.0, 1204.0,
            399.0, 154.0,
            400.0, 119.0
        ))

        return bezier_point_quartet_collection
