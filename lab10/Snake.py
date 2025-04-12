import pygame
import random
import psycopg2

WIDTH = 600
HEIGHT = 400
CELL_SIZE = 20
FPS = 10
LEVEL_UP_SCORE = 5

def get_db_connection():
    return psycopg2.connect(
        dbname="snake_game",
        user="postgres",
        password="X6temax6",
        host="localhost",
        port="5432"
    )

def get_or_create_user(username):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, username, level, score FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    if user:
        return user[0], user[2], user[3]
    else:
        cur.execute("INSERT INTO users (username, level, score) VALUES (%s, %s, %s) RETURNING id",
                    (username, 1, 0))
        user_id = cur.fetchone()[0]
        conn.commit()
        return user_id, 1, 0

def update_user_score(user_id, score, level):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE users SET score = %s, level = %s WHERE id = %s", (score, level, user_id))
    conn.commit()

def game_loop():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 32)
    small_font = pygame.font.SysFont("Arial", 20)
    snake = [(100, 100), (90, 100), (80, 100)]
    direction = (CELL_SIZE, 0)
    food = (random.randrange(1, WIDTH // CELL_SIZE) * CELL_SIZE,
            random.randrange(1, HEIGHT // CELL_SIZE) * CELL_SIZE)
    score = 0
    level = 1
    user_id = None
    username = ""
    input_active = True
    while input_active:
        screen.fill((0, 0, 0))
        name_text = font.render("Введите имя пользователя:", True, (255, 255, 255))
        screen.blit(name_text, (WIDTH // 2 - name_text.get_width() // 2, HEIGHT // 3 - 50))
        input_text = font.render(username, True, (255, 255, 255))
        screen.blit(input_text, (WIDTH // 2 - input_text.get_width() // 2, HEIGHT // 2 + 5))
        if username:
            user_id, level, score = get_or_create_user(username)
            stats_text = small_font.render(f"Ваш уровень: {level}, Очки: {score}", True, (255, 255, 255))
            screen.blit(stats_text, (WIDTH // 2 - stats_text.get_width() // 2, HEIGHT // 2 + 50))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                input_active = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    user_id, level, score = get_or_create_user(username)
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    username += event.unicode
        clock.tick(15)

    running = True
    paused = False
    global FPS
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                    direction = (-CELL_SIZE, 0)
                elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                    direction = (CELL_SIZE, 0)
                elif event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                    direction = (0, -CELL_SIZE)
                elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                    direction = (0, CELL_SIZE)
                elif event.key == pygame.K_p:
                    paused = not paused

        if not paused:
            head_x, head_y = snake[0]
            new_head = (head_x + direction[0], head_y + direction[1])
            if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT or new_head in snake:
                update_user_score(user_id, score, level)
                running = False
                continue
            snake = [new_head] + snake
            if new_head == food:
                score += 1
                if score % LEVEL_UP_SCORE == 0:
                    level += 1
                    FPS += 2
                food = (random.randrange(1, WIDTH // CELL_SIZE) * CELL_SIZE,
                        random.randrange(1, HEIGHT // CELL_SIZE) * CELL_SIZE)
            else:
                snake.pop()

            for segment in snake:
                pygame.draw.rect(screen, (0, 255, 0), (*segment, CELL_SIZE, CELL_SIZE))

            pygame.draw.rect(screen, (255, 0, 0), (*food, CELL_SIZE, CELL_SIZE))

            score_text = small_font.render(f"Очки: {score}", True, (255, 255, 255))
            level_text = small_font.render(f"Уровень: {level}", True, (255, 255, 255))
            screen.blit(score_text, (10, 10))
            screen.blit(level_text, (10, 30))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

game_loop()
