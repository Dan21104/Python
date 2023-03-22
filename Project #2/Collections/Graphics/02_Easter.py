import pygame

screen_width = 1600
screen_height = 900
window = pygame.display.set_mode((screen_width, screen_height))

coordinate_x = 100

while coordinate_x <= 1400:
    pygame.draw.ellipse(window, (150, 250, 69), (coordinate_x, 600, 230, 300))
    coordinate_x += 300
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
