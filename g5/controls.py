import pygame
from settings import *
from boll import Boll
from briks import Brick

running = True     #    змінна, яка показує, коли зупинити гру
win = True         #    змінна, яка показує виграш
count = 0          #    рахунок гри
time_game = 0      #    час гри
level = 0
start_time = 111111111111111   # рахуємо початок зміни ракетки

def events(screen, raketka):              # обробка подій
    for event in pygame.event.get():             # для всіх подій що відбуваються у грі
        if event.type == pygame.QUIT:            # якщо натиснуто хрестик на вікні 
            pygame.quit()                           #  то вихід
        elif event.type == pygame.KEYDOWN:       #  якщо тип події натиснуто клавішу
            if event.key == pygame.K_RIGHT:         # РУХ ПРАВОРУЧ! якщо натиснута клавіша праворуч
                raketka.mright = True           #  
            elif event.key == pygame.K_LEFT:         # # РУХ ЛІВОРУЧ!якщо натиснута клавіша ліворуч
                raketka.mleft = True           #  кажемо натиснута       
 
        elif event.type == pygame.KEYUP:        # якщо клавішу відпустили
            if event.key == pygame.K_RIGHT:     # якщо це вправо
                raketka.mright = False          # кажемо, що не натиснута 
            elif event.key == pygame.K_LEFT:       # якщо це вліво
                raketka.mleft = False           # кажемо, що не натиснута a
                
def update(BG_COLOR, screen, raketka, boll, brick, drop):      # оновлення екрану
    screen.fill(BG_COLOR)                   # замалювати все вікно фоновим кольором
    raketka.output()                        # намалювати ракетку
    boll.update(raketka)                    # відслідковуємо взаємодію м'яча з ракеткою
    brick.drew(screen, boll, drop, raketka)                # відслідковуємо взаємодію цеглинок із м'ячем

    pygame.display.flip()                   # промалювати кадр
