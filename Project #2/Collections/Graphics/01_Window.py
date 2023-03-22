import pygame

screen_width = 1600
screen_height = 900
window = pygame.display.set_mode((screen_width, screen_height))

pygame.draw.rect(window, (0, 255, 255), (500, 250, 500, 350))
pygame.draw.line(window, (255, 0, 255), (0, 900), (1600, 0), 10)
pygame.draw.circle(window, (255, 255, 0), (800, 450), 150, 5)
pygame.draw.ellipse(window, (150, 250, 69), (250, 50, 300, 200))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
