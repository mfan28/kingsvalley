import pygame
from random import randint
from GlobalVar import *
from GlobalFunc import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.counter = 0
        self.x = pos_x
        self.y = pos_y
        self.velocity = randint(2,5)
        self.isStair = False
        if randint(0, 1) == 0:
            self.dir = "right"
        else:
            self.dir = "left"
        self.prov = self.dir

        self.listempty = []

        path = path_abs + "/img/enemy"
        for i in range(1, 4):
            self.listempty.append(load_image(path + "/mummy_" + str(i) + ".png"))

        self.image = self.listempty[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.counter += .15

        if self.dir == "right":
            self.x += self.velocity
        else:
            self.x -= self.velocity

        if self.x > (WIDTH - 16):
            self.dir = "left"
        if self.x < -16:
            self.dir = "right"


        actlist = self.listempty

        if self.counter >= len(actlist):
            self.counter = 0

        if self.dir == "left":
            self.image = actlist[int(self.counter)]
            self.prov = self.dir
        elif self.dir == "right":
            self.image = pygame.transform.flip(actlist[int(self.counter)], True, False)
            self.prov = self.dir
        elif self.dir == "":
            if self.prov == "left":
                self.image = actlist[0]
            else:
                self.image = pygame.transform.flip(actlist[0], True, False)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.mask = pygame.mask.from_surface(self.image)