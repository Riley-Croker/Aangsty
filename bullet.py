from turtle import speed
import pygame

class Bullet:
    speed = 5
    hasMadeContact = False   
    earth = pygame.image.load('Assets\RockProjectile.png')
    earthResized = pygame.transform.scale(earth, (50, 50))
    water = pygame.image.load('Assets\waterAttack.png')
    waterResized = pygame.transform.scale(water, (50, 50))
    fire = pygame.image.load('Assets\Fireball.png')
    fireResized = pygame.transform.scale(fire, (50, 50))
    air = pygame.image.load('Assets\Aang.png')
    airResized = pygame.transform.scale(air, (50, 50))

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
            tempPic = self.earthResized
        elif self.type == "Water":
            tempPic = self.waterResized
        elif self.type == "Fire":
            tempPic = self.fireResized
        else:
            tempPic = self.airResized
        aSurface.blit(tempPic, (self.x,self.y))

    def move(self):
        self.x += self.speed