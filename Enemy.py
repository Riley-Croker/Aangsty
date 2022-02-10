####
# Imports
####
import pygame

### Global Image Variables ###
fireImg = pygame.image.load('Assets\FireLord.jpg')
waterImg = pygame.image.load('Assets\WaterEnemy.png')
earthImg = pygame.image.load('Assets\EarthEnemy.png')

class Enemy:
    ###Global Class Vars
    health = 5
    width = 100
    height= 150
    speed = 10
    isDead = False

   

#constructor function
    def __init__(self, ax, ay, atype):
        self.x = ax
        self.y =ay
        self.type = atype
        

    
    def render(self, aSurface, atype):
        if(atype == "fire"):
            aSurface.blit(fireImg,(self.x, self.y))
        elif(atype == "water"):
            aSurface.blit(waterImg, (self.x, self.y))
        elif(atype == "earth"):
            aSurface.blit(earthImg, (self.x, self.y))
        


