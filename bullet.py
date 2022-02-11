from turtle import speed
import pygame

class Bullet:
    speed = 5
    hasMadeContact = False

    # constructor function CHANGE TO NO IMAGE ONCE GOT IMAGES
    def __init__(self, aX, aY, aType):
        self.x = aX
        self.y = aY
        self.type = aType
        #self.image = aImage
        #self.height = aImage.get_height()
        #self.width = aImage.get_width()

    def render(self, aSurface):
        if self.type == "Earth":
            tempColor = (255,215,0)
        elif self.type == "Water":
            tempColor = (0,0,255)
        elif self.type == "Fire":
            tempColor = (255,0,0)
        else:
            tempColor = (255,255,255)
        playerRect = pygame.Rect(self.x, self.y, 50, 50)
        pygame.draw.rect(aSurface, tempColor, playerRect)

    def move(self):
        self.x += self.speed