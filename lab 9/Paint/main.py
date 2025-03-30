import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))
drawing = False
last_pos = None
radius = 5
color = (0, 0, 0)
shape = "free"

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                last_pos = event.pos
                start_pos = event.pos
            elif event.button == 3:
                screen.fill((255, 255, 255))
            elif event.button == 4:
                radius += 1
            elif event.button == 5:
                radius = max(1, radius - 1)
        elif event.type == pygame.MOUSEBUTTONUP:
            if shape == "rectangle":
                end_pos = event.pos
                width = abs(end_pos[0] - start_pos[0])
                height = abs(end_pos[1] - start_pos[1])
                rect_x = min(start_pos[0], end_pos[0])
                rect_y = min(start_pos[1], end_pos[1])
                pygame.draw.rect(screen, color, (rect_x, rect_y, width, height), 2)
            elif shape == "right_triangle":
                end_pos = event.pos
                pygame.draw.polygon(screen, color, [
                    (start_pos[0], start_pos[1]),
                    (end_pos[0], start_pos[1]),
                    (start_pos[0], end_pos[1])
                ], 2)
            elif shape == "equilateral_triangle":
                side = abs(event.pos[0] - start_pos[0])
                height = (side * (3 ** 0.5)) / 2
                pygame.draw.polygon(screen, color, [
                    (start_pos[0] - side / 2, start_pos[1] + height / 2),
                    (start_pos[0] + side / 2, start_pos[1] + height / 2),
                    (start_pos[0], start_pos[1] - height / 2)
                ], 2)
            elif shape == "diamond":
                w = abs(event.pos[0] - start_pos[0]) // 2
                h = abs(event.pos[1] - start_pos[1]) // 2
                pygame.draw.polygon(screen, color, [
                    (start_pos[0], start_pos[1] - h),
                    (start_pos[0] - w, start_pos[1]),
                    (start_pos[0] + w, start_pos[1]),
                    (start_pos[0], start_pos[1] + h)
                ], 2)
            elif shape == "circle":
                end_pos = event.pos
                radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                pygame.draw.circle(screen, color, start_pos, radius, 2)
            drawing = False
        elif event.type == pygame.MOUSEMOTION and drawing and shape == "free":
            if last_pos:
                pygame.draw.line(screen, color, last_pos, event.pos, radius)
            last_pos = event.pos
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = (255, 0, 0)
            elif event.key == pygame.K_g:
                color = (0, 255, 0)
            elif event.key == pygame.K_b:
                color = (0, 0, 255)
            elif event.key == pygame.K_t:
                shape = "rectangle"
            elif event.key == pygame.K_o:
                shape = "circle"
            elif event.key == pygame.K_f:
                shape = "free"
            elif event.key == pygame.K_c:
                color = (255, 255, 255)
            elif event.key == pygame.K_p:
                shape = "right_triangle"
            elif event.key == pygame.K_e:
                shape = "equilateral_triangle"
            elif event.key == pygame.K_d:
                shape = "diamond"
    pygame.display.update()

pygame.quit()