from Drawing import *
import pygame

screen = app().initScreen((400,400))

Rect(screen, 100, 100, 50, 50, fill=(255, 255, 0))
Circle(screen, 250, 250, 50, fill=(255, 0, 0))


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()