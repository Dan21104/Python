import pygame

screen_width = 600
screen_height = 600

window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sokoban")
clock = pygame.time.Clock()


def game_input():
    ...


def game_update():
    ...


def game_output():
    ...


while True:
    game_input()
    game_update()
    game_output()
