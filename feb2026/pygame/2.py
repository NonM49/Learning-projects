import sys, pygame
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0
clock = pygame.time.Clock()

screen = pygame.display.set_mode(size)

image = pygame.image.load("private_projects/easy_practice_projects/feb2026/pygame/2_image.jpg")
image_rect = image.get_rect(center = (screen.get_width() / 2, screen.get_height() / 2)) # set image to center of the screen

while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    image_rect = image_rect.move(speed)
    if image_rect.left < 0 or image_rect.right > width:
        speed[0] = -speed[0]
    if image_rect.top < 0 or image_rect.bottom > height:
        speed[1] = -speed[1]

    screen.fill("black")
    screen.blit(image, image_rect)
    pygame.display.flip()