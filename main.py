import pygame

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Pygame Sprite Control')

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

player = pygame.Rect(100, 100, 50, 50)
static_rect = pygame.Rect(300, 200, 50, 50)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 1
    if keys[pygame.K_RIGHT]:
        player.x += 1
    if keys[pygame.K_UP]:
        player.y -= 1
    if keys[pygame.K_DOWN]:
        player.y += 1

    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, player)
    pygame.draw.rect(screen, BLUE, static_rect)
    
    pygame.display.flip()

pygame.quit()