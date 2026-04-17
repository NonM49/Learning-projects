import pygame
from game import screen

class Player():
    def __init__(self):
        self.radius = 20
        self.speed = 200
        self.pos = pygame.Vector2((screen.get_width() / 2, screen.get_height() / 2))
        self.color = "black"

    def set_position(self):
        self.pos = pygame.Vector2((screen.get_width() / 2, screen.get_height() / 2))

    def draw(self, aim_dir):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)
        pygame.draw.circle(screen, "blue", self.pos, self.radius, 5)

        cannon_len = 26
        cannon_wid = 20
        cannon = pygame.Surface((cannon_len, cannon_wid), pygame.SRCALPHA)
        cannon.fill(self.color)

        angle = aim_dir.angle_to((pygame.Vector2(1, 0)))
        rot_cannon = pygame.transform.rotate(cannon, angle)

        cannon_center = self.pos + aim_dir * ((self.radius - (self.radius / 2)) + cannon_len * 0.5)
        cannon_rect = rot_cannon.get_rect(center=cannon_center)

        screen.blit(rot_cannon, cannon_rect)

    def move_key(self, dt):
        self.move = pygame.Vector2(0, 0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.move.x -= 1
        if keys[pygame.K_d]:
            self.move.x += 1
        if keys[pygame.K_w]:
            self.move.y -= 1
        if keys[pygame.K_s]:
            self.move.y += 1

        if self.move.length_squared() > 0:
            self.move = self.move.normalize()

        self.pos += self.move * self.speed * dt

    def movement_limit(self):
        self.pos.x = max(self.radius, min(screen.get_width() - self.radius, self.pos.x))
        self.pos.y = max(self.radius, min(screen.get_height() - self.radius, self.pos.y))
