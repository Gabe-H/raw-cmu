import pygame
from pygame import *

class app():
    def initScreen(self, dims):
        pygame.init()
        return pygame.display.set_mode(dims)

class Rect():
    def __init__(self, screen, left, top, width, height, fill=(0,0,0)):
        pygame.draw.rect(screen, fill, (left, top, width, height))
    
class Circle():
    def __init__(self, screen, centerX, centerY, radius, fill=(0,0,0)):
        pygame.draw.circle(screen, fill, (centerX, centerY), radius)

class Polygon():
    def __init__(self, screen, *points, fill=(0,0,0)):
        pointRange = []
        for p in range(len(points)//2):
            pointRange.append((points[p*2], points[p*2+1]))
        pygame.draw.polygon(screen, fill, pointRange)

class Oval():
    def __init__(self, screen, centerX, centerY, width, height, fill=(0,0,0)):
        # pygame draws like a rectangle, left
        pygame.draw.ellipse(screen, fill, (centerX-(width/2), centerY-(height/2), width, height))

