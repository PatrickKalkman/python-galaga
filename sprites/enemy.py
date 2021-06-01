import pygame

import constants
import spritesheet

from bezier.bezier_control_point_collection_factory import \
    BezierControlPointCollectionFactory
from bezier.bezier_path_point_calculator import \
    BezierPathPointCalculator


class Enemy(pygame.sprite.Sprite):
    def __init__(self, control_points):
        super(Enemy, self).__init__()
        sprites = spritesheet.SpriteSheet(constants.SPRITE_SHEET)
        self.timer = 0
        self.bezier_timer = 0.0
        self.interval = 2
        self.number_of_images = 7
        self.speed = 1
        self.sprite_index_count = 1
        self.images = sprites.load_strip(
            [0, 199, 48, 40], self.number_of_images)

        self.surf = self.images[0]
        self.rect = self.surf.get_rect(
            center=(constants.SCREEN_WIDTH / 2,
                    constants.SCREEN_HEIGHT - 20))
        self.image_index = 0
        self.control_points = control_points
        self.calculator = BezierPathPointCalculator()

    def get_event(self, event):
        pass


    def update(self, keys):
        self.timer += 1
        self.bezier_timer += 0.006
        if int(self.bezier_timer) > len(self.control_points) - 1:
            self.bezier_timer = 0
        control_point_index = int(self.bezier_timer)
        path_point = self.calculator.calculate_path_point(self.control_points[control_point_index],
                                                          self.bezier_timer)
        self.rect.centerx = path_point.xpos
        self.rect.centery = path_point.ypos

        if self.rect.bottom < 0:
            self.kill()

    def get_surf(self):
        if self.timer % self.interval == 0:
            self.image_index += self.sprite_index_count
            if self.image_index == self.number_of_images - 1 or \
                    self.image_index == 0:
                self.sprite_index_count = -self.sprite_index_count
        return self.images[self.image_index]
