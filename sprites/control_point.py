import pygame


class ControlPoint(pygame.sprite.Sprite):
    def __init__(self, x, y, color, cp_index, p_index):
        super(ControlPoint, self).__init__()
        self.cp_index = cp_index
        self.p_index = p_index
        self.original_image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(self.original_image, color, (25, 25), 20)
        self.selected_image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(self.selected_image, color, (25, 25), 25)
        pygame.draw.circle(self.selected_image,
                           (255, 255, 255), (25, 25), 25, 4)
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(x, y))
        self.selected = False

    def get_event(self, event):
        pass

    def update(self, keys, control_points):
        mouse_pos = pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_pressed()
        self.selected = self.rect.collidepoint(
            mouse_pos) and any(mouse_buttons)
        self.image = self.selected_image if self.selected else self.original_image

        if self.selected:
            self.rect = self.image.get_rect(
                center=(mouse_pos[0], mouse_pos[1]))
            control_points[self.cp_index].points[self.p_index].x = mouse_pos[0]
            control_points[self.cp_index].points[self.p_index].y = mouse_pos[1]

        # return control_points

    def get_surf(self):
        return self.image
