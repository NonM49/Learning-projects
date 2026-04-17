import pygame
from player import Player
from game import screen
from bullet import Bullet
from enemy import Enemy

pygame.init()

dt = 0

clock = pygame.time.Clock()

player = Player()
bullet = Bullet()

enemies = [Enemy()]
spawn_timer = 0.0
spawn_interval = 1.0      # start: 1 enemy every 2 sec
min_spawn_interval = 0.4  # cap
interval_decay = 0.98     # gets harder each spawn

restart_rect = pygame.Rect(0, 0, 140, 50)
restart_rect.center = (screen.get_width() / 2, screen.get_height () / 2 + 60)

game_over = False
is_running = True

font = pygame.font.SysFont(None, 36, True)

aim_dir = pygame.Vector2(1, 0) # prevent first click error

while is_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # event.button == 1: check when left click
            bullet.shoot(player.pos, aim_dir)

        if game_over and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if restart_rect.collidepoint(event.pos):
                game_over = False
                score = 0
                player.set_position()
                enemies.clear()
                bullet.bullets.clear()
                enemies = [Enemy()]
                spawn_timer = 0.0
                spawn_interval = 2.0

    if not game_over:
        screen.fill("#8feb7c")

        spawn_timer += dt
        if spawn_timer >= spawn_interval:
            enemies.append(Enemy())
            spawn_timer = 0.0
            spawn_interval = max(min_spawn_interval, spawn_interval * interval_decay)

        mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
        aim_dir = mouse_pos - player.pos #Vector subtraction gives direction from player to mouse.
        if aim_dir.length_squared() > 0:
            aim_dir = aim_dir.normalize()

        player.move_key(dt)
        player.movement_limit()

        bullet.update(dt)
        # move enemies
        for e in enemies:
            e.run_toward(dt, player.pos)

        # bullet vs enemies
        alive_enemies = []
        for e in enemies:
            hit = False
            for b in bullet.bullets[:]:
                if e.pos.distance_to(b["pos"]) <= e.radius + bullet.radius:
                    bullet.bullets.remove(b)
                    e.take_damage(1)
                    hit = True
                    break
            if e.hp > 0:
                alive_enemies.append(e)
        enemies = alive_enemies

        # enemy vs player
        for e in enemies:
            if e.pos.distance_to(player.pos) <= e.radius + player.radius:
                game_over = True
                break

    player.draw(aim_dir)
    bullet.draw()
    for e in enemies:
        e.draw()

    if game_over:
        over_text = font.render("GAME OVER", True, "red")
        screen.blit(over_text, over_text.get_rect(center=(screen.get_width()/2, screen.get_height()/2)))

        pygame.draw.rect(screen, "white", restart_rect, border_radius=8)
        txt = font.render("Restart", True, "black")
        screen.blit(txt, txt.get_rect(center=restart_rect.center))

    pygame.display.flip()

    dt = clock.tick(60) / 1000




