from turtle import speed
import pygame

class Bullet:
    speed = 5
    hasMadeContact = False   

    # constructor function
    def __init__(self, aX, aY, aType, aImage):
        self.x = aX
        self.y = aY
        self.type = aType
        self.image = aImage
        self.height = aImage.get_height()
        self.width = aImage.get_width()
        self.top = self.y
        self.bottom = self.y + self.height
        self.left = self.x
        self.right = self.x + self.width

    def render(self, aSurface):
        aSurface.blit(self.image, (self.x,self.y))

    def move(self):
        self.x += self.speed
        self.left = self.x
        self.right = self.x + self.width

    def collision(self, enemy):
        # collisions
        if self.bottom >= enemy.top and self.top <= enemy.bottom and self.right >= enemy.left and self.left <= enemy.right: 
            self.hasMadeContact = True
            #Typing
            if(self.type == "Fire" and enemy.type == "earth") or (self.type == "Water" and enemy.type == "fire") or (self.type == "Earth" and enemy.type == "water"):
                enemy.setDead(True)