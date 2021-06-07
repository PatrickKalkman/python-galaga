from .control_point_quartet import ControlPointQuartet
from .control_point_quartet_collection import ControlPointQuartetCollection


class ControlPointCollectionFactory():

    @staticmethod
    def create_demo_collection():
        control_point_quartet_collection = ControlPointQuartetCollection()

        control_point_quartet_collection.add(ControlPointQuartet(
            785, -40,
            517, -40,
            1329, 906,
            801, 903))
            
        control_point_quartet_collection.add(ControlPointQuartet(
            801, 903,
            273, 900,
            1053, -40,
            785, -40))

        return control_point_quartet_collection
