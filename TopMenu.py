import pygame
from GlobalVar import *


class TopMenu:

    def __init__(self):
        pass

    def draw(self, screen):
        tx = 0
        ty = 0
        colortext = WHITE
        backgroundtext = BLACK
        textsize = 32

        font = pygame.font.Font(None, textsize)
        strCount = "Очки: " + "000000"
        textCount = font.render(strCount, 1, colortext, backgroundtext)
        screen.blit(textCount, (tx, ty))

        strLives = "Жизни: " + "05"
        tx += 160
        textLives = font.render(strLives, 1, colortext, backgroundtext)
        screen.blit(textLives, (tx, ty))

        strLevel = "Уровень: " + "01"
        tx += 160
        textLevel = font.render(strLevel, 1, colortext, backgroundtext)
        screen.blit(textLevel, (tx, ty))
