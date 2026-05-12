import pygame
from settings import *
import time
import controls


class Raketka:

    def __init__(self, screen):
        self.screen = screen
        self.image_norm = pygame.image.load('image/raketka.png') # присвоюємо змінній файл з малюнком ракетки
        self.image_small = pygame.image.load('image/raketka_small.png') # присвоюємо змінній файл з малюнком ракетки  
        self.image_big = pygame.image.load('image/raketka_big.png')
        self.image = self.image_norm                          
        self.rect = self.image.get_rect()  # зробили нашу ракетку як прямокутник
        self.screen_rect = screen.get_rect()   #  створюємо прямокутник за розміром екрану
        self.rect.centerx = self.screen_rect.centerx      # координати центру по x ракетки виставити по центру екрана
        self.rect.bottom = self.screen_rect.bottom       # низ ракетки по низу екрана
        self.mright = False        # відслідковує, чи натиснута клавіша вправо
        self.mleft = False         # відслідковує, чи натиснута клавіша вліво
        

    def output(self):               # розміщуємо малюнок ракетки на прямокутнику на екрані
        self.screen.blit(self.image, self.rect)

    def update_raketka(self, drop):       # оновлення позиції ракетки
        self.drop = drop
        if self.mright and self.rect.right < self.screen_rect.right:    # якщо натиснута клавіша вправо і правий край ракетки менше правого краю вікна
            self.rect.centerx += SPEED_RAKETKA
        elif self.mleft  and self.rect.left > self.screen_rect.left:    # якщо натиснута клавіша вліво і лівий край ракетки більше лів краю вікна
            self.rect.centerx -= SPEED_RAKETKA

        end_time = time.time()                          # таймер скільки ракетка буде зміненою
        if end_time - controls.start_time > 5:          # якщо час більше 5 секунд
            self.resize_raketka(0)                      # робимо ракетку нормальною
            controls.start_time = 11111111111111111
        
    def resize_raketka(self, size):                       # зміна розміру ракетки
        centr_x = self.rect.centerx                       # запам'ятовуємо положення центру ракетки по х
        if size == 4:                                     # якщо спеціалізація крапельки 4 
            self.image = self.image_small                 # то присвоюємо ракетці малий малюнок
        elif size == 5:
            self.image = self.image_big                # інакше великий малюнок
        else:
            self.image = self.image_norm 
        self.rect = self.image.get_rect()           # зстворюємо  прямокутник ракетки
        self.rect.bottom = self.screen_rect.bottom       # низ ракетки по низу екрана
        self.rect.centerx = centr_x                      # розміщаємо центр ракетки де запам'ятали

