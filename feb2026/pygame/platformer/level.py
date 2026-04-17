import pygame
from cut_assets import tile1

tile1 = pygame.transform.scale(tile1, (20, 20))

pygame.init()

class Platform():
    def __init__(self, x, y, w = 20, h = 20):
        self.rect = pygame.Rect(x, y, w, h)

    def draw(self, screen, camera):
        screen.blit(tile1, self.rect.topleft - camera)

level1 = [
    "....................",
    "...X................",
    "..........X........",
    ".................X..",
    "....................",
    "....................",
    "...............XXXX.",
    "XXXXXXXXXX.........."
]