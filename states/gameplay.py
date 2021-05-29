import pygame
from .base import BaseState
from sprites.player import Player
from sprites.rocket import Rocket
from sprites.enemy import Enemy


class Gameplay(BaseState):
    def __init__(self):
        super(Gameplay, self).__init__()
        self.rect = pygame.Rect((0, 0), (80, 80))
        self.next_state = "GAME_OVER"
        self.player = Player()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)
        self.shoot_sound = pygame.mixer.Sound(
            "./assets/sounds/13 Fighter Shot1.mp3")
        enemy = Enemy()
        self.all_sprites.add(enemy)
        pygame.mixer.music.load('./assets/sounds/02 Start Music.mp3')
        pygame.mixer.music.play()

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                self.done = True
            if event.key == pygame.K_SPACE:
                # check if the sprite group already contains two rockets
                rocket_count = 0
                for sprite in self.all_sprites.sprites():
                    if (isinstance(sprite, Rocket)):
                        rocket_count += 1

                if rocket_count < 2:
                    self.rocket = Rocket()
                    self.rocket.rect.centerx = self.player.rect.centerx
                    self.all_sprites.add(self.rocket)
                    self.shoot_sound.play()

    def draw(self, screen):
        pressed_keys = pygame.key.get_pressed()
        for entity in self.all_sprites:
            entity.update(pressed_keys)

        for entity in self.all_sprites:
            screen.blit(entity.get_surf(), entity.rect)
