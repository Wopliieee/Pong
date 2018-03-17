import pygame
import time

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
gray = (169,169,169)

display_width = 1000
display_height = 800

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Pong")

font = pygame.font.SysFont(None, 80)

def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [250, 250])

def gameLoop():

    global pos_y_w2, pos_y_w3
    gameExit = False

    pos_x_a = 925
    pos_y_a = 300
    pos_y_a_change = 0
    pos_x_w = 75
    pos_y_w = 300
    pos_y_w_change = 0

    ball_x = 490
    ball_x_change = 0
    ball_y = 290
    ball_y_change = 0

    font = pygame.font.SysFont(None, 200)

    clock = pygame.time.Clock()

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    pos_y_a_change -= 8
                elif event.key == pygame.K_DOWN:
                    pos_y_a_change += 8
                elif event.key == pygame.K_w:
                    pos_y_w_change -= 8
                elif event.key == pygame.K_s:
                    pos_y_w_change += 8
                elif event.key == pygame.K_SPACE:
                    ball_x_change += 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    pos_y_a_change = 0
                elif event.key == pygame.K_w or event.key == pygame.K_s:
                    pos_y_w_change = 0


        if pos_y_a < 0:
            pos_y_a = 0
        elif pos_y_a > 600:
            pos_y_a = 600

        if pos_y_w < 0:
            pos_y_w = 0
        elif pos_y_w > 600:
            pos_y_w = 600

        ball_x2 = ball_x + 10
        ball_y2 = ball_y + 10
        pos_y_a2 = pos_y_a + 120
        pos_y_a3 = pos_y_a - 90
        dol_paletka_a = pos_y_a3 + 100
        gora_paletka_a = pos_y_a2 - 120

        pos_y_w2 = pos_y_w + 120
        pos_y_w3 = pos_y_w - 90

        dol_paletka_w = pos_y_w3 + 100
        gora_paletka_w = pos_y_w2 - 120


        if ball_x2 > 899:
            if ball_y2 > pos_y_a3 and ball_y2 < pos_y_a2:
                ball_x_change -= 10
                if ball_y2 > dol_paletka_a and ball_y2 < pos_y_a2:
                    ball_y_change = 0
                    ball_y_change += 5
                if ball_y2 > pos_y_a3 and ball_y2 < gora_paletka_a:
                    ball_y_change = 0
                    ball_y_change -= 5

        if ball_x2 < 100:
            if ball_y2 > pos_y_w3 and ball_y2 < pos_y_w2:
                ball_x_change += 10
                if ball_y2 > dol_paletka_w and ball_y2 < pos_y_a2:
                    ball_y_change = 0
                    ball_y_change += 5
                if ball_y2 > pos_y_a3 and ball_y2 < gora_paletka_w:
                    ball_y_change = 0
                    ball_y_change -= 5

        if ball_x2 > 920 or ball_x2 < 80:
            gameLoop()

        if ball_y < -80:
            ball_y_change += 5
        elif ball_y > 680:
            ball_y_change -= 5


        ball_x += ball_x_change
        ball_y += ball_y_change
        pos_y_a += pos_y_a_change
        pos_y_w += pos_y_w_change
        gameDisplay.fill(black)
        pygame.draw.rect(gameDisplay, gray, [505, 0, 10, 800])
        pygame.draw.rect(gameDisplay, white, [pos_x_a, pos_y_a, 10, 200])
        pygame.draw.rect(gameDisplay, white, [pos_x_w, pos_y_w, 10, 200])
        screen_text = font.render(".", True, red)
        gameDisplay.blit(screen_text, (ball_x, ball_y))
        pygame.display.update()

        clock.tick(120)

    pygame.quit()
    quit()

gameLoop()

