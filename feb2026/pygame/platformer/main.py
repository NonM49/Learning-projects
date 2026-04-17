import pygame
from player import Player
from settings import *
from cut_assets import tile1
from level import Platform, level1

pygame.init()

platforms = []

tile_size = 20

for y, row in enumerate(level1):
    for x, tile in enumerate(row):
        if tile == "X":
            platforms.append(Platform(x * tile_size, y * tile_size))

player = Player(screen)
dt = 0
camera = pygame.Vector2(0, 0)

is_running = True
while is_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    screen.fill("#86cbf0")

    player.input()
    player.update(dt, platforms)

    # 🎥 update camera AFTER player
    camera.x = player.rect.centerx - screen.get_width() // 2
    camera.y = player.rect.centery - screen.get_height() // 2

    # 🎨 draw with camera offset
    for platform in platforms:
        platform.draw(screen, camera)

    player.draw(screen, camera)

    pygame.display.flip()

    dt = clock.tick(60) / 1000
    dt = min(dt, 0.05)
    
#what I learned 

#camera fomula
#draw_x = world_x - camera_x
#draw_y = world_y - camera_y
