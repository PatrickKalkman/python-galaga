from .control_point_quartet import ControlPointQuartet
from .control_point_handler import ControlPointHandler


class ControlPointQuartetCollection():
    def __init__(self):
        self.control_point_quartets = []

    def add(self, controlPointQuartet: ControlPointQuartet):
        self.control_point_quartets.append(controlPointQuartet)

    def number_of_quartets(self):
        return len(self.control_point_quartets)

    def get_quartet(self, quartet_index):
        return self.control_point_quartets[quartet_index]

    def get_quartet_from_time(self, time: float):
        return self.control_point_quartets[int(time)]

    def give_position_is_inside_control_point(self, x, y, image_width):
        for quartet_index in range(len(self.control_point_quartets)):
            result = self.control_point_quartets[quartet_index].is_in_control_point(
                x, y, image_width)
            if result[0]:
                return (quartet_index, result[1], True)

        return (-1, -1, False)

    def get_control_point(self, control_point_handler: ControlPointHandler):
        quartet_index = control_point_handler.quartet_index
        control_point_index = control_point_handler.control_point_index
        return self.control_point_quartets[quartet_index].points[control_point_index]

    def save_control_points(self):
        print('saving')
        with open('control_points.txt', 'w') as file:
            for quartet in self.control_point_quartets:
                file.write('\n    control_point_quartet_collection.add(ControlPointQuartet(')
                for point in quartet.points:
                    file.write(f'\n        {point.x},{point.y},')
                file.write('))')
