from .control_point_quartet import ControlPointQuartet
from .control_point_quartet_collection import ControlPointQuartetCollection


class ControlPointCollectionFactory():

    @staticmethod
    def create_demo_collection():
        control_point_quartet_collection = ControlPointQuartetCollection()

        control_point_quartet_collection.add(ControlPointQuartet(
            768, 121,
            494, 125,
            1193, 858,
            771, 853))

        control_point_quartet_collection.add(ControlPointQuartet(
            771, 853,
            349, 848,
            1042, 117,
            768, 121))

        return control_point_quartet_collection
