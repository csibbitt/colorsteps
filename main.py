import pygame
from pygame import Color
from palettes import ALL_PALETTES

pygame.init()
screen = pygame.display.set_mode([800, 600])
font = pygame.font.SysFont(None, 25)

palette_index = 0
color_index = 0
screen.fill(ALL_PALETTES[palette_index]['colors'][color_index])
pygame.display.flip()

running = True
while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT or (i.type == pygame.KEYUP and i.key == pygame.K_q):
            running = False
            pygame.quit()
            break

        if i.type == pygame.KEYUP and i.key == pygame.K_UP:
            color_index = (color_index + 1) % len(ALL_PALETTES[palette_index]['colors'])

        if i.type == pygame.KEYUP and i.key == pygame.K_DOWN:
            color_index = (color_index - 1) % len(ALL_PALETTES[palette_index]['colors'])

        if i.type == pygame.KEYUP and i.key == pygame.K_RIGHT:
            palette_index = (palette_index + 1) % len(ALL_PALETTES)
            color_index = 0

        if i.type == pygame.KEYUP and i.key == pygame.K_LEFT:
            palette_index = (palette_index - 1) % len(ALL_PALETTES)
            color_index = 0

        cur_color = ALL_PALETTES[palette_index]['colors'][color_index]
        screen.fill(cur_color)
        text = font.render(ALL_PALETTES[palette_index]['name'] +
            '[' + str(color_index) + '](' +
            hex(cur_color.r) + ',' +
            hex(cur_color.g) + ',' +
            hex(cur_color.b) +
            ')', True, Color('blue'))
        screen.blit(text, (0, 0))
        pygame.display.flip()
        pygame.display.update()