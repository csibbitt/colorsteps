import pygame
from palettes import CGA

pygame.init()
screen = pygame.display.set_mode([800,600])

color_index = 0
screen.fill(CGA[color_index])
pygame.display.flip()

while True:
  for i in pygame.event.get():
      if i.type == pygame.QUIT:
        running = False
        pygame.quit()
      if i.type == pygame.KEYUP and i.key == pygame.K_SPACE:
        color_index = (color_index + 1) % len(CGA)
        screen.fill(CGA[color_index])
        pygame.display.flip()