import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 1000

shipA_x = SCREEN_WIDTH / 2 - 15
shipA_y = SCREEN_HEIGHT - 70

step = 3.5

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")
clock = pygame.time.Clock()

ship_A = pygame.image.load('Default/ship_A.png')


def game_input():
    global shipA_x, shipA_y, step
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_ESCAPE]:
        exit()
    elif key_input[pygame.K_LEFT]:
        shipA_x -= step
    elif key_input[pygame.K_RIGHT]:
        shipA_x += step
    pygame.display.update()


def game_update():
    global shipA_x
    if shipA_x < -30:
        shipA_x = -30
    if shipA_x > SCREEN_WIDTH - 10:
        shipA_x = SCREEN_WIDTH - 10


def game_output():
    window.blit(ship_A, (shipA_x, shipA_y))
    pygame.display.flip()


while True:
    game_input()
    game_update()
    game_output()
    clock.tick(144)
