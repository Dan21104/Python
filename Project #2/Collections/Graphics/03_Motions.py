import pygame

screen_width = 1600
screen_height = 900

window = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

SIZE = 30

x = 800
y = 450
vx = 1
vy = 1
a = 0.1

while True:
    # 1 input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    # 2 update
    x += 5 * vx
    y += vy
    vx += a
    vy += a
    a -= 0.001
    if x <= 0 + SIZE or x >= window.get_width() - SIZE:
        vx = -vx
    if y <= 0 + SIZE or y >= window.get_height() - SIZE:
        vy = -vy

    # 3 output / draw
    window.fill((0, 255, 255))
    pygame.draw.circle(window, (255, 255, 0), (x, y), SIZE)
    pygame.display.flip()
    clock.tick(60)
