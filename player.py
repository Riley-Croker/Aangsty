import pygame

class Player:
    # Global class vars with constant starting values
    health = 5
    width = 100
    height = 100
    speed = 10
    isDead = False

    # constructor function
    def __init__(self, aX, aY, aImage):
        self.x = aX
        self.y = aY
        self.image = aImage

    def render(self, aSurface):
        aSurface.blit(self.image, (self.x,self.y))