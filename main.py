import sys
import pygame

from states.menu import Menu
from states.gameplay import Gameplay
from states.game_over import GameOver
from states.splash import Splash
from game import Game
import constants

pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((constants.SCREEN_WIDTH,
                                  constants.SCREEN_HEIGHT))
states = {
    "MENU": Menu(),
    "SPLASH": Splash(),
    "GAMEPLAY": Gameplay(),
    "GAME_OVER": GameOver(),
}

game = Game(screen, states, "GAMEPLAY")
game.run()

pygame.quit()
sys.exit()
