import pygame
pygame.init()

TILE_SIZE = 64
LEVEL_WIDTH = 5
LEVEL_HEIGHT = 5

level = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 2, 0, 1],
    [1, 3, 3, 3, 1],
    [1, 1, 1, 1, 1],
]

tiles = [
    (11, 6),    # 0 = floor
    (7, 6),     # 1 = wall
    (1, 0),     # 2 = box
    (10, 5),    # 3 = coin
    (3, 4),     # 4 = up
    (0, 6),     # 5 = right
    (0, 4),     # 6 = down
    (3, 6),     # 7 = left
]

window = pygame.display.set_mode((LEVEL_WIDTH * TILE_SIZE, LEVEL_HEIGHT * TILE_SIZE))
pygame.display.set_caption("Sokoban")
clock = pygame.time.Clock()

p_position = (2, 1)
direction = 4

image = pygame.image.load('Default/sokoban_tilesheet.png')


def game_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_ESCAPE]:
        exit()


def game_update():
    ...


def game_output():
    for y in range(0, LEVEL_HEIGHT):
        for x in range(0, LEVEL_WIDTH):
            draw_tile(0, x, y)
            draw_tile(level[y][x], x, y)
        draw_player()
        pygame.display.flip()


def draw_tile(tile, x, y):
    tx, ty = tiles[tile]
    position = (x * TILE_SIZE, y * TILE_SIZE)
    rectangle = (tx * TILE_SIZE, ty * TILE_SIZE, TILE_SIZE, TILE_SIZE)
    window.blit(image, position, rectangle)


def draw_player():
    x, y = p_position
    draw_tile(4 + direction, x, y)


while True:
    game_input()
    game_update()
    game_output()
    clock.tick(60)
