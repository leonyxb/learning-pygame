import sys
import pygame

pygame.init()

size = (800, 500)

pygame.display.set_mode(size)
pygame.display.set_caption("我的游戏")
icon = pygame.image.load("rubik.png")
pygame.display.set_icon(icon)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
