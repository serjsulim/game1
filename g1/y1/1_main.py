import pygame
import sys
from raketka import Raketka          # імпортуємо з файлу raketka клас Raketka 

def run():
    width = 1000                               # ширина вікна
    height = 600                               # висота вікна

    pygame.init()
    screen = pygame.display.set_mode((width,height)) # створюємо вікно 
    pygame.display.set_caption('Arkanoid')           # заголовок вікна
    bg_color = (0, 0, 0)                             # змінна колір фону вікна
    raketka = Raketka(screen)                  # створюємо ракетку з рядка 3 імпорту з файла ракетка


    while True:
        for event in pygame.event.get():             # для всіх подій
            if event.type == pygame.QUIT:            # якщо натиснуто хрестик на вікні 
                sys.exit()                           #  то вихід
        screen.fill(bg_color)                        # застосувати колір фону
        raketka.output()                             # намалювати ракетку
        pygame.display.flip()                        # промалювати кадр

run()

