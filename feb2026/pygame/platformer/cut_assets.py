import pygame
import os

pygame.init()

base_path = os.path.dirname(__file__) # get the folder that this file in

def get_path(file):
    return os.path.join(base_path, file) # build full path

player_sprite1 = pygame.image.load(get_path("assets/Characters/tile_0004.png"))
player_sprite2 = pygame.image.load(get_path("assets/Characters/tile_0005.png"))
tile1 = pygame.image.load(get_path("assets/Tiles/tile_0000.png"))