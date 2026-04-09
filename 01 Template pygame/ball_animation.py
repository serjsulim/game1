
import pygame   # die Spiele-Engine
import random   # Zufallszahlen brauchen wir immer...
import os       # Das Dateisystem

WIDTH = 400       # Breite des Bildschirms in Pixeln
HEIGHT = 300      # Höhe des Bildschirms in Pixeln
FPS = 60          # Frames per Second (30 oder 60 FPS sind üblicher Standard)

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

PI = 3.1415

pygame.init()           # pygame Initialisierung
pygame.mixer.init()     # Die Sound-Ausgabe wird initialisiert
pygame.display.set_caption("My Game")   # Überschrift des Fensters

clock = pygame.time.Clock()



screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED)


game_folder = os.path.dirname(__file__)


image_dict = {}
image_dict["ball"] = pygame.image.load(os.path.join(game_folder, '_images/ball.png')).convert_alpha()
for i in range(1,9):
    image_dict["coin"+str(i)] = pygame.image.load(os.path.join(game_folder, '_images/coin'+str(i)+'.png')).convert_alpha()

class Ball:
    def __init__(self, x, y, sx, sy):
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.image = image_dict["coin1"]
        self.imageRect = self.image.get_rect()

        # Animation
        self.timer = 0
        self.anim_frames = 8
        self.act_frame = 1
        self.max_ticks_anim = 5

    def update(self):
        # Animation
        self.timer += 1
        if self.timer >= self.max_ticks_anim:
            self.timer = 0
            self.act_frame += 1
            if self.act_frame > self.anim_frames:
                self.act_frame = 1
            self.image = image_dict["coin" + str(self.act_frame)]

        # Position
        self.x += self.sx
        self.y += self.sy

        self.imageRect.topleft = (self.x,self.y)

        if self.imageRect.right >= WIDTH or self.imageRect.left <= 0:
            self.sx = self.sx * -1

        if self.imageRect.bottom >= HEIGHT or self.imageRect.top <= 0:
            self.sy = self.sy * -1

    def render(self, screen):
        screen.blit(self.image, self.imageRect)

sprites = []
for _ in range(5):
    sprites.append(Ball(random.randint(64, WIDTH-64),
                   random.randint(64, HEIGHT-64),
                   random.choice([-3,-2,4,3]),
                   random.choice([-2,-3,3,4])))

running = True

while running:
    

    dt = clock.tick(FPS) / 1000

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # Windows Close Button?
            running = False             # dann raus aus dem Game Loop

    

    for sprite in sprites:
        sprite.update()

    screen.fill(WHITE)    # RGB Weiß

    for sprite in sprites:
        sprite.render(screen)

    pygame.display.flip()

pygame.quit()
