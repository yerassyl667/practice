import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("TUTU")
icon = pygame.image.load('C:\\Users\\kulse\\OneDrive\\Рабочий стол\\practice\\icon.png')
pygame.display.set_icon(icon)
screen.fill((130, 150, 150))

square = pygame.Surface((100, 125))
square.fill('black')

myfont = pygame.font.Font('C:\\Users\\kulse\\OneDrive\\Рабочий стол\\practice\\BigShouldersStencil-Thin.ttf')
text_surface = myfont.render('Julian', False, 'red')
player = pygame.image.load('C:\\Users\\kulse\\OneDrive\\Рабочий стол\\practice\\icon.png')

running = True
while running:
    
    screen.blit(square, (10, 0))
    pygame.draw.circle(screen, 'orange', (300, 150), 25)
    screen.blit(text_surface, (50, 50))
    screen.blit(player, (300, 100))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()