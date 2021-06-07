import pygame
import math
from .base import BaseState
from sprites.player import Player
from sprites.rocket import Rocket
from sprites.enemy import Enemy
from sprites.control_point import ControlPoint

from bezier.control_point_collection_factory import ControlPointCollectionFactory
from bezier.path_point_calculator import PathPointCalculator
from bezier.control_handler_mover import ControlHandlerMover
from bezier.path_point_selector import PathPointSelector

ADDENEMY = pygame.USEREVENT + 1


class Gameplay(BaseState):
    def __init__(self):
        super(Gameplay, self).__init__()
        self.rect = pygame.Rect((0, 0), (80, 80))
        self.next_state = "GAME_OVER"
        self.control_points = ControlPointCollectionFactory.create_demo_collection()
        self.path_point_selector = PathPointSelector(self.control_points)
        self.path_point_selector.create_path_point_mapping()
        self.mover = ControlHandlerMover(self.control_points, self.path_point_selector)
        self.control_sprites = pygame.sprite.Group()
        self.add_control_points()
        self.player = Player()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

        self.all_enemies = pygame.sprite.Group()
        self.enemy = Enemy(self.control_points)
        self.all_enemies.add(self.enemy)
        self.all_sprites.add(self.enemy)
        self.rocket = Rocket()
        self.all_rockets = pygame.sprite.Group()
        self.shoot_sound = pygame.mixer.Sound(
            "./assets/sounds/13 Fighter Shot1.mp3")
        pygame.mixer.music.load('./assets/sounds/02 Start Music.mp3')
        pygame.mixer.music.play()
        self.show_control = False
        self.mover.align_all()

    def add_control_points(self):
        for quartet_index in range(self.control_points.number_of_quartets()):
            for point_index in range(3):
                quartet = self.control_points.get_quartet(quartet_index)
                point = quartet.get_point(point_index)
                x = point.x
                y = point.y
                self.control_sprites.add(ControlPoint(
                    x, y, (255, 120, 120), quartet_index, point_index,
                    self.control_points, self.mover))

    def get_event(self, event):
        for entity in self.all_sprites:
            entity.get_event(event)

        if event.type == pygame.QUIT:
            self.quit = True
        if event.type == ADDENEMY:
            enemy = Enemy(self.control_points)
            self.all_enemies.add(enemy)
            self.all_sprites.add(enemy)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                self.control_points.save_control_points()
                self.done = True
            if event.key == pygame.K_s:
                self.show_control = not self.show_control
            if event.key == pygame.K_SPACE:
                # check if the sprite group already contains two rockets
                rocket_count = 0
                for sprite in self.all_sprites.sprites():
                    if (isinstance(sprite, Rocket)):
                        rocket_count += 1

                if rocket_count < 2:
                    self.rocket = Rocket()
                    self.rocket.rect.centerx = self.player.rect.centerx
                    self.all_rockets.add(self.rocket)
                    self.all_sprites.add(self.rocket)
                    self.shoot_sound.play()

    def draw(self, screen):
        pressed_keys = pygame.key.get_pressed()
        for entity in self.all_sprites:
            entity.update(pressed_keys)

        for entity in self.control_sprites:
            entity.update(pressed_keys)

        for entity in self.all_sprites:
            screen.blit(entity.get_surf(), entity.rect)

        if self.show_control:
            for entity in self.control_sprites:
                screen.blit(entity.get_surf(), entity.rect)

            self.drawPath(screen)
            self.draw_control_lines(screen)

        pygame.sprite.groupcollide(self.all_rockets, self.all_enemies, True, True)

    def drawPath(self, screen):
        calculator = PathPointCalculator()
        bezier_timer = 0
        previous_path_point = None
        while bezier_timer < self.control_points.number_of_quartets():
            control_point_index = int(bezier_timer)
            path_point = calculator.calculate_path_point(self.control_points.get_quartet(control_point_index), bezier_timer)
            if previous_path_point is None:
                previous_path_point = path_point

            pygame.draw.line(screen, (255, 255, 255), (previous_path_point.xpos, previous_path_point.ypos), (path_point.xpos, path_point.ypos))
            previous_path_point = path_point
            bezier_timer += 0.005

    def draw_control_lines(self, screen):
        for pair in self.path_point_selector.get_control_point_pairs():
            pygame.draw.line(screen, (255, 255, 255), pair[0], pair[1])
