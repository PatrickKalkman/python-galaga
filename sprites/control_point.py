from bezier.control_point_handler import ControlPointHandler
import pygame


class ControlPoint(pygame.sprite.Sprite):
    def __init__(self, x, y, color, cp_index,
                 p_index, control_points,
                 control_handler_mover: ControlPointHandler):
        super(ControlPoint, self).__init__()

        self.control_points = control_points
        self.cp_index = cp_index
        self.p_index = p_index
        self.control_handler_mover = control_handler_mover
        self.original_image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(self.original_image, color, (25, 25), 20)
        self.selected_image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(self.selected_image, color, (25, 25), 25)
        pygame.draw.circle(self.selected_image, (255, 255, 255), (25, 25), 25, 4)
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(x, y))
        self.selected = False

    def get_event(self, event):
        pass

    def update(self, keys):
        mouse_pos = pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_pressed()
        self.selected = self.rect.collidepoint(
            mouse_pos) and any(mouse_buttons)
        self.image = self.selected_image if self.selected else self.original_image

        if self.selected:
            self.rect = self.image.get_rect(
                center=(mouse_pos[0], mouse_pos[1]))
            self.control_handler_mover.move_control_handler(
                ControlPointHandler(self.cp_index, self.p_index),
                mouse_pos[0], mouse_pos[1])
        else:
            self.x = self.control_points.get_quartet(
                self.cp_index).get_point(self.p_index).x
            self.y = self.control_points.get_quartet(
                self.cp_index).get_point(self.p_index).y
            self.rect = self.image.get_rect(center=(self.x, self.y))

    def get_surf(self):
        return self.image
