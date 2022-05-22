import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("我的游戏")

clock = pygame.time.Clock()

rocket_surf = pygame.transform.scale(pygame.image.load("graphics/rocket.png").convert_alpha(), (50, 50))


move = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("black")
    if move:
        rocket_rect = rocket_surf.get_rect(center=pygame.mouse.get_pos())
    else:
        rocket_rect = rocket_surf.get_rect(center=(400, 300))

    if rocket_rect.collidepoint(pygame.mouse.get_pos()):
        move = True

    screen.blit(rocket_surf, rocket_rect)

    pygame.display.update()

    clock.tick(60)
