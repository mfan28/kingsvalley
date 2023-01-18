import pygame


def load_image(name):
    image = pygame.image.load(f"{name}")
    return image


tiles_group = pygame.sprite.Group()
treasures_group = pygame.sprite.Group()
kirka_group = pygame.sprite.Group()
sword_group = pygame.sprite.Group()
hero_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
