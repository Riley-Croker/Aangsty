####
# Imports
####
import pygame
import random

### Global Image Variables ###
fireImg = pygame.image.load('Assets\FireLord.png')
waterImg = pygame.image.load('Assets\WaterEnemy.png')
earthImg = pygame.image.load('Assets\EarthEnemy.png')
airImg = pygame.image.load('Assets\AirEnemy.png')

fireImg = pygame.transform.scale(fireImg, (100, 155))
fireImg = pygame.transform.flip(fireImg, True, False)
waterImg = pygame.transform.scale(waterImg, (100, 165))
earthImg = pygame.transform.scale(earthImg, (100, 150))
airImg = pygame.transform.scale(airImg, (100, 150))

class Enemy:
    ###Global Class Vars
    health = 5
    isDead = False

   

#constructor function
    def __init__(self, ax, ay, atype, aspeed):
        self.x = ax
        self.y =ay
        self.type = atype
        self.speed = aspeed

        

    
    def render(self, aSurface, atype):
        if(atype == "fire"):
            aSurface.blit(fireImg,(self.x, self.y))
        elif(atype == "water"):
            aSurface.blit(waterImg, (self.x, self.y))
        elif(atype == "earth"):
            aSurface.blit(earthImg, (self.x, self.y))
        elif(atype == "air"):
            aSurface.blit(airImg, (self.x, self.y))

    def setSpeed(self, aSpeed):
        self.speed = aSpeed

    def moveEnemy(self):
        self.x -= self.speed

    def setDead(self, aBool):
        self.isDead = aBool
  







        


