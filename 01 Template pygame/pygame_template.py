
import pygame
import random
import os

WIDTH = 400
HEIGHT = 300
FPS = 60

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("My Game")

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED)
game_folder = os.path.dirname(__file__)

sprite_images = {}
sprite_images["ball"] = pygame.image.load(
    os.path.join(game_folder, "_images/ball.png")
).convert_alpha()

class Ball:
    def __init__(self, x, y, sx, sy):
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.image = sprite_images["ball"]
        self.imageRect = self.image.get_rect()

    def update(self):
        
        self.x += self.sx
        self.y += self.sy

        self.imageRect.topleft = (self.x,self.y)
        
        if self.imageRect.right >= WIDTH or self.imageRect.left <= 0:
            self.sx *= -1

        if self.imageRect.bottom >= HEIGHT or self.imageRect.top <= 0:
            self.sy *= -1

    def draw(self, surface):
        surface.blit(self.image, self.imageRect)

sprites = []
for _ in range(10):
    sprites.append(Ball(
        random.randint(64, WIDTH - 64),
        random.randint(64, HEIGHT - 64),
        random.choice([-3, -2, -1, 1, 2, 3]),
        random.choice([-3, -2, -1, 1, 2, 3]),
    ))

running = True

while running:

    dt = clock.tick(FPS) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for sprite in sprites:
        sprite.update()

    screen.fill((255, 255, 255))    # RGB weiß

    for sprite in sprites:
        sprite.draw(screen)

    pygame.display.flip()

pygame.quit()