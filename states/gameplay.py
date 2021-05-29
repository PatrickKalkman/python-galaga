import pygame
from .base import BaseState
from sprites.player import Player
from sprites.rocket import Rocket


class Gameplay(BaseState):
    def __init__(self):
        super(Gameplay, self).__init__()
        self.rect = pygame.Rect((0, 0), (80, 80))
        self.next_state = "GAME_OVER"
        self.player = Player()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                self.done = True
            if event.key == pygame.K_SPACE:
                self.rocket = Rocket()
                self.rocket.rect.centerx = self.player.rect.centerx
                self.all_sprites.add(self.rocket)

    def draw(self, screen):
        pressed_keys = pygame.key.get_pressed()
        for entity in self.all_sprites:
            entity.update(pressed_keys)

        for entity in self.all_sprites:
            screen.blit(entity.get_surf(), entity.rect)
