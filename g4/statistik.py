import pygame
from settings import *

def draw_message(screen, text, text_size, color = TEXT_COLOR, y_offset = 0):     # виведення тексту на екран
                                                  # y_offset зміщення по у для наступних рядків 
    
    font = pygame.font.Font(None, text_size)           # використати системний шрифт 
    message = font.render(text, True, color)     
    rect = message.get_rect(center = (WIDTH//2, HEIGHT//2 + y_offset))
    screen.blit(message, rect)
    pygame.display.flip()                   # промалювати кадр
