import pygame
import time
pygame.init()

clock_face = pygame.image.load("clock.png")
right_arm = pygame.image.load("rightarm.png")
left_arm = pygame.image.load("leftarm.png")

WIDTH, HEIGHT = clock_face.get_size()
CENTER = (WIDTH // 2, HEIGHT // 2)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")

def blit_rotate_center(surf, image, pos, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=pos).center)
    surf.blit(rotated_image, new_rect.topleft)


running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(clock_face, (0, 0))

    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    minute_angle = minutes * -11
    second_angle = seconds * -6

    blit_rotate_center(screen, right_arm, CENTER, minute_angle)
    blit_rotate_center(screen, left_arm, CENTER, second_angle)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    time.sleep(1)

pygame.quit()