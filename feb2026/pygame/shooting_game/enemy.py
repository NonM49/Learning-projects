import pygame
import random
from game import screen

pygame.init()

class Enemy():
    def __init__(self):
        self.radius = 20
        self.speed = 80
        self.hp = 5
        
        margin = self.radius + 10
        w, h = screen.get_width(), screen.get_height()
        side = random.choice(["top", "bottom", "left", "right"])

        if side == "top":
            self.pos = pygame.Vector2(random.randint(0, w), -margin)
        elif side == "bottom":
            self.pos = pygame.Vector2(random.randint(0, w), h + margin)
        elif side == "left":
            self.pos = pygame.Vector2(-margin, random.randint(0, h))
        elif side == "right":
            self.pos = pygame.Vector2(w + margin, random.randint(0, h))

    def draw(self):
        pygame.draw.circle(screen, "red", self.pos, self.radius)

    def run_toward(self, dt, target_pos):
        direction = target_pos - self.pos
        if direction.length_squared() > 0:
            direction = direction.normalize()
        self.pos += direction * self.speed * dt

    def take_damage(self, damage):
        self.hp -= damage

