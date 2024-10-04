import sys

import pygame
from settings import SCREEN_HEIGHT, SCREEN_WIDTH


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
        pygame.display.set_caption('Sprout land')
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
