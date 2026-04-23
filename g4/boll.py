import pygame
from settings import *
import controls
from random import choice

class Boll:
    def __init__(self, screen):
        self.screen = screen
        self.speed_x = SPEED_BOLL_X * choice((-1, 1))   # швидкість руху по х
        self.speed_y = SPEED_BOLL_Y * choice((-1, 1))   # швидкість руху по у
        self.color = BOLL_COLOR
        self.rect = pygame.Rect(WIDTH//2, HEIGHT//2, RADIUS_BOLL, RADIUS_BOLL) # створюємо прямокутник для м'яча

    def update(self, raketka):           # слідкуємо за рухом м'яча
        self.raketka = raketka
        self.rect.x += self.speed_x      # збільшуємо координату х
        self.rect.y += self.speed_y      # збільшуємо координату у

        if self.rect.x < 0 or self.rect.x > WIDTH:    # відбиття від правої та лівої стін
            self.speed_x = self.speed_x * -1

        if self.rect.y < 0:                             # відбиття від стелі
            self.speed_y = self.speed_y * -1
        
        if self.rect.y > HEIGHT:                        # падіння м'яча нижче підлоги - ПРОГРАШ
            controls.running = False          # гра закінчена
            controls.win = False              # програш

        if self.rect.colliderect(self.raketka): # якщо м'яч доторкнувся до ракетки
            self.speed_y = SPEED_BOLL_Y * choice((-1.1, -1,  -0.9))    # відбиття м'яча
                                        # випадковий вибір швидкості зі списку

        pygame.draw.ellipse(self.screen, self.color, self.rect)      # малюємо м'яч 
