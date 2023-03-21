import sys
import pygame
from pygame.locals import *

displayX = 800
displayY = 600
grass_position = [0, 0]
ball_position = [displayX/2, displayY/2]

pygame.init()

DISPLAYSURF = pygame.display.set_mode((displayX, displayY))
pygame.display.set_caption('Ball Game')
ball_image = pygame.image.load('ball.png')
ball_surf = ball_image.convert()
grass_image = pygame.image.load('grass.jpg')
grass_surf = grass_image.convert()

ball_velocity = [0, 0]

FPS = 50

timer = pygame.time.Clock()


while True:
    # sprawdzic wejscie (controller)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                ball_velocity[0] += 1
            if event.key == K_LEFT:
                ball_velocity[0] -= 1
            if event.key == K_DOWN:
                ball_velocity[1] += 1
            if event.key == K_UP:
                ball_velocity[1] -= 1
            if event.key == ord(' '):
                ball_velocity = [0, 0]
                ball_position = [displayX/2, displayY/2]
                # zmienic model

    ball_position[0] += ball_velocity[0]
    ball_position[1] += ball_velocity[1]

    # wygenerowac widok
    DISPLAYSURF.blit(grass_surf, grass_position)
    DISPLAYSURF.blit(ball_surf, ball_position)

    pygame.display.update()
    timer.tick(FPS)
