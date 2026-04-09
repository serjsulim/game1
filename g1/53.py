import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((1000, 600)) # створюємо вікно
pygame.display.set_caption('Test')           # заголовок вікна
bg_color = (0, 0, 0)                             # змінна колір фону вікна
boll_color = (255, 255, 250)

rect = pygame.Rect(400, 200, 50, 50)       # створюємо прямокутник
image = pygame.image.load('g1/bus.png') # присвоюємо змінній файл з малюнком ракетки
rect1 = image.get_rect(center = (300, 300))  # тримуємо картинку як прямокутник для можливості керування

while True:
    for event in pygame.event.get():             # для всіх подій
        if event.type == pygame.QUIT:            # якщо натиснуто хрестик на вікні 
            sys.exit()                           #  то вихід
    screen.fill(bg_color)                       # зафарбовуємо екран кольором
    pygame.draw.rect(screen, boll_color, rect) # у прямокутник малюємо еліпс
    screen.blit(image, rect1)                   # малюємо на екрані
    
    pygame.display.flip()                        # оновлюємо дисплей