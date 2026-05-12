import pygame
from settings import *
from boll import Boll
from raketka import Raketka
import controls
import time


class Drop:
    def __init__(self):
        self.color = DROP_COLOR
        self.radius = DROP_RADIUS
        self.rect = []                     # список для додавання крапельок

    def new_drop(self, x, y, special):     # створення нової крапельки
        self.special = special
        if self.special > 0 and self.special != 3:               # якщо цеглинка незвичайна (номер більше нуля)
            self.rect.append([pygame.Rect(x, y, DROP_RADIUS, DROP_RADIUS), self.special])   # створюємо крапельку тої ж спеціалізації, що й цеглина

    def update(self, screen, raketka, boll):     # оновлення положення крапельки на екрані
        self.screen = screen
        self.raketka = raketka
        self.boll = boll
        for drop in self.rect:    # перебираємо усі крапельки у списку
            drop[0].y += DROP_SPEED_Y     # рухаємо їх униз
            if drop[0].colliderect(self.raketka):   #  якщо краплинка доторкається до ракетки
                if drop[1] == 1:                    # якщо спеціалізація краплинки 1
                    self.boll.speed_x *= 1.2        # збільшуємо швидкість
                    self.boll.speed_y *= 1.2        #
                elif drop[1] == 2:                  # якщо спеціалізація краплинки 2
                    self.boll.speed_x *= 0.8        # зменшуємо швидкість
                    self.boll.speed_y *= 0.8
                elif drop[1] == 4 or drop[1] == 5:   # якщо спеціалізація 4 або 5
                    controls.start_time = time.time() # запам'ятовуємо час зміни ракетки
                    raketka.resize_raketka(drop[1])    # змінюємо її розмір
                self.rect.remove(drop)    # видаляємо краплинку 

            pygame.draw.ellipse(self.screen, self.color[drop[1]], drop[0])      # малюємо краплинку
            if drop[0].y > HEIGHT:        # якщо крапелька впала нижче екрану
                self.rect.remove(drop)    # видаляємо її