import pygame

class Player:
    # Global class vars with constant starting values
    health = 5
    speed = 10
    isDead = False

    # constructor function
    def __init__(self, aX, aY, aImage):
        self.x = aX
        self.y = aY
        self.image = aImage
        self.height = aImage.get_height()
        self.width = aImage.get_width()

    def render(self, aSurface):
        aSurface.blit(self.image, (self.x,self.y))

    def setDead(self, aBool):
        self.isDead = aBool    