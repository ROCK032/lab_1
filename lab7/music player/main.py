import pygame

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Music Player")

pygame.font.init()
font = pygame.font.SysFont("comicsansms", 25)

_songs = ['song.mp3', 'song2.mp3', 'song3.mp3']
_current_index = 0
_paused = False

def play_song():
    pygame.mixer.music.load(_songs[_current_index])
    pygame.mixer.music.play()

def play_next_song():
    global _current_index
    _current_index = (_current_index + 1) % len(_songs)
    play_song()

def play_prev_song():
    global _current_index
    _current_index = (_current_index - 1) % len(_songs)
    play_song()

def toggle_pause():
    global _paused
    if _paused:
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.pause()
    _paused = not _paused

play_song()

SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)

running = True

while running:
    screen.fill((0, 0, 0))

    song_name = _songs[_current_index]
    text_name = font.render(f'Name Music: {song_name}', True, (255, 255, 255))

    clue_a = font.render('A -> Previous', True, (255, 255, 255))
    clue_d = font.render('D -> Next', True, (255, 255, 255))
    clue_space = font.render('SPACE -> Pause/Play', True, (255, 255, 255))

    screen.blit(text_name, (20, 50))
    screen.blit(clue_a, (20, 150))
    screen.blit(clue_d, (20, 200))
    screen.blit(clue_space, (20, 250))

    pygame.display.flip()

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == SONG_END:
            play_next_song()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                play_prev_song()
            elif event.key == pygame.K_d:
                play_next_song()
            elif event.key == pygame.K_SPACE:
                toggle_pause()

pygame.quit()
