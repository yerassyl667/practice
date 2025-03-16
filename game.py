import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("RAMRAM")
icon = pygame.image.load('C:\\Users\\kulse\\OneDrive\\Рабочий стол\\practice\\icon.png')
pygame.display.set_icon(icon)
screen.fill((130, 150, 150))
running = True
while running:
    
    

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                screen.fill((130, 250, 250))

    