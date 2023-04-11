import pygame
pygame.init()

screen_width = 1600
screen_height = 900

window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

LP_WIDTH = 20
LP_LENGTH = 200
lp_x = 10
lp_y = 250

RP_WIDTH = 20
RP_LENGTH = 200
rp_x = screen_width - 10 - RP_WIDTH
rp_y = 250

P_SIZE = 15
p_x = 800
p_y = 450
p_vx = 0.1
p_vy = 0.1
p_a = 0.0008
p_dx = 1
p_dy = -1

step = 7

l_score = 0
r_score = 0
score_increment = 1

font_obj = pygame.font.Font(None, 32)
l_text_Surface = font_obj.render(str(l_score), True, (97, 222, 42), None)
l_text_Rect = l_text_Surface.get_rect()
l_text_Rect.center = (700, 30)

r_text_Surface = font_obj.render(str(r_score), True, (97, 222, 42), None)
r_text_Rect = r_text_Surface.get_rect()
r_text_Rect.center = (900, 30)

while True:
    # 1 input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_UP]:
        rp_y -= step
    if key_input[pygame.K_DOWN]:
        rp_y += step
    if key_input[pygame.K_w]:
        lp_y -= step
    if key_input[pygame.K_s]:
        lp_y += step
    if key_input[pygame.K_ESCAPE]:
        exit()
    pygame.display.update()

    # 2 update
    p_x += 5 * p_vx * p_dx
    p_y += 2 * p_vy * p_dy
    if p_y <= 0 + P_SIZE:
        p_dy = 1
    if p_y >= screen_height - P_SIZE:
        p_dy = -1
    if p_x <= lp_x + LP_WIDTH * 2 and lp_y - LP_WIDTH <= p_y <= lp_y + LP_LENGTH + LP_WIDTH:
        p_dx = 1
    if p_x >= screen_width - RP_WIDTH * 2 - 20 and rp_y - RP_WIDTH <= p_y <= rp_y + RP_LENGTH + RP_WIDTH:
        p_dx = -1
    if p_x < 0:
        p_x = screen_width / 2
        p_y = screen_height / 2
        p_vx = 0.1
        p_vy = 0.1
        p_dx = 1
        r_score += score_increment
        r_text_Surface = font_obj.render(str(r_score), True, (97, 222, 42), None)
        r_text_Rect = r_text_Surface.get_rect()
        r_text_Rect.center = (900, 30)
    if p_x > screen_width:
        p_x = screen_width / 2
        p_y = screen_height / 2
        p_vx = 0.1
        p_vy = 0.1
        p_dx = -1
        l_score += score_increment
        l_text_Surface = font_obj.render(str(l_score), True, (97, 222, 42), None)
        l_text_Rect = l_text_Surface.get_rect()
        l_text_Rect.center = (700, 30)
    if p_vx < 2 and p_vy < 2:
        p_vx += p_a
        p_vy += p_a
    if lp_y < 0:
        lp_y = 0
    if lp_y > screen_height - LP_LENGTH:
        lp_y = screen_height - LP_LENGTH
    if rp_y < 0:
        rp_y = 0
    if rp_y > screen_height - RP_LENGTH:
        rp_y = screen_height - RP_LENGTH

    # 3 output / draw
    window.fill((0, 0, 0))
    pygame.draw.circle(window, (255, 255, 255), (p_x, p_y), P_SIZE)
    pygame.draw.rect(window, (255, 255, 255), (lp_x, lp_y, LP_WIDTH, LP_LENGTH))
    pygame.draw.rect(window, (255, 255, 255), (rp_x, rp_y, RP_WIDTH, RP_LENGTH))
    window.blit(l_text_Surface, l_text_Rect)
    window.blit(r_text_Surface, r_text_Rect)
    pygame.display.flip()
    clock.tick(144)
