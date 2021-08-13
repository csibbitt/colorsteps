import pygame
from palettes import CGA, EGA

pygame.init()
screen = pygame.display.set_mode([800, 600])

color_index = 0
screen.fill(EGA[color_index])
pygame.display.flip()

running = True
while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT or (i.type == pygame.KEYUP and i.key == pygame.K_q):
            running = False
            pygame.quit()

        if i.type == pygame.KEYUP and i.key == pygame.K_UP:
            color_index = (color_index + 1) % len(EGA)
            screen.fill(EGA[color_index])
            pygame.display.flip()

        if i.type == pygame.KEYUP and i.key == pygame.K_DOWN:
            color_index = (color_index - 1) % len(EGA)
            screen.fill(EGA[color_index])
            pygame.display.flip()
