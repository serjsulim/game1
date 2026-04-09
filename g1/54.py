import pygame

pygame.init()               # Ініціюємо модуль (обов'язково)

width = 800
height = 600

screen = pygame.display.set_mode((width,height))   # створюємо вікно
pygame.display.set_caption("Нове вікно")   # заголовок вікна
bg_color = (0, 0, 0)                    # колір фону
rect_color = (255, 255,255)               # колір прямокутника
image = pygame.image.load('g1/bus.png')   # завантажуємо малюнок у змінну image
rect1 = image.get_rect(center =(1000, 100))             # створюємо новий прямокутник для малюнку

rect = pygame.Rect(400, 200, 50, 50)     # створюємо прямокутник у координатах 200. 200 , розміром 100 на 20
runnig = True

while runnig:
    for event in pygame.event.get():   # у цьому циклі перебираються усі події, що настають у грі
        if event.type == pygame.QUIT:   # якщо натиснуто хрестик
            pygame.quit()
            #runnig = False             
    screen.fill(bg_color)           # зафарбовуємо вікно кольором фону
    pygame.draw.ellipse(screen, rect_color, rect)             # малюємо прямокутник у вікні
    screen.blit(image, rect1)                                 # малюємо прямокутник з малюнком
    rect1.x -= 1                                             # робимо рух (збільшуємо координату х)
    #rect1.y += 1                                             # робимо рух (збільшуємо координату х)
    pygame.display.flip()          # оновлюємо вікно



