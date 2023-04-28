import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 1000

BACKGROUND_COLOR = (0, 0, 0)
BULLET_COLOR = (255, 255, 255)
BULLET_SIZE = 5

shipA_x = SCREEN_WIDTH / 2 - 15
shipA_y = SCREEN_HEIGHT - 70
bullet_x = shipA_x
bullet_y = shipA_y
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
    if shipA_x < -20:
        shipA_x = -20
    if shipA_x > SCREEN_WIDTH - 45:
        shipA_x = SCREEN_WIDTH - 45


def game_output():
    window.fill(BACKGROUND_COLOR)
    pygame.draw.circle(window, BULLET_COLOR, (bullet_x, bullet_y), BULLET_SIZE)
    window.blit(ship_A, (shipA_x, shipA_y))
    pygame.display.flip()


while True:
    game_input()
    game_update()
    game_output()
    clock.tick(144)
