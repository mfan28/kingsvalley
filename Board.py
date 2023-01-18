import pygame
from GlobalVar import *
from GlobalFunc import *
from Level import *
from Enemy import Enemy


class Board:
    herox = 0
    heroy = 0
    # относительные координаты вьюшки
    # показывать на экране будем область из "уровня"
    v_x = 0
    v_y = 0
    
    def __init__(self, board):
        path = path_abs + "/img/level"
        path_enemy = path_abs + "/img/enemy"
        self.tile_images = {
            'wall': load_image(path + '/wall_1.png'),
            'lstair': load_image(path + '/downst_2.png'),
            'rstair': load_image(path + '/downst_1.png'),
            'kirka': load_image(path + '/kirka.png'),
            'sword': load_image(path + '/sword.png')
            
        }

        lvlname = board[0]

        self.lvlmap = board[1]

        # значения по умолчанию
        self.left = 0
        self.top = tile_size + 1
        self.cell_size = tile_size
        self.width = len(self.lvlmap[0])
        self.height = len(self.lvlmap)

        # делаем массив пустым
        self.board = [[0] * self.width for _ in range(self.height)]

        x0 = self.left
        y0 = self.top
        for i in range(0, self.height):
            for j in range(0, self.width):

                if self.lvlmap[i][j] == "#":
                    self.board[i][j] = 1
                    tilename = "wall"
                elif self.lvlmap[i][j] == "$":
                    self.board[i][j] = 2
                    tilename = "lstair"
                elif self.lvlmap[i][j] == "%":
                    self.board[i][j] = 3
                    tilename = "rstair"
                elif self.lvlmap[i][j] == "*":
                    self.board[i][j] = 4
                elif self.lvlmap[i][j] == "^":
                    self.board[i][j] = 5
                    tilename = "kirka"
                elif self.lvlmap[i][j] == "+":
                    self.board[i][j] = 6
                    tilename = "sword"
                elif self.lvlmap[i][j] == "!":
                    self.herox = x0
                    self.heroy = y0
                elif self.lvlmap[i][j] == "&":
                    self.board[i][j] = 7
                    
                    

                if self.board[i][j] > 0:
                    if self.board[i][j] <= 3:
                        tTile = Tile(self.tile_images[tilename], x0, y0)
                        tiles_group.add(tTile)
                    elif self.board[i][j] == 4:
                        tTreasure = Treasure(path, x0, y0)
                        treasures_group.add(tTreasure)
                    elif self.board[i][j] == 5:
                        tKirka = Kirka(self.tile_images[tilename], x0, y0)
                        kirka_group.add(tKirka)
                    elif self.board[i][j] == 6:
                        tSword = Sword(self.tile_images[tilename], x0, y0)
                        sword_group.add(tSword)
                    elif self.board[i][j] == 7:
                        tEnemy = Enemy(x0, y0-16)
                        enemy_group.add(tEnemy)
                        # схитрим и занулим, т.к мумия в "карту" не входит
                        self.board[i][j] = 0

                x0 = x0 + self.cell_size
            y0 = y0 + self.cell_size
            x0 = self.left

    def render(self):
        x0 = self.left
        y0 = self.top
        size = self.cell_size

        for i in range(0, self.height):
            x0 = self.left
            for j in range(0, self.width):
                # если 0 - рисуем клетку линией, если не 0 - закрашиваем
                if self.board[i][j] == 0:
                    pass
                # тут будем рисовать белую клеточку, а потом врисовывать
                # туда цветной квадратик
                elif self.board[i][j] == 1:
                    pass    

                elif self.board[i][j] == 2:
                    pass    

                x0 = x0 + size
            y0 = y0 + size

