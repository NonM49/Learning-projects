import pygame
import random

pygame.init()

screen = pygame.display.set_mode((360,500))
clock = pygame.time.Clock()
dt = 0
is_running = True

rect_side = 30

font = pygame.font.SysFont(None, 36, True)

score = 0
game_over = False
restart_rect = pygame.Rect(0, 0, 140, 50)
restart_rect.center = (screen.get_width() / 2, screen.get_height() / 2 + 60)

spawn_interval = 5.0
spawn_timer = 0

enemy_radius = 10
enemies = []

def setcenter():
    return pygame.Vector2(screen.get_width() / 2, screen.get_height() / 1.2)

def increase_enemy():
    enemies.append({
        "pos": pygame.Vector2(random.randint(enemy_radius, screen.get_width() - enemy_radius),random.randint(-500, -enemy_radius)),
        "enemy_x": random.choice([-80, 80]),
        "enemy_y": random.randint(100, 300)
        })    
    
player_pos = setcenter()
increase_enemy()

while is_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if game_over and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if restart_rect.collidepoint(event.pos):
                game_over = False
                score = 0
                player_pos = setcenter()
                enemies.clear()
                increase_enemy()


    screen.fill("#6ba6b1")

    if not game_over:
        score += dt

        
        move = pygame.Vector2(0, 0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            move.x -= 1
        if keys[pygame.K_d]:
            move.x += 1
        if keys[pygame.K_w]:
            move.y -= 1
        if keys[pygame.K_s]:
            move.y += 1

        if move.length_squared() > 0:
            move = move.normalize()

        player_pos += move * 300 * dt

        half_size = rect_side / 2
        player_pos.x = max(half_size, min(screen.get_width() - half_size, player_pos.x))
        player_pos.y = max(half_size, min(screen.get_height() - half_size, player_pos.y))


        spawn_timer += dt
        if spawn_timer >= spawn_interval:
            spawn_timer -= spawn_interval
            increase_enemy()

    player_rect = pygame.Rect(0, 0, rect_side, rect_side)
    player_rect.center = (player_pos.x, player_pos.y)
    pygame.draw.rect(screen, "grey", player_rect)

    for enemy in enemies:

        enemy["pos"].y += enemy["enemy_y"] * dt
        enemy["pos"].x += enemy["enemy_x"] * dt

        if enemy["pos"].x - enemy_radius <= 0 or enemy["pos"].x + enemy_radius >= screen.get_width():
            enemy["enemy_x"] *= -1

        if enemy["pos"].y - enemy_radius > screen.get_height():
            enemy["pos"].x = random.randint(enemy_radius, screen.get_width() - enemy_radius)
            enemy["pos"].y = -enemy_radius
            enemy["enemy_y"] = random.randint(100, 300)

        pygame.draw.circle(screen, "red", (int(enemy["pos"].x), int(enemy["pos"].y)), enemy_radius)

        nearest_x = max(player_rect.left, min(enemy["pos"].x, player_rect.right))
        nearest_y = max(player_rect.top, min(enemy["pos"].y, player_rect.bottom))
        #basicly: if enemy["pos"].x is in between player_rect.left, player_rect.right return enemy_["pos"].x


        dx = enemy["pos"].x - nearest_x 
        dy = enemy["pos"].y - nearest_y 

        if dx * dx + dy * dy <= enemy_radius * enemy_radius:
            game_over = True

    score_text = font.render(f"Score: {int(score)}", True, "black")
    screen.blit(score_text, (20, 20))

    if game_over:
        over_text = font.render("GAME OVER", True, "red")
        screen.blit(over_text, over_text.get_rect(center=(screen.get_width()/2, screen.get_height()/2)))

        pygame.draw.rect(screen, "white", restart_rect, border_radius=8)
        txt = font.render("Restart", True, "black")
        screen.blit(txt, txt.get_rect(center=restart_rect.center))

        for enemy in enemies:
            enemy["enemy_x"] = 0
            enemy["enemy_y"] = 0

    pygame.display.flip()

    dt = clock.tick(60) / 1000
