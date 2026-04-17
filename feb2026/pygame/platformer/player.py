import pygame
from settings import gravity
from cut_assets import player_sprite1, player_sprite2

pygame.init()

player_sprite1 = pygame.transform.scale(player_sprite1, (25, 25))
player_sprite2 = pygame.transform.scale(player_sprite2, (25, 25))

animation_speed = 10

class Player():
    def __init__(self, screen):
        self.pos = pygame.Vector2(screen.get_width() // 2, screen.get_height() // 2)
        self.velocity = pygame.Vector2((0, 0))
        self.jump_force = -500
        self.speed = 100
        self.on_ground = False

        self.image = player_sprite1
        self.run_frame = [player_sprite1, player_sprite2]
        self.frame = 0
        self.timer = 0

        self.rect = player_sprite1.get_rect(midbottom=self.pos)

    def input(self):
        keys = pygame.key.get_pressed()

        # Left / Right
        if keys[pygame.K_a]:
            self.velocity.x = -200
        elif keys[pygame.K_d]:
            self.velocity.x = 200
        else:
            self.velocity.x = 0
        
        # jump
        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity.y = self.jump_force

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.on_ground:
                    self.velocity.y = self.jump_force

    def update(self, dt, platforms):
        self.on_ground = False
        self.velocity.y += gravity * dt
        self.pos += self.velocity * dt

        #self.rect = player_sprite.get_rect(center = (self.pos))
        self.rect.midbottom = self.pos

        self.pos.x += self.velocity.x * dt
        self.rect.x = int(self.pos.x)

        self.pos.y += self.velocity.y * dt
        self.rect.y = int(self.pos.y)

        for platform in platforms:
            if self.rect.colliderect(platform):
                if self.velocity.y > 0:  # only when falling
                    self.rect.bottom = platform.rect.top
                    self.on_ground = True
                elif self.velocity.y < 0: # jumping
                    self.pos.y = self.rect.bottom
                    
                self.velocity.y = 0
                self.pos.y = self.rect.y

                if self.velocity.x > 0:  # moving right
                    self.rect.right = platform.rect.left
                elif self.velocity.x < 0:  # moving left
                    self.rect.left = platform.rect.right

                self.pos.x = self.rect.x

        self.pos.x = self.rect.x

        if self.velocity.x != 0:
            self.timer += dt
            if self.timer > 0.1:
                self.frame = (self.frame + 1) % 2
                self.timer = 0
            self.image = self.run_frame[self.frame]
            
    def draw(self, screen, camera):
        # stand
        screen.blit(self.image, self.rect.topleft - camera)