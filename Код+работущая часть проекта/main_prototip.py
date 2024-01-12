import sys
import pygame

pygame.init()
def draw_start(screen):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("Старт игры!", True, (0, 0, 255))
    text_1 = width // 2 - text.get_width() // 2
    text_2 = height // 2 - text.get_height() // 2
    text_3 = text.get_width()
    text_4 = text.get_height()
    screen.blit(text, (text_1, text_2))
    pygame.draw.rect(screen, (0, 255, 0), (text_1 - 10, text_2 - 10,
                                           text_3 + 20, text_4 + 20), 1)


size = width, height = 1200, 800
screen = pygame.display.set_mode(size)
x = 150
y = 650
x1 = 0
#  n = pygame.image.load('images/future-city-art-cyberpunk-neon-3 — копия (2).webp').convert()
pygame.display.set_caption('pygame')
icon = pygame.image.load('2706092 — копия.png').convert_alpha()
pygame.display.set_icon(icon)
count = 0
#list_left = [
#    pygame.image.load('images/rakosha/дракончики1.png').convert_alpha(),
#    pygame.image.load('images/rakosha/дракончики2.png').convert_alpha(),
#    pygame.image.load('images/rakosha/дракончики3.png').convert_alpha(),
#    pygame.image.load('images/rakosha/дракончики1.png').convert_alpha(),
#]

#list_right = [
#    pygame.image.load('images/drakon-/дракончики11.png').convert_alpha(),
#    pygame.image.load('images/drakon-/дракончики22.png').convert_alpha(),
#    pygame.image.load('images/drakon-/дракончики33.png').convert_alpha(),
#    pygame.image.load('images/drakon-/дракончики11.png').convert_alpha(),
#]
# fon = pygame.image.load('1613237918_194-p-fon-dlya-intro-gacha-sinii-255.jpg').convert()
musik = pygame.mixer.Sound('мелодия звуковой анимации.mp3')
musik.play()




draw_start(screen)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            print('Нажатие на мышку еще дорабатьывается  мышки пока в разработки')
    mouse = pygame.mouse.get_pos()
    pygame.display.flip()
pygame.quit()
