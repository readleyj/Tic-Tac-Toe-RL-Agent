import pygame


pygame.init()
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption('Testing a game')
pygame.mouse.set_visible(0)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))

while True:
    screen.blit(background, (0, 0))
    pygame.display.flip()
