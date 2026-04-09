import pygame
import sys
from raketka import Raketka          # імпортуємо з файлу raketka клас Raketka 
import controls
from pygame.sprite import Group

def run():
    width = 1000                               # ширина вікна
    height = 600                               # висота вікна
    game = True
    pygame.init()
    screen = pygame.display.set_mode((width,height)) # створюємо вікно 
    pygame.display.set_caption('Arkanoid')           # заголовок вікна
    bg_color = (0, 0, 0)                             # змінна колір фону вікна
    raketka = Raketka(screen)                  # створюємо ракетку з рядка 3 імпорту з файла ракетка
    boll = Group()



    while game:
        controls.events(screen, raketka, boll)                     # відслідковуємо ракетку
        raketka.update_raketka()
        controls.update(bg_color, screen, raketka, boll)
        boll.update(raketka, game)

run()

