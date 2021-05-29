import pygame

import constants
import spritesheet


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        sprites = spritesheet.SpriteSheet(constants.SPRITE_SHEET)
        self.timer = 0
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

    def update(self, keys):
        self.timer += 1
        self.rect.move_ip(0, -self.speed)

        if self.rect.bottom < 0:
            self.kill()

    def get_surf(self):
        if self.timer % self.interval == 0:
            self.image_index += self.sprite_index_count
            if self.image_index == self.number_of_images - 1 or self.image_index == 0:
                self.sprite_index_count = -self.sprite_index_count
        return self.images[self.image_index]
