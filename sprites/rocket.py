import math
import pygame
import constants


class Rocket(pygame.sprite.Sprite):
    def __init__(self, sprites, xSpeed, ySpeed):
        super(Rocket, self).__init__()
        self.timer = 0
        self.interval = 2
        self.number_of_images = 3
        self.ySpeed = ySpeed
        self.xSpeed = xSpeed
        self.images = sprites.load_strip([0, 177, 12, 14], self.number_of_images, -1)

        self.surf = self.images[1]
        self.rect = self.surf.get_rect(
            center=(constants.SCREEN_WIDTH / 2,
                    constants.SCREEN_HEIGHT - 20))
        self.image_index = 0
        self.rotation = 0
        if self.ySpeed > 0:
            self.rotation = math.degrees(math.atan2(xSpeed, ySpeed)) + 180

    def update(self, keys):
        self.timer += 1
        self.rect.move_ip(self.xSpeed, self.ySpeed)

        if self.rect.bottom < 0 or self.rect.top > constants.SCREEN_HEIGHT:
            self.kill()

    def get_event(self, event):
        pass

    def get_surf(self):
        if self.timer % self.interval == 0:
            self.image_index += 1
        if self.image_index >= self.number_of_images:
            self.image_index = 0

        rot_image = pygame.transform.rotate(self.images[self.image_index], self.rotation)
        self.rect = rot_image.get_rect(center=self.rect.center)

        return rot_image
