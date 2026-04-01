import pygame

# Ініціалізація
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Створюємо кульку (прямокутник) та задаємо швидкість
ball_rect = pygame.Rect(400, 300, 20, 20)
ball_speed = [5, -5]  # [швидкість_x, швидкість_y]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 1. РУХ: додаємо швидкість до координат прямокутника
    ball_rect.x += ball_speed[0]
    ball_rect.y += ball_speed[1]

    # 2. ВІДБИТТЯ ВІД СТІН
    # Від лівої або правої стіни
    if ball_rect.left <= 0 or ball_rect.right >= 800:
        ball_speed[0] = -ball_speed[0]  # змінюємо напрямок по X

    # Від верхньої стіни
    if ball_rect.top <= 0:
        ball_speed[1] = -ball_speed[1]  # змінюємо напрямок по Y

    # Якщо впала вниз (програш)
    if ball_rect.bottom >= 600:
       ball_speed[1] = -ball_speed[1]  # змінюємо напрямок по Y
        #print("Game Over")
       # ball_rect.center = (400, 300) # Повертаємо в центр

    # Малювання
    screen.fill((30, 30, 30))
    pygame.draw.ellipse(screen, (255, 255, 255), ball_rect) # Малюємо коло всередині Rect
    
    pygame.display.flip()
    clock.tick(60) # 60 FPS

pygame.quit()