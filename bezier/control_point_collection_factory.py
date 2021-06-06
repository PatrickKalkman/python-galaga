from .control_point_quartet import ControlPointQuartet
from .control_point_quartet_collection import ControlPointQuartetCollection


class ControlPointCollectionFactory():

    @staticmethod
    def create_demo_collection():
        control_point_quartet_collection = ControlPointQuartetCollection()

        control_point_quartet_collection.add(ControlPointQuartet(
            189, 119,
            56, 17,
            203, 254,
            240, 364
        ))

        control_point_quartet_collection.add(ControlPointQuartet(
            240, 364,
            259, 504,
            299, 504,
            189, 119,
        ))

        return control_point_quartet_collection
