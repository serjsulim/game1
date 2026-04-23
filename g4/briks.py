import pygame
from settings import *
from boll import Boll
import controls
from random import choice

class Brick:
    def __init__(self):   
        self.rect = []          #  список усіх цеглинок
            # special 
            # 1 Збільшує швидкість руху м'яча
            # 2 зменшує швидкість руху м'яча
            # 3 не реалізовано
            # 4 не реалізовано
        for x in range(55, WIDTH - BRICK_WIDTH - 10, BRICK_WIDTH + 10):    # перебираємо усі координати по ширині
            for y in range(70, 70 + (BRICK_HEIGHT + 10) * ROW_AMAUNT, BRICK_HEIGHT + 10):  # перебираємо усі координати по висоті
                self.special = choice((1, 2, 3, 4))                                        # випадково обираємо спеціалізацію цеглинки
                self.rect.append([pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT), self.special])  # додаємо цеглинки у список

    def drew(self, screen, boll):          # відслідковуємо взаємодію з м'ячем
        self.boll = boll
        for brick in self.rect:            # перебираємо усі блоки
            if brick[0].colliderect(self.boll):   # якщо перетнувся з м'ячем
                self.rect.remove(brick)           # видаляємо блок
                controls.count += 1               # збільшуємо рахунок
                              
                if brick[1] == 1:
                    self.boll.speed_y = self.boll.speed_y // abs(self.boll.speed_y) * SPEED_BOLL_Y * (- 1.4)
                    self.boll.speed_x = self.boll.speed_x // abs(self.boll.speed_x) * SPEED_BOLL_X * 1.4
                elif brick[1] == 2:
                    self.boll.speed_y = self.boll.speed_y // abs(self.boll.speed_y) * SPEED_BOLL_Y * (- 0.6)
                    self.boll.speed_x = self.boll.speed_x // abs(self.boll.speed_x) * SPEED_BOLL_X * 0.6
                else:
                    self.boll.speed_y *= -1           # змінюємо напрям
                

            pygame.draw.rect(screen, BRICK_COLOR[brick[1]], brick[0])

        if len(self.rect) == 0:
            controls.win = True
            controls.running = False

