from turtle import speed
import pygame

class Bullet:
    speed = 5
    hasMadeContact = False   

    # constructor function CHANGE TO NO IMAGE ONCE GOT IMAGES
    def __init__(self, aX, aY, aType, aImage):
        self.x = aX
        self.y = aY
        self.type = aType
        self.image = aImage
        self.height = aImage.get_height()
        self.width = aImage.get_width()

    def render(self, aSurface):
        aSurface.blit(self.image, (self.x,self.y))

    def move(self):
        self.x += self.speed