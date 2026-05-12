import pygame
import os                            # Das Dateisystem
import controls
from settings import *               # із файлу settings імпортуємо усе
from raketka import Raketka          # імпортуємо з файлу raketka клас Raketka 
from boll import Boll
import statistik
from map import level_map
from briks import Brick
import time
from drop import Drop



clock = pygame.time.Clock()  # змінна для створення FPS
pygame.mixer.pre_init(44100, -16, 1, 512) # виправлення багу затримки музики
pygame.init()      # ініціюємо модуль pygame
won_sound = pygame.mixer.Sound("music/won.wav")
lose_sound = pygame.mixer.Sound("music/lose.wav")
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # створюємо вікно 
pygame.display.set_caption('Arkanoid')           # заголовок вікна

def run(level):            
    
    raketka = Raketka(screen)                  # створюємо ракетку з рядка 3 імпорту з файла ракетка
    boll = Boll(screen)                        # cтворюємо м'яч
    brick = Brick(level)                       # цеглинки 
    drop = Drop()                              # список краплинок
    start_time = time.time()

    while controls.running:
        controls.events(screen, raketka)           # відслідковуємо натискання клавіш для руху ракетки
        raketka.update_raketka(drop)                   # оновити положення ракетки ()              
        controls.update(BG_COLOR, screen, raketka, boll, brick, drop) # відслідковування взаємодій
        
        clock.tick(FPS)        # вказуємо, щоб даний цикл while виконувався FPS раз на секунду

    end_time = time.time()
    screen.fill(BG_COLOR)        # очистити екран

    if controls.win:         # перевіряємо виграш
        statistik.draw_message(screen, 'You WON', 200, y_offset = -100) # вивести на екран повідомлення про виграш
        won_sound.play()
        controls.running = True
        controls.level += 1
    else:
        statistik.draw_message(screen, 'You Lose', 200, y_offset = -100) # вивести на екран повідомлення про програш
        lose_sound.play()

    controls.time_game += int(end_time - start_time)     # рахує час рівня і додає його до загального часу
    statistik.draw_message(screen, f'Рахунок: {controls.count}', 100, TEXT_COLOR, y_offset = 0)
    statistik.draw_message(screen, f'Час гри: {controls.time_game// 60} хвилин {controls.time_game % 60} секунд', 100, TEXT_COLOR,   y_offset = 100)   
    pygame.time.wait(5000)      # чекати 10000 мілісекунд

while controls.win and controls.level < len(level_map):
    run(controls.level)

if controls.level >= len(level_map):
    screen.fill(BG_COLOR)
    statistik.draw_message(screen, 'You beat all levels!', 200, y_offset=-100)
    statistik.draw_message(screen, f'Рахунок: {controls.count}', 100, TEXT_COLOR, y_offset=0)
    statistik.draw_message(screen, f'Час гри: {controls.time_game// 60} хвилин {controls.time_game % 60} секунд', 100, TEXT_COLOR,   y_offset=100)
    pygame.display.flip()
    pygame.time.wait(5000)

pygame.quit()    # вихід з гри
