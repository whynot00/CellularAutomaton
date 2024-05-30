import pygame
from gamefield import GameField
from events import events

class MainWindow:

    def __init__(self):

        pygame.init()
        pygame.display.set_caption('Клеточный автомат')

        self.screen = pygame.display.set_mode((1100, 1100))
        self.screen.fill((112,112,112))

    def main_loop(self):

        gamefield = GameField(self.screen)

        gamefield.set_rules([3], [2,3])

        # gamefield.set_cell_size(10)
        # gamefield.set_game_speed(1)

        gamefield.init()

        # gamefield.set_random(100, 40)

        events(gamefield)

    
game = MainWindow()

game.main_loop()
