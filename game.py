import pygame
import math
import time

pygame.init()

WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Часы на Pygame")

font = pygame.font.Font(None, 50)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

CENTER = (WIDTH // 2, HEIGHT // 2)
RADIUS = 150

background = pygame.image.load("cineraria-flower-png-isolated-transparent-background_191095-10910.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

def draw_hand(angle, length, color, width=3):
    x = CENTER[0] + length * math.cos(math.radians(angle))
    y = CENTER[1] - length * math.sin(math.radians(angle))
    pygame.draw.line(screen, color, CENTER, (x, y), width)

running = True
while running:
    screen.blit(background, (0, 0))
    
    pygame.draw.circle(screen, WHITE, CENTER, RADIUS, 3)
    
    current_time = time.localtime()
    hours = current_time.tm_hour % 12
    minutes = current_time.tm_min
    seconds = current_time.tm_sec
    
    sec_angle = 90 - (seconds * 6)
    min_angle = 90 - (minutes * 6)
    hour_angle = 90 - (hours * 30 + minutes * 0.5)
    
    draw_hand(hour_angle, RADIUS * 0.5, RED, 6)
    draw_hand(min_angle, RADIUS * 0.7, BLUE, 4)
    draw_hand(sec_angle, RADIUS * 0.9, GREEN, 2)
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.time.delay(1000)

pygame.quit()

