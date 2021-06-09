from .control_point_quartet import ControlPointQuartet
from .control_point_quartet_collection import ControlPointQuartetCollection


class ControlPointCollectionFactory():

    @staticmethod
    def create_collection1():
        control_point_quartet_collection = ControlPointQuartetCollection()

        control_point_quartet_collection.add(ControlPointQuartet(
            513, -15,
            565, 16,
            863, 656,
            516, 654))

        control_point_quartet_collection.add(ControlPointQuartet(
            516, 654,
            169, 652,
            676, 535,
            528, 393))

        control_point_quartet_collection.add(ControlPointQuartet(
            528, 393,
            380, 251,
            461, 14,
            513, -15))

        return control_point_quartet_collection

    def create_collection2():
        control_point_quartet_collection = ControlPointQuartetCollection()

        control_point_quartet_collection.add(ControlPointQuartet(
            513, -15,
            430, 11,
            204, 659,
            516, 654))

        control_point_quartet_collection.add(ControlPointQuartet(
            516, 654,
            828, 649,
            420, 388,
            525, 375))
            
        control_point_quartet_collection.add(ControlPointQuartet(
            525, 375,
            630, 362,
            596, -41,
            513, -15))

        return control_point_quartet_collection
