import pygame
from settings import *
from boll import Boll
import controls
from random import choice
from map import *
from drop import Drop
from raketka import Raketka

class Brick:
    def __init__(self, level):   
        self.rect = []          #  список усіх цеглинок
        self.sound_bricks = pygame.mixer.Sound("music/1.wav")
        self.level = level
        self.map = level_map[self.level]
            # special 
            # 0 проста цеглина
            # 1 Збільшує швидкість руху м'яча
            # 2 зменшує швидкість руху м'яча
            # 3 має підвищену міцність
            # 4 зменшує ракетку
            # 5 збільшує ракетку
        
        for y in range(len(self.map)):
            for x in range(len(self.map[0])):
                self.rect.append([pygame.Rect(int( 0.1 * BRICK_WIDTH + 1.1 * BRICK_WIDTH * x), 50 + 1.3 * y * BRICK_HEIGHT, BRICK_WIDTH, BRICK_HEIGHT), self.map[y][x]])  # додаємо цеглинки у список

    def drew(self, screen, boll, drop, raketka):          # відслідковуємо взаємодію з м'ячем
        self.boll = boll
        self.drop = drop
        for brick in self.rect:            # перебираємо усі блоки
            if brick[0].colliderect(self.boll):   # якщо перетнувся з м'ячем
                self.drop.new_drop(self.boll.rect.x, self.boll.rect.y, brick[1])
                self.sound_bricks.play()
                if brick[1] == 3:          # якщо спеціалізація 3 (міцна)
                    brick[1] = 0           # робимо її звичайною але не видаляємо
                else:    
                    self.rect.remove(brick)           # видаляємо блок
                controls.count += 1               # збільшуємо рахунок
                self.boll.speed_y *= -1           # змінюємо напрям
                
                

            pygame.draw.rect(screen, BRICK_COLOR[brick[1]], brick[0])
        self.drop.update(screen, raketka, self.boll)
        if len(self.rect) == 0:    # коли всі цеглинки розбито
            controls.win = True
            controls.running = False

