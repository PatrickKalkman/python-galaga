from .bezier_control_point_quartet import BezierControlPointQuartet


class BezierControlPointCollectionFactory():

    @staticmethod
    def create_demo_collection():
        bezier_point_quartet_collection = []

        bezier_point_quartet_collection.append(BezierControlPointQuartet(
            189, 119,
            56, 17,
            203, 254,
            240, 364
        ))

        bezier_point_quartet_collection.append(BezierControlPointQuartet(
            240, 364,
            259, 504,
            299, 504,
            189, 119,
        ))

        return bezier_point_quartet_collection

# The basic tricks in getting this to be a smooth curve across the whole path is to:
# p3 of the each segment is in common to p0 of next each segment.
# To make the circular, p3 of last segment must be same as p0 of 1st segment.
# p2 and p3 of each segment must be on a strait line with p0 and p1 or the next segment. So this means 