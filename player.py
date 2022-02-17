import pygame

class Player:
    # Global class vars with constant starting values
    health = 5
    speed = 10
    isDead = False
    canFire = True
    timeSinceLastBullet = 0
    timeBetweenBullets = 1000
    aangClock = pygame.time.Clock()

    # constructor function
    def __init__(self, aX, aY, aImage):
        self.x = aX
        self.y = aY
        self.image = aImage
        self.height = aImage.get_height()
        self.width = aImage.get_width()

    def render(self, aSurface):
        aSurface.blit(self.image, (self.x,self.y))

    def updateTime(self):
        dt = self.aangClock.tick()

        self.timeSinceLastBullet += dt
        if self.timeSinceLastBullet > self.timeBetweenBullets:
            self.canFire = True
            self.timeSinceLastBullet = 0
    def setDead(self, aBool):
        self.isDead = aBool    
