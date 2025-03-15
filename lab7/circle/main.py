import pygame

pygame.init()

WIDTH, HEIGHT = 1280, 720

Radius = 25
Step = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()

x, y = 50, 50
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and y - Step - Radius >= 0:
        y -=Step
    if keys[pygame.K_s] and y + Step + Radius <= HEIGHT:
        y += Step
    if keys[pygame.K_a] and  x - Step - Radius >= 0:
        x -= Step
    if keys[pygame.K_d] and x + Step + Radius <= WIDTH:
        x += Step
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), Radius)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()