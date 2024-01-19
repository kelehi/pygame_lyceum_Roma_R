import pygame
import sys


def game():
    list_random = []
    clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((1500, 800))
    pygame.display.set_caption('Программа Романа')
    icon = pygame.image.load('s/2706092.png')
    pygame.display.set_icon(icon)
    ghost = pygame.image.load('s/2603009.png')
    player = pygame.image.load('s/leftgame/x1670754038.png.pagespeed.ic.Z3RY1P6uWG.png')
    rn1 = pygame.image.load('s/drakon-/дракончики11.png').convert_alpha()
    rn2 = pygame.image.load('s/drakon-/дракончики22.png').convert_alpha()
    rn3 = pygame.image.load('s/drakon-/дракончики33.png').convert_alpha()
    rn4 = pygame.image.load('s/drakon-/дракончики11.png').convert_alpha()
    count_right = 0
    player_x = 150
    player_y = 750
    ghost_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(ghost_timer, 8000)
    is_jump = False
    jump_count = 15
    bg_s = pygame.mixer.Sound('s/Фон для игры - Без названия.mp3')
    bg_s.play()
    count_right += 1
    running = True
    list_x_y = 0
    while running:
        screen.blit(pygame.image.load('fonts/future-city-art-cyberpunk-neon-3.webp').convert(), (list_x_y, 0))
        if count_right == 1:
            screen.blit(rn1, (0, 675))
        elif count_right == 2:
            screen.blit(rn2, (0, 675))
        elif count_right == 3:
            screen.blit(rn3, (0, 675))
        elif count_right == 4:
            screen.blit(rn4, (0, 675))
            count_right = 0
        keys = pygame.key.get_pressed()
        count_right += 1
        pygame.display.update()
        for event in pygame.event.get():
            if keys[pygame.K_ESCAPE]:
                running = False