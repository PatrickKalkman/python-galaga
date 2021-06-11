
import pygame
import random
import constants

WHITE = (255, 255, 255)
LIGHTGREY = (120, 120, 120)
DARKGREY = (100, 100, 100)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (120, 120, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)


class StarField():
    def __init__(self):
        # create the locations of the stars for when we animate the background
        self.star_field_slow = []
        self.star_field_medium = []
        self.star_field_fast = []

        for slow_stars in range(50):
            star_loc_x = random.randrange(0, constants.SCREEN_WIDTH)
            star_loc_y = random.randrange(0, constants.SCREEN_HEIGHT)
            self.star_field_slow.append([star_loc_x, star_loc_y])

        for medium_stars in range(35):
            star_loc_x = random.randrange(0, constants.SCREEN_WIDTH)
            star_loc_y = random.randrange(0, constants.SCREEN_HEIGHT)
            self.star_field_medium.append([star_loc_x, star_loc_y])

        for fast_stars in range(30):
            star_loc_x = random.randrange(0, constants.SCREEN_WIDTH)
            star_loc_y = random.randrange(0, constants.SCREEN_HEIGHT)
            self.star_field_fast.append([star_loc_x, star_loc_y])

    def render(self, screen):
        for star in self.star_field_slow:
            star[1] += 1
            if star[1] > constants.SCREEN_HEIGHT:
                star[0] = random.randrange(0, constants.SCREEN_WIDTH)
                star[1] = random.randrange(-20, -5)
            pygame.draw.circle(screen, DARKGREY, star, 3)

        for star in self.star_field_medium:
            star[1] += 4
            if star[1] > constants.SCREEN_HEIGHT:
                star[0] = random.randrange(0, constants.SCREEN_WIDTH)
                star[1] = random.randrange(-20, -5)
            pygame.draw.circle(screen, LIGHTGREY, star, 2)

        for star in self.star_field_fast:
            star[1] += 8
            if star[1] > constants.SCREEN_HEIGHT:
                star[0] = random.randrange(0, constants.SCREEN_WIDTH)
                star[1] = random.randrange(-20, -5)
            pygame.draw.circle(screen, YELLOW, star, 1)
