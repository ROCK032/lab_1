import pygame
import random

pygame.init()
W, H = 600, 400
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Snake")
font = pygame.font.Font(None, 36)
Cell_Size = 20

Food_Types = [
    {"color": (255, 0, 0), "points": 10, "speed_change": 1.5},
    {"color": (255, 255, 0), "points": 20, "speed_change": 2},
    {"color": (255, 20, 147), "points": 5, "speed_change": 1}
]


def random_food(snake):
    while True:
        x = random.randint(0, (W - Cell_Size) // Cell_Size) * Cell_Size
        y = random.randint(0, (H - Cell_Size) // Cell_Size) * Cell_Size
        food_type = random.choice(Food_Types)
        if (x, y) not in snake:
            return x, y, food_type


def game_over_screen(score, level):
    screen.fill((0, 0, 0))
    text = font.render(f"Game Over: {score}, Level {level}", True, (255, 255, 255))
    text2 = font.render("Try Again -> Enter or Exit -> ESC", True, (255, 255, 255))
    screen.blit(text, (W // 2 - 150, H // 2 - 20))
    screen.blit(text2, (W // 2 - 200, H // 2 + 20))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                elif event.key == pygame.K_RETURN:
                    return True


def game_loop():
    snake = [(W // 2, H // 2)]
    dx, dy = Cell_Size, 0
    score = 0
    level = 1
    speed = 10
    food_eaten = 0
    food_timer = pygame.time.get_ticks()
    food = random_food(snake)
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -Cell_Size
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, Cell_Size
                elif event.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -Cell_Size, 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = Cell_Size, 0

        head_x, head_y = snake[0]
        new_head = (head_x + dx, head_y + dy)

        if (
                new_head[0] < 0 or new_head[0] >= W or
                new_head[1] < 0 or new_head[1] >= H or
                new_head in snake
        ):
            running = False

        snake.insert(0, new_head)

        if new_head == (food[0], food[1]):
            food_type = food[2]
            food = random_food(snake)
            score += food_type["points"]
            food_eaten += 1
            speed = max(5, speed + food_type["speed_change"])
            food_timer = pygame.time.get_ticks()
            if food_eaten % 3 == 0:
                level += 1
        else:
            snake.pop()

        if pygame.time.get_ticks() - food_timer >= 5000:
            food = random_food(snake)
            food_timer = pygame.time.get_ticks()

        screen.fill((0, 0, 0))
        score_text = font.render(f"Score: {score} Level: {level}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        pygame.draw.rect(screen, food[2]["color"], (food[0], food[1], Cell_Size, Cell_Size))

        for segment in snake:
            pygame.draw.rect(screen, (0, 255, 0), (segment[0], segment[1], Cell_Size, Cell_Size))

        pygame.display.update()
        clock.tick(speed)

    if game_over_screen(score, level):
        game_loop()

game_loop()