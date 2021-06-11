import pygame
from pygame.locals import (
    K_LEFT,
    K_RIGHT,
)

import constants


class Player(pygame.sprite.Sprite):
    def __init__(self, sprites):
        super(Player, self).__init__()
        self.timer = 0
        self.interval = 2
        self.number_of_images = 6
        self.images = sprites.load_strip([0, 130, 48, 45], self.number_of_images, -1)
        self.surf = self.images[0]
        self.rect = self.surf.get_rect(center=(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 40))
        self.image_index = 0

    def get_event(self, event):
        pass

    def update(self, pressed_keys):
        self.timer += 1
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > constants.SCREEN_WIDTH:
            self.rect.right = constants.SCREEN_WIDTH

    def get_surf(self):
        if self.timer % self.interval == 0:
            self.image_index += 1
            if self.image_index >= self.number_of_images:
                self.image_index = 0
        return self.images[self.image_index]
