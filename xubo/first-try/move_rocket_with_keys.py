import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("我的游戏")

clock = pygame.time.Clock()

pos_x = 400
pos_y = 300
move_x = 0
move_y = 0
rocket_surf = pygame.transform.scale(pygame.image.load("graphics/rocket.png").convert_alpha(), (50, 50))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_y = -1
            if event.key == pygame.K_DOWN:
                move_y = 1

            if event.key == pygame.K_LEFT:
                move_x = -1
            if event.key == pygame.K_RIGHT:
                move_x = 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                move_y = 0
            if event.key == pygame.K_DOWN:
                move_y = 0

            if event.key == pygame.K_LEFT:
                move_x = 0
            if event.key == pygame.K_RIGHT:
                move_x = 0

    screen.fill("black")
    pos_x = pos_x + move_x
    pos_y = pos_y + move_y
    rocket_rect = rocket_surf.get_rect(center=(pos_x, pos_y))
    screen.blit(rocket_surf, rocket_rect)

    pygame.display.update()

    clock.tick(60)
