import pygame

pygame.init()

size = (1024, 768)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Alain's Game")
rubik = pygame.image.load("rocket.png").convert_alpha()
rubik = pygame.transform.scale(rubik, (100, 100))
pygame.display.set_icon(rubik)

clock = pygame.time.Clock()

x = 100
y = 100
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("你点了关闭")
            pygame.quit()
            exit()

    screen.blit(rubik, (x, y))
    x = x + 2

    pygame.display.update()
    clock.tick(60)
