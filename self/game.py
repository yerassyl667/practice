import pygame

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Моя первая игра на Pygame")

# Цвета
WHITE = (255, 255, 255)

# Основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заливка экрана цветом
    screen.fill(WHITE)

    # Обновление экрана
    pygame.display.flip()

# Завершаем Pygame
pygame.quit()
