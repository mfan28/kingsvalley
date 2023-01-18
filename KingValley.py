import pygame
import sys

from GlobalVar import *
from GlobalFunc import *

from Maps import Maps
from TopMenu import TopMenu
from Board import Board
from Hero import Hero
from Enemy import Enemy


pygame.init()

screen_size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(screen_size)


# пока всё внутри класса, ничего не расчитываем
# просто выводим
topmenu = TopMenu()

# все карты сразу в символьном виде
# читаем все файлы 
# TODO: поставить ограничение на раширение .map
# Легенда:
# # - стена
# $ - лестница вправо
# % - лестница влево
# ^ - кирка
# ! - главный герой 
# * - клад
# + - меч

maps = Maps()

# согласно номеру текущей карты, инициализируем поле
brd = Board(maps.get_currentmap())

# герой появится, где мы нарисуем на карте,
# по рандому - жестковато будет
hero = Hero(brd.herox, brd.heroy - 16)
hero_group.add(hero)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressedkey = pygame.key.get_pressed()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            pygame.quit()
        if event.key == pygame.K_RIGHT:
            hero.dir = "right"
        if event.key == pygame.K_LEFT:
            hero.dir = "left"
    if event.type == pygame.KEYUP:
        # Make the 
        if hero.dir not in "up down":
            hero.dir = ""

    if hero.dir == "right":
        hero.x += 2
    if hero.dir == "left":
        hero.x -= 2

    screen.fill(BLACK)
    # рисуем меню
    topmenu.draw(screen)
    tiles_group.draw(screen)
    treasures_group.draw(screen)
    kirka_group.draw(screen)
    sword_group.draw(screen)
    enemy_group.draw(screen)
    hero_group.draw(screen)
    
    clock.tick(FPS)
    pygame.display.update()
    tiles_group.update()
    treasures_group.update()
    enemy_group.update()
    hero_group.update()

pygame.quit()
