import pygame
from GlobalVar import *
from GlobalFunc import *


class Treasure(pygame.sprite.Sprite):
    def __init__(self, path, pos_x, pos_y):
        super().__init__()
        self.list = []
        for i in range(1, 4):
            self.list.append(load_image(path + "/treasure_" + str(i) + ".png"))
        self.image = self.list[0]
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.counter = 0

    def update(self):
        self.counter += .1
        if self.counter >= len(self.list):
            self.counter = 0

        self.image = self.list[int(self.counter)]


class Kirka(pygame.sprite.Sprite):
    def __init__(self, img, pos_x, pos_y):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y


class Sword(pygame.sprite.Sprite):
    def __init__(self, img, pos_x, pos_y):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y


class Tile(pygame.sprite.Sprite):
    def __init__(self, img, pos_x, pos_y):
        super().__init__()
        # pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    # def update(self, *args, **kwargs):
        # return super().update(*args, **kwargs)
    def update(self):
        pass
