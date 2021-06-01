import pygame
from .base import BaseState
from sprites.player import Player
from sprites.rocket import Rocket
from sprites.enemy import Enemy
from sprites.control_point import ControlPoint


from bezier.bezier_control_point_collection_factory import \
    BezierControlPointCollectionFactory
from bezier.bezier_path_point_calculator import \
    BezierPathPointCalculator


class Gameplay(BaseState):
    def __init__(self):
        super(Gameplay, self).__init__()
        self.rect = pygame.Rect((0, 0), (80, 80))
        self.next_state = "GAME_OVER"
        self.control_points = BezierControlPointCollectionFactory.create_demo_collection()
        self.control_sprites = pygame.sprite.Group()
        self.add_control_points()
        self.player = Player()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)
        enemy = Enemy(self.control_points)
        self.all_sprites.add(enemy)
        self.shoot_sound = pygame.mixer.Sound(
            "./assets/sounds/13 Fighter Shot1.mp3")
        pygame.mixer.music.load('./assets/sounds/02 Start Music.mp3')
        pygame.mixer.music.play()

    def add_control_points(self):
        for quartet_index in range(len(self.control_points)):
            for point_index in range(3):
                x = self.control_points[quartet_index].get(point_index).x
                y = self.control_points[quartet_index].get(point_index).y
                self.control_sprites.add(ControlPoint(x, y, (255, 120, 120), quartet_index, point_index))

    def get_event(self, event):
        for entity in self.all_sprites:
            entity.get_event(event)

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

        for entity in self.control_sprites:
            entity.update(pressed_keys, self.control_points)
            x = self.control_points[entity.cp_index].get(entity.p_index).x
            y = self.control_points[entity.cp_index].get(entity.p_index).y
            #print(f'{x}, {y}')

        for entity in self.all_sprites:
            screen.blit(entity.get_surf(), entity.rect)

        for entity in self.control_sprites:
            screen.blit(entity.get_surf(), entity.rect)

        self.drawPath(screen)
        self.draw_control_lines(screen)

    def drawPath(self, screen):
        calculator = BezierPathPointCalculator()
        bezier_timer = 0
        previous_path_point = None
        while bezier_timer < len(self.control_points):
            control_point_index = int(bezier_timer)
            path_point = calculator.calculate_path_point(self.control_points[control_point_index],
                                                         bezier_timer)
            if previous_path_point is None:
                previous_path_point = path_point

            pygame.draw.line(screen, (255, 255, 255),
                             (previous_path_point.xpos, previous_path_point.ypos),
                             (path_point.xpos, path_point.ypos))
            previous_path_point = path_point
            bezier_timer += 0.005

    def draw_control_lines(self, screen):
        lines = []

        lines.append(
            ((self.control_points[0].get(1).x,
              self.control_points[0].get(1).y),
             (self.control_points[-1].get(2).x,
              self.control_points[-1].get(2).x)))

        for index in range(0, len(self.control_points), 2):
            lines.append(
                ((self.control_points[index].get(2).x,
                  self.control_points[index].get(2).y),
                 (self.control_points[index+1].get(1).x,
                  self.control_points[index+1].get(1).y)))

        for line in lines:
            pygame.draw.line(screen, (255, 255, 255), (line[0]), (line[1]))
