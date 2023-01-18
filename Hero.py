import pygame
from GlobalVar import *
from GlobalFunc import *


class Hero(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.counter = 0
        self.x = pos_x
        self.y = pos_y

        self.isKirka = False
        self.isSword = False
        self.isStair = False
        self.dir = ""
        self.prov = ""
        self.jumpCount = 10
        self.isJump = False

        # наборы спрайтов по разную активность
        # "пустой" - бежим безо всего, можем прыгать
        # с киркой - прыгать не можем, но можем долбить пол
        # с мечом - прыгать не можем, можем кинуть меч
        self.listempty = []
        self.listkirka = []
        self.listsword = []

        path = path_abs + "/img/hero"
        for i in range(1, 4):
            self.listempty.append(load_image(path + "/heroempty_" + str(i) + ".png"))
            self.listkirka.append(load_image(path + "/herokirka_" + str(i) + ".png"))
            self.listsword.append(load_image(path + "/herosword_" + str(i) + ".png"))

        self.image = self.listempty[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):

        self.counter += .15

        # в зависимости от инструмента - выбираем список спрайтов
        if self.isKirka:
            actlist = self.listkirka
        elif self.isSword:
            actlist = self.listsword
        else:
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
