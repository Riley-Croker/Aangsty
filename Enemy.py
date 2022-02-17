####
# Imports
####
import pygame
import random

### Global Image Variables ###
fireImg = pygame.image.load('Assets\FireLord.png')
waterImg = pygame.image.load('Assets\WaterEnemy.png')
earthImg = pygame.image.load('Assets\EarthEnemy.png')
azulaImage = pygame.image.load('Assets\Azula.png')

fireImg = pygame.transform.scale(fireImg, (100, 155))
fireImg = pygame.transform.flip(fireImg, True, False)
waterImg = pygame.transform.scale(waterImg, (100, 165))
earthImg = pygame.transform.scale(earthImg, (100, 150))
azulaImage = pygame.transform.scale(azulaImage, (100, 150))
azulaImage = pygame.transform.flip(azulaImage, True, False)

class Enemy:
    ###Global Class Vars
    health = 5
    isDead = False

   

#constructor function
    def __init__(self, ax, ay, atype, aspeed):
        self.x = ax
        self.y = ay
        self.type = atype
        self.speed = aspeed
        if(atype == "fire"):
            self.width = 100
            self.height = 155
        elif(atype == "water"):
            self.width = 100
            self.height = 165
        elif(atype == "earth"):
            self.width = 100
            self.height = 150
        elif(atype == "azula"):
            self.width = 100
            self.height = 150
        self.top = self.y
        self.bottom = self.y + self.height
        self.left = self.x
        self.right = self.x + self.width
        

    
    def render(self, aSurface, atype):
        if(atype == "fire"):
            aSurface.blit(fireImg,(self.x, self.y))
        elif(atype == "water"):
            aSurface.blit(waterImg, (self.x, self.y))
        elif(atype == "earth"):
            aSurface.blit(earthImg, (self.x, self.y))
        elif(atype == "azula"):
            aSurface.blit(azulaImage, (self.x, self.y))

    def setSpeed(self, aSpeed):
        self.speed = aSpeed

    def moveEnemy(self):
        self.x -= self.speed
        self.left = self.x
        self.right = self.x + self.width

    def setDead(self, aBool):
        self.isDead = aBool
  







        


