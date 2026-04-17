import pygame
import random
import os
pygame.init()

base_path = os.path.dirname(__file__) # get the folder that this file in

def get_path(file):
    return os.path.join(base_path, file) # build full path

eat_sound = pygame.mixer.Sound(get_path("eat_sound.mp3"))
game_over_sound = pygame.mixer.Sound(get_path("game_over_sound.mp3"))

game_over_sound.set_volume(0.25)

pygame.mixer.music.load(get_path("music.mp3"))
pygame.mixer.music.play(-1) # -1 = play forever
pygame.mixer.music.set_volume(0.25)


cell_size = 20
cell_number = 20
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
clock = pygame.time.Clock()

score = 0
time_store = 0
time_speed = 0.2
font = pygame.font.SysFont(None, 36, True)
game_over_state = False

restart_rect = pygame.Rect(0, 0, 200, 60)
restart_rect.center = (screen.get_width() / 2, screen.get_height() / 2 + 60)

def game_over():
    overlay = pygame.Surface(screen.get_size())
    overlay.set_alpha(40) # set transparency
    overlay.fill("black")
    screen.blit(overlay, (0, 0))

    over_text = font.render("GAME OVER", True, "red")
    screen.blit(over_text, over_text.get_rect(center=(screen.get_width()/2, screen.get_height()/2 - 40)))

    score_text = font.render(f"SCORE : {score}", True, "black")
    screen.blit(score_text, score_text.get_rect(center=(screen.get_width()/2, screen.get_height()/2 )))

    # hover effect on restart button 
    mouse_pos = pygame.mouse.get_pos()
    if restart_rect.collidepoint(mouse_pos):
        color = "#cccccc"
    else:
        color = "white"

    pygame.draw.rect(screen, color, restart_rect, border_radius=8)
    txt = font.render("R to restart", True, "black")
    screen.blit(txt, txt.get_rect(center=restart_rect.center))

def restart():
    global snake, food, game_over_state, time_store, score
    snake = Snake()
    food = Food()
    game_over_state = False
    time_store = 0
    score = 0

def score_format():
    score_text = font.render(f"SCORE : {score}", True, "black")
    score_rect = score_text.get_rect(topleft=(20, 20))
    padding = 10
    bg_rect = score_rect.inflate(padding * 2, padding * 2)
    pygame.draw.rect(screen, "black", bg_rect, 3, border_radius = 8)
    screen.blit(score_text, score_rect)


class Snake():
    def __init__(self):
        self.pos = [pygame.Vector2(14, 10), pygame.Vector2(13, 10)]
        self.head = self.pos[-1]
        self.ate = False
        self.color = "#4398e8"
        self.direction = ""
        self.next_direction = ""

    def draw(self):
        for body in self.pos:
            x_pos = body.x * cell_size
            y_pos = body.y * cell_size
            rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, self.color, rect)
        
class Food():
    def __init__(self):
        self.pos = pygame.Vector2(7, 10)
        self.color = "red"
        self.radius = cell_size / 2

    def draw(self):
        x_pos = self.pos.x * cell_size
        y_pos = self.pos.y * cell_size
        #circle_center = pygame.Vector2(self.pos.x * cell_size, self.pos.y * cell_size)
        food_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
        pygame.draw.circle(screen, self.color, food_rect.center, self.radius)

snake = Snake()
food = Food()
dt = 0
is_running = True

while is_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if game_over_state: # make restart button clickable
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rect.collidepoint(event.pos): # event.pos = (x, y) of mouse click
                    restart()

    screen.fill("#43e88b")

    keys = pygame.key.get_pressed() # get keyboard input

    if keys[pygame.K_r]:
            restart()

    if not game_over_state:
        if keys[pygame.K_a] and snake.direction != "right":
            snake.next_direction = "left"
        if keys[pygame.K_d] and snake.next_direction == "": # prevent instant die on first move
            pass
        elif keys[pygame.K_d] and snake.direction != "left":
            snake.next_direction = "right"
        if keys[pygame.K_w] and snake.direction != "down":
            snake.next_direction = "up"
        if keys[pygame.K_s] and snake.direction != "up":
            snake.next_direction = "down"

        time_store += dt
        if time_store >= time_speed and snake.next_direction != "":
            time_store = 0
            snake.direction = snake.next_direction

            x, y = snake.head
            if snake.direction == "left": # created new head
                x -= 1
            elif snake.direction == "right":
                x += 1
            elif snake.direction == "up":
                y -= 1
            elif snake.direction == "down":
                y += 1
            snake.head = pygame.Vector2(x, y)
            snake.pos.append(snake.head)

            if x < 0 or x >= cell_number or y < 0 or y >= cell_number: # wall collision
                game_over_sound.play()
                game_over_state = True

            if snake.head in snake.pos[:-1]: # snake vs snake   # snake.pos[:-1] = except the last index
                game_over_sound.play()
                game_over_state = True

            if snake.head == food.pos: # snake vs food
                eat_sound.play()
                score += 1
                while True:
                    x = random.randint(0, cell_number - 1)
                    y = random.randint(0, cell_number - 1)
                    new_pos = pygame.Vector2(x, y)

                    if new_pos not in snake.pos: # if food not spawn inside the snake body break
                        food.pos = new_pos
                        break
            else:    
                snake.pos.pop(0)
        food.draw()
        snake.draw()
        score_format()
    else:
        game_over()

    pygame.display.flip()

    dt = clock.tick(60) / 1000


#What i learned
# = → assignment (change value)
# == → comparison (check value)

# -  just calculate
# -=  calculate and update

# __file__ = the current Python file path
# os.path.dirname(...) = gets the folder containing that file
# os.path.join(base_path, file) = Safely combines paths

# collidepoint() = Returns true if the given point is inside the rectangle
