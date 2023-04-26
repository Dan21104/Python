# todo
import pygame
pygame.init()

BACKGROUND_COLOR = (0, 0, 0)

PADDLE_COLOR = (255, 255, 255)
PADDLE_WIDTH = 20
PADDLE_LENGTH = 200

LINE_COLOR = (255, 255, 255)
LINE_WIDTH = 10
LINE_LENGTH = 70

paddle_x = 10
paddle_y = 350

BALL_COLOR = (255, 255, 255)
BALL_SIZE = 15

ball_x = 800
ball_y = 450
ball_vx = 0.1
ball_vy = 0.1
ball_a = 0.0008
ball_dx = 1
ball_dy = -1

step = 7

score = 0
score_increment = 1

cor = 20

font_obj = pygame.font.Font(None, 32)
text_Surface = font_obj.render(str(score), True, (97, 222, 42), None)
text_Rect = text_Surface.get_rect()
text_Rect.center = (800, 30)

screen_width = 1600
screen_height = 900

window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()


def game_input():
    global paddle_y, step
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_ESCAPE]:
        exit()
    elif key_input[pygame.K_w] or key_input[pygame.K_UP]:
        paddle_y -= step
    elif key_input[pygame.K_s] or key_input[pygame.K_DOWN]:
        paddle_y += step
    pygame.display.update()


def game_update():
    global ball_x, ball_y, ball_dx, ball_dy, ball_vx, ball_vy, score, text_Surface, text_Rect, paddle_y
    ball_x += 5 * ball_vx * ball_dx
    ball_y += 2 * ball_vy * ball_dy
    if ball_y <= 0 + BALL_SIZE:
        ball_dy = 1
    if ball_y >= screen_height - BALL_SIZE:
        ball_dy = -1
    if ball_x >= screen_width - BALL_SIZE:
        ball_dx = -1
    if ball_x <= paddle_x + PADDLE_WIDTH * 2\
            and ball_y - PADDLE_WIDTH <= ball_y <= paddle_y + PADDLE_LENGTH + PADDLE_WIDTH:
        ball_dx = 1
        score += score_increment
        text_Surface = font_obj.render(str(score), True, (97, 222, 42), None)
        text_Rect = text_Surface.get_rect()
        text_Rect.center = (800, 30)
    if ball_x < 0:
        ball_x = screen_width / 2
        ball_y = screen_height / 2
        ball_vx = 0.1
        ball_vy = 0.1
        ball_dx = 1
        score = 0
    if ball_vx < 2 and ball_vy < 2:
        ball_vx += ball_a
        ball_vy += ball_a
    if paddle_y < 0:
        paddle_y = 0
    if paddle_y > screen_height - PADDLE_LENGTH:
        paddle_y = screen_height - PADDLE_LENGTH


def game_output():
    global cor
    window.fill(BACKGROUND_COLOR)
    pygame.draw.rect(window, PADDLE_COLOR, (paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_LENGTH))
    pygame.draw.circle(window, BALL_COLOR, (ball_x, ball_y), BALL_SIZE)
    window.blit(text_Surface, text_Rect)
    while cor <= screen_height:
        pygame.draw.rect(window, LINE_COLOR, (800, cor, LINE_WIDTH, LINE_LENGTH))
        cor += 90
    pygame.display.flip()


while True:
    game_input()
    game_update()
    game_output()
    clock.tick(144)
