import pygame, time

class RectCell:

    def __init__(self, screen, coords: tuple):

        self.is_live = False
        self.live_count = 0

        self.screen = screen

        self.font_size = 13
        self.font = pygame.font.SysFont('Arial', self.font_size)

        self.color_pressed = (0, 80, 130)
        self.color_default = (245, 245, 245)

        self.x, self.y, self.width, self.height = coords

        self.rectangle = pygame.draw.rect(self.screen, self.color_default, (self.x, self.y, self.width, self.height))

    def set_live(self):
        if not self.is_live:
            self.is_live = True
            self.rectangle = pygame.draw.rect(self.screen, self.color_pressed, self.rectangle)

        else:
            self.is_live = False
            self.rectangle = pygame.draw.rect(self.screen, self.color_default, self.rectangle)

    def create_live(self):
        self.is_live = True
        self.rectangle = pygame.draw.rect(self.screen, self.color_pressed, self.rectangle)

    def delete_live(self):
        self.is_live = False
        self.rectangle = pygame.draw.rect(self.screen, self.color_default, self.rectangle)

    def set_zeroing(self):
        self.live_count = 0

    def __add__(self, value):
        self.live_count += value
        return self

class GameField:

    def __init__(self, screen):

        self.screen = screen
        self.screen_size = self.screen.get_size()

        self.set_game_speed()

        self.width = self.height = 10
        self.margin = 1

        self.set_rules()

    def init(self):

        self.cell_count_height = int(self.screen_size[1] // (self.height + self.margin / 2))
        self.cell_count_width = int(self.screen_size[0] // (self.width + self.margin / 2))
        self.gamefield_lst = [[] for x in range(self.cell_count_height)]

        for row in range(self.cell_count_height):
            for col in range(self.cell_count_width):
                x = row * self.width + (row + 1) * self.margin
                y = col * self.height + (col + 1) * self.margin
                self.gamefield_lst[col].append(RectCell(self.screen, (x, y, self.width, self.height)))

        pygame.display.update()

    def set_rules(self, B=[3], S=[2,3]):

        if type(B) != list or type(S) != list:
            raise ValueError("Правила должны быть в списках.")
        
        self.rules = (B, S)

    def set_cell_size(self, size=10):

        self.width = self.height = size

    def set_game_speed(self, speed=1):
        
        self.game_speed = 0.1 / speed

    def game_speed_tick(self):

        time.sleep(self.game_speed)

    def set_live(self, x, y):

        row = x // (self.width + self.margin)
        column = y // (self.height + self.margin)
        self.gamefield_lst[column][row].set_live()

    def counting_cells(self):

        height = len(self.gamefield_lst) - 1
        width = len(self.gamefield_lst[0]) - 1

        for index_row, row in enumerate(self.gamefield_lst):
            for index_cell, cell in enumerate(row):
                if cell.is_live:
                    if index_row < height:
                        
                        self.gamefield_lst[index_row + 1][index_cell] += 1                     

                        if index_cell > 0:
                            self.gamefield_lst[index_row + 1][index_cell - 1] += 1
                        if index_cell < width:
                            self.gamefield_lst[index_row + 1][index_cell + 1] += 1

                    if index_row > 0:
                        self.gamefield_lst[index_row - 1][index_cell] += 1

                        if index_cell > 0:
                            self.gamefield_lst[index_row - 1][index_cell - 1] += 1
                        if index_cell < width:
                            self.gamefield_lst[index_row - 1][index_cell + 1] += 1

                    if index_cell > 0:
                        self.gamefield_lst[index_row][index_cell - 1] += 1
                    if index_cell < width:
                        self.gamefield_lst[index_row][index_cell + 1] += 1

    def cell_selection(self):

        for row in self.gamefield_lst:
            for item in row:
                if item.is_live and item.live_count in self.rules[1]:
                    item.is_live = True
                elif not item.is_live and item.live_count in self.rules[0]:
                    item.create_live()
                    
                else:
                    item.delete_live()
                item.set_zeroing()
                
    def set_default(self):

        for row in self.gamefield_lst:
            for item in row:
                item.delete_live() 

