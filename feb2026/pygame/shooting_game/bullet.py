import pygame
from game import screen

pygame.init()

class Bullet():
    def __init__(self):
        self.bullets = []
        self.speed = 500
        self.radius = 5
        

    def update(self, dt):
        for b in self.bullets:
            b["pos"] += b["dir"] * self.speed * dt

        self.bullets = [
            b for b in self.bullets
            if 0 <= b["pos"].x <= screen.get_width()
            and 0 <= b["pos"].y <= screen.get_height()
        ]

    def draw(self):
        for b in self.bullets:
            pygame.draw.circle(screen, "black", b["pos"], 5)

    def shoot(self, pos, dir):
        self.bullets.append({
                "pos": pos.copy(),
                "dir": dir.copy()
            })


