import pygame

# Initialization
pygame.init()

size = (400, 160)
win = pygame.display.set_mode(size)
pygame.display.set_caption('Jeu MacGyver')
framework = pygame.image.load('images/structures.png')

win.blit(framework, (0, 0))


# Refresh
state = True

while state:
    
    win.blit(framework, (0, 0))
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = False
