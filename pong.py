import pygame
import random as random

pygame.init()

SCREEN_SIZE_X = 700
SCREEN_SIZE_Y = 400
BALL_SIZE = 10
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 90
font = pygame.font.SysFont("Arial", 50)


direction = 0

player1_points = 0
player2_points = 0

ball_position = [int(SCREEN_SIZE_X/2), int(SCREEN_SIZE_Y/2)]
ball_velocity = [10, -10]

paddle1_position = [0, 1]
paddle2_position = [SCREEN_SIZE_X - PADDLE_WIDTH, SCREEN_SIZE_Y - PADDLE_HEIGHT - 1]

paddle1_velocity = [15, -15]
paddle2_velocity = [15, -15]

paddle1_movement = [False, False]
paddle2_movement = [False, False]




gameDisplay = pygame.display.set_mode((SCREEN_SIZE_X, SCREEN_SIZE_Y))
clock = pygame.time.Clock()

while True:
    text1 = font.render((str(player1_points)), True, (255,255,255))
    text2 = font.render((str(player2_points)), True, (255,255,255))
    if player1_points > 10:
        text3 = font.render("Player 1 won",True, (255,255,255))
    elif player2_points > 10:
        text3 = font.render("Player 2 won",True, (255,255,255))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
                #ruch paletka 1
            elif event.key == pygame.K_UP:
                paddle1_movement[0] = True
            elif event.key == pygame.K_DOWN:
                paddle1_movement[1] = True
                #ruch paletka 2
            elif event.key == pygame.K_w:
                paddle2_movement[0] = True
            elif event.key == pygame.K_s:
                paddle2_movement[1] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                paddle1_movement[0] = False
            elif event.key == pygame.K_DOWN:
                paddle1_movement[1] = False
                #ruch paletka 2
            elif event.key == pygame.K_w:
                paddle2_movement[0] = False
            elif event.key == pygame.K_s:
                paddle2_movement[1] = False



    ball_position[0] += ball_velocity[0]
    ball_position[1] += ball_velocity[1]

#poruszanie sie paletek
    if paddle1_movement[0] == True:
        paddle1_position[1] -= paddle1_velocity[0]
    elif paddle1_movement[1] == True:
        paddle1_position[1] -= paddle1_velocity[1]

    if paddle2_movement[0] == True:
        paddle2_position[1] -= paddle2_velocity[0]
    elif paddle2_movement[1] == True:
        paddle2_position[1] -= paddle2_velocity[1]

#blokada zeby pilka sie odbiala od scian
    if ball_position[1] < BALL_SIZE/2:
        ball_velocity[1] *= -1
    if ball_position[1] > SCREEN_SIZE_Y - BALL_SIZE :
        ball_velocity[1] *= -1


#blokada zeby paletki nie wychodzily za plansze
    if paddle1_position[1] < 1:
        paddle1_position[1] = 0
    if paddle2_position[1] < 1:
        paddle2_position[1] = 0

    if paddle1_position[1] > SCREEN_SIZE_Y - PADDLE_HEIGHT:
        paddle1_position[1] = SCREEN_SIZE_Y - PADDLE_HEIGHT
    if paddle2_position[1] > SCREEN_SIZE_Y - PADDLE_HEIGHT:
        paddle2_position[1] = SCREEN_SIZE_Y - PADDLE_HEIGHT


    #zdobywanie punktow
    elif ball_position[0] < BALL_SIZE - 10:
        direction =  random.random()
        if direction > 0.5:
            ball_velocity[0] *= -1
        else:
            pass
        player2_points += 1
        ball_position = [int(SCREEN_SIZE_X/2), int(SCREEN_SIZE_Y/2)]

    elif ball_position[0] > SCREEN_SIZE_X:
        direction =  random.random()
        if direction > 0.5:
            ball_velocity[0] *= -1
        else:
            pass
        player1_points += 1
        ball_position = [int(SCREEN_SIZE_X/2), int(SCREEN_SIZE_Y/2)]


    if ball_position[0] - BALL_SIZE == paddle1_position[0]:
        ball_velocity[1] *= -1



    gameDisplay.fill((0,0,0))
    pygame.draw.circle(gameDisplay, (255,255,255), ball_position, BALL_SIZE)
    pygame.draw.rect(gameDisplay, (255,255,255), (paddle1_position[0],paddle1_position[1],PADDLE_WIDTH,PADDLE_HEIGHT))
    pygame.draw.rect(gameDisplay, (255,255,255), (paddle2_position[0],paddle2_position[1],PADDLE_WIDTH,PADDLE_HEIGHT))
    gameDisplay.blit(text1, (100,100))
    gameDisplay.blit(text2, (570,100))

    pygame.display.update()
    clock.tick(15)
