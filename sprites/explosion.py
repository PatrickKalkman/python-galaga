import pygame
import constants
import spritesheet


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Explosion, self).__init__()
        sprites = spritesheet.SpriteSheet(constants.SPRITE_SHEET_EXPLOSION)
        self.timer = 0
        self.interval = 2
        self.number_of_images = 6
        self.images = sprites.load_strip([0, 130, 48, 45], self.number_of_images)
        self.surf = self.images[0]
        self.rect = self.surf.get_rect(center=(x, y))
        self.image_index = 0

    def get_event(self, event):
        pass

    def update(self, pressed_keys):
        self.timer += 1

    def get_surf(self):
        if self.timer % self.interval == 0:
            self.image_index += 1
            if self.image_index >= self.number_of_images:
                self.image_index = 0
        return self.images[self.image_index]
