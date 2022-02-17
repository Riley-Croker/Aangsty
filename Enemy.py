####
# Imports
####
import pygame

### Global Image Variables ###
fireImg = pygame.image.load('Assets\FireLord.png')
waterImg = pygame.image.load('Assets\WaterEnemy.png')
earthImg = pygame.image.load('Assets\EarthEnemy.png')

fireImg = pygame.transform.scale(fireImg, (100, 150))
waterImg = pygame.transform.scale(waterImg, (100, 150))
earthImg = pygame.transform.scale(earthImg, (100, 150))

class Enemy:
    ###Global Class Vars
    health = 5
    width = 100
    height= 150
    speed = 5
    isDead = False

   

#constructor function
    def __init__(self, ax, ay, atype):
        self.x = ax
        self.y = ay
        self.type = atype
        self.top = self.y
        self.bottom = self.y + self.width
        self.left = self.x
        self.right = self.x + self.width
        

    
    def render(self, aSurface, atype):
        if(atype == "fire"):
            aSurface.blit(fireImg,(self.x, self.y))
        elif(atype == "water"):
            aSurface.blit(waterImg, (self.x, self.y))
        elif(atype == "earth"):
            aSurface.blit(earthImg, (self.x, self.y))

    def setSpeed(self, aSpeed):
        self.speed = aSpeed

    def moveEnemy(self):
        self.x -= self.speed




        


