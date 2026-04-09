import pygame

class Bol(pygame.sprite.Sprite):

    def __init__(self, screen):
        super(Bol, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(500, 500, 20, 20)
        self.color = 100, 100, 100
        self.speed = [0.5, 0.5]
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)



    def update(self, raketka, game):             # рух кульки
        self.x -= self.speed[0]
        self.rect.x = self.x
        self.raketka = raketka
        
        self.y -= self.speed[1]
        self.rect.y = self.y

     # 2. ВІДБИТТЯ ВІД СТІН
        # Від лівої або правої стіни
        if self.rect.left <= 0 or self.rect.right >= 1000:
             self.speed[0] = - self.speed[0]  # змінюємо напрямок по X

        # Від верхньої стіни
        if self.rect.top <= 0:
             self.speed[1] = - self.speed[1]  # змінюємо напрямок по Y

        # Якщо впала вниз (програш)
        if self.rect.bottom >= 600:
            #self.speed[1] = - self.speed[1]  # змінюємо напрямок по Y
            game = False
            return game

        if self.rect.bottom >= self.raketka.rect.top and (self.raketka.rect.left < self.rect.centerx < self.raketka.rect.right):
            self.speed[1] *= -1  

    def draw_boll(self):
        pygame.draw.ellipse(self.screen, self.color, self.rect)
