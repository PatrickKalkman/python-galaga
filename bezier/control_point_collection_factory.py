from .control_point_quartet import ControlPointQuartet
from .control_point_quartet_collection import ControlPointQuartetCollection


class ControlPointCollectionFactory():

    @staticmethod
    def create_demo_collection():
        control_point_quartet_collection = ControlPointQuartetCollection()

        control_point_quartet_collection.add(ControlPointQuartet(
            585, 20,
            317, 20,
            878, 654,
            516, 654))

        control_point_quartet_collection.add(ControlPointQuartet(
            516, 654,
            154, 654,
            853, 240,
            616, 454))

        control_point_quartet_collection.add(ControlPointQuartet(
            616, 454,
            154, 654,
            853, 20,
            585, 20))

        return control_point_quartet_collection
