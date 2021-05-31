import pygame

import constants
import spritesheet


class Rocket(pygame.sprite.Sprite):
    def __init__(self):
        super(Rocket, self).__init__()
        sprites = spritesheet.SpriteSheet(constants.SPRITE_SHEET)
        self.timer = 0
        self.interval = 2
        self.number_of_images = 3
        self.speed = 10
        self.images = sprites.load_strip(
            [0, 177, 12, 14], self.number_of_images)

        self.surf = self.images[1]
        self.rect = self.surf.get_rect(
            center=(constants.SCREEN_WIDTH / 2,
                    constants.SCREEN_HEIGHT - 20))
        self.image_index = 0

    def update(self, keys):
        self.timer += 1
        self.rect.move_ip(0, -self.speed)

        if self.rect.bottom < 0:
            self.kill()

    def get_event(self, event):
        pass

    def get_surf(self):
        if self.timer % self.interval == 0:
            self.image_index += 1
        if self.image_index >= self.number_of_images:
            self.image_index = 0
        return self.images[self.image_index]
