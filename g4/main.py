import pygame
import os                            # Das Dateisystem
import controls
from settings import *               # із файлу settings імпортуємо усе
from raketka import Raketka          # імпортуємо з файлу raketka клас Raketka 
from boll import Boll
import statistik
from briks import Brick
import time


clock = pygame.time.Clock()  # змінна для створення FPS

def run():            
    
    
    pygame.init()      # ініціюємо модуль pygame
    
    screen = pygame.display.set_mode((WIDTH, HEIGHT)) # створюємо вікно 
    pygame.display.set_caption('Arkanoid')           # заголовок вікна
    raketka = Raketka(screen)                  # створюємо ракетку з рядка 3 імпорту з файла ракетка
    boll = Boll(screen)                        # cтворюємо м'яч
    brick = Brick()
    start_time = time.time()
    while controls.running:
        controls.events(screen, raketka)           # відслідковуємо натискання клавіш для руху ракетки
        raketka.update_raketka()                   # оновити положення ракетки ()              
        controls.update(BG_COLOR, screen, raketka, boll, brick) # відслідковування взаємодій
        
        clock.tick(FPS)        # вказуємо, щоб даний цикл while виконувався FPS раз на секунду

    end_time = time.time()
    screen.fill(BG_COLOR)        # очистити екран
    if controls.win:         # перевіряємо виграш
        statistik.draw_message(screen, 'You WON', 200, y_offset = -100) # вивести на екран повідомлення про виграш
        statistik.draw_message(screen, f'Рахунок: {controls.count}', 100, TEXT_COLOR, y_offset = 0)
        statistik.draw_message(screen, f'Час гри: {int(end_time - start_time)} секунд', 100, TEXT_COLOR,   y_offset = 100)
    else:
        statistik.draw_message(screen, 'You Lose', 200, y_offset = -100) # вивести на екран повідомлення про програш
        statistik.draw_message(screen, f'Рахунок: {controls.count}', 100, TEXT_COLOR, y_offset = 0)
        statistik.draw_message(screen, f'Час гри: {int(end_time - start_time)} секунд', 100, TEXT_COLOR, y_offset = 100)

    pygame.time.wait(5000)      # чекати 10000 мілісекунд


run()

pygame.quit()    # вихід з гри
