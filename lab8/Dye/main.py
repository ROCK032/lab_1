import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
current_color = BLACK

screen.fill(WHITE)

drawing = False
mode = "pen"
start_pos = None

font = pygame.font.SysFont(None, 24)


def draw_hints():
    hints = ["R - Rectangle", "C - Circle", "P - Pen", "E - Eraser", "1 - Red", "2 - Green", "3 - Blue", "4 - Black"]
    y = 10
    for hint in hints:
        text = font.render(hint, True, BLACK)
        screen.blit(text, (10, y))
        y += 20


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                start_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                if mode == "rect":
                    end_pos = event.pos
                    rect = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                    pygame.draw.rect(screen, current_color, rect, 2)
                elif mode == "circle":
                    end_pos = event.pos
                    radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                    pygame.draw.circle(screen, current_color, start_pos, radius, 2)
        elif event.type == pygame.MOUSEMOTION and drawing:
            if mode == "pen":
                pygame.draw.line(screen, current_color, event.pos, event.pos, 3)
            elif mode == "eraser":
                pygame.draw.circle(screen, WHITE, event.pos, 10)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = "rect"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_p:
                mode = "pen"
            elif event.key == pygame.K_e:
                mode = "eraser"
            elif event.key == pygame.K_1:
                current_color = (255, 0, 0)
            elif event.key == pygame.K_2:
                current_color = (0, 255, 0)
            elif event.key == pygame.K_3:
                current_color = (0, 0, 255)
            elif event.key == pygame.K_4:
                current_color = (0, 0, 0)

    draw_hints()
    pygame.display.flip()

pygame.quit()
sys.exit()