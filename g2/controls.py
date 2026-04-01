import pygame
import sys
from boll import Bol

def events(screen, raketka, boll):              # обробка подій
    for event in pygame.event.get():             # для всіх подій
        if event.type == pygame.QUIT:            # якщо натиснуто хрестик на вікні 
            sys.exit()                           #  то вихід
        elif event.type == pygame.KEYDOWN:       #  відслідковуємо натискання клавіші на клаві
            if event.key == pygame.K_d:         # РУХ ПРАВОРУЧ! якщо натиснута клавіша d
                raketka.mright = True           # 
            elif event.key == pygame.K_a:         # # РУХ ЛІВОРУЧ!якщо натиснута клавіша a
                raketka.mleft = True           #  кажемо натиснута а       
            elif event.key == pygame.K_SPACE:
                if len(boll) < 2:                # кількість кульок одночасно
                    new_boll = Bol(screen)
                    boll.add(new_boll)
        elif event.type == pygame.KEYUP:    # якщо клавішу відпустили
            if event.key == pygame.K_d:         # якщо це d
                raketka.mright = False          # кажемо, що не натиснута d
            elif event.key == pygame.K_a:       # якщо це a
                raketka.mleft = False           # кажемо, що не натиснута a
                
def update(bg_color, screen, raketka, boll): # оновлення екрану
    screen.fill(bg_color)                        # застосувати колір фону
    for bol_1 in boll.sprites():
        bol_1.draw_boll()
    raketka.output()                             # намалювати ракетку
    
    pygame.display.flip()                        # промалювати кадр
