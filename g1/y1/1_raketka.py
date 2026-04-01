import pygame

class Raketka:

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('g2/image/raketka.png') # присвоюємо змінній файл з малюнком ракетки
        self.rect = self.image.get_rect()  # зробили нашу ракетку як прямокутник
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx      # координати центру по x ракетки виставити по центру екрана
        self.rect.bottom = self.screen_rect.bottom       # низ ракетки по низу екрана

    def output(self):               # малювання ракетки
        self.screen.blit(self.image, self.rect)

