
import pygame 
import random
from Enemy import Enemy
from bullet import Bullet
from player import Player 
###########################
######### SOUND ###########
###########################

pygame.mixer.init()

airSound = pygame.mixer.Sound("Assets/air.mp3")
fireSound = pygame.mixer.Sound("Assets/fireballSound.mp3")
waterSound = pygame.mixer.Sound("Assets/water.mp3")
earthSound = pygame.mixer.Sound("Assets/earth.mp3")
azulaScream = pygame.mixer.Sound("Assets/azulaScream.mp3")
fireScream = pygame.mixer.Sound("Assets/fireScream.mp3")
waterScream = pygame.mixer.Sound("Assets/waterScream.mp3")
earthScream = pygame.mixer.Sound("Assets/earthScream.mp3")

###########################
######### IMAGES ##########
###########################

startScreen = pygame.image.load('Assets\StartScreen2.png')
startScreenResized = pygame.transform.scale(startScreen, (1200, 650))
aangPic = pygame.image.load('Assets\Aang.png')
earth = pygame.image.load('Assets\RockProjectile.png')
earthResized = pygame.transform.scale(earth, (100, 100))
water = pygame.image.load('Assets\waterAttack.png')
waterResized = pygame.transform.scale(water, (100, 100))
fire = pygame.image.load('Assets\Fireball.png')
fireResized = pygame.transform.scale(fire, (150, 75))
air = pygame.image.load('Assets\AirSlash.png')
airResized = pygame.transform.scale(air, (100, 100))

###########################
##### Player Stuff ########
###########################

aang = Player(0, 450, aangPic)
player_height = aang.image.get_height()
player_width = aang.image.get_height()



##### Make Enemies List ####
enemyTypeList = ["fire", "water", "earth", "azula"]
levelVal = 10
enemyList = []
reposition = True

## Fills List With Random Enemies Based on Level Enemy Count ###
for i in range(levelVal):
    xPos = (random.randrange(1250, 3000, 50))
    yPos = 500
    enemyType = (random.choice(enemyTypeList))
    enemySpeed = random.randrange(1,3)
    enemy = Enemy( xPos, yPos, enemyType, enemySpeed )
    enemyList.append(enemy)



FPS = 60

WIDTH = 1200
HEIGHT = 650

bulletList = []

# make the game window object
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

# name the game window
pygame.display.set_caption("Aangsty")

# main game function
def main():
    # make a clock object that will be used
    # to make the game run at a consistent framerate
    clock = pygame.time.Clock()
 
    # make a boolean that represents whether the game should continue to run or not
    running = True
    # while the game is running
    while running:
	    # this makes it so this function can run at most FPS times/sec
        clock.tick(FPS)
 
        # for all the game events
        for event in pygame.event.get():
            # if the game is exited out of, then stop running the game
            if event.type == pygame.QUIT:
                running = False
        
        # This fills the game window to be the given RGB color
        WINDOW.fill((0,255,0))
        
        WINDOW.blit(startScreenResized, (0, 0))

        #Renders and moves to the left side of the sceen 
        
        for i in enemyList:
            if(not i.isDead):
                i.render(WINDOW, i.type)
            i.moveEnemy()
            if i.x < 25:
                enemyList.remove(i)
            prevEnemy = i
         


        #render aang and update his timer
        aang.render(WINDOW)
        aang.updateTime()

        #rendering, collision, and move Bullets
        for bullet in bulletList:
            for enemy in enemyList:
                bullet.collision(enemy)
                if enemy.isDead:
                    enemyList.remove(enemy)
                    if(enemy.type == "fire"):
                        fireScream.play()
                    elif(enemy.type == "water"):
                        waterScream.play()
                    elif(enemy.type == "earth"):
                        earthScream.play()
                    elif(enemy.type == "azula"):
                        azulaScream.play()
            if (not bullet.hasMadeContact):
                bullet.render(WINDOW)
            else:
                bulletList.remove(bullet)
            bullet.move()
            if bullet.x >= WINDOW.get_width():
                bulletList.remove(bullet)

        

        # handle player movement
        # this gets a list of booleans showing which keys are currently pressed
        keysPressed = pygame.key.get_pressed()

        # player movement
        if keysPressed[pygame.K_UP] == True and aang.y >= 0:
            aang.y-=5
        elif keysPressed[pygame.K_DOWN] == True and (aang.y + aang.height) <= WINDOW.get_height():
            aang.y+=5
        if keysPressed[pygame.K_LEFT] == True and aang.x >= 0:
            aang.x-=5
        elif keysPressed[pygame.K_RIGHT] == True and (aang.x + aang.width) <= WINDOW.get_width():
            aang.x+=5

        #firing bullets (-50 is half the bullet height, change if bullet height is ever changed)
        if keysPressed[pygame.K_e] == True and aang.canFire:
            bulletList.append(Bullet(aang.x + aang.width,aang.y + aang.height/2-50,"Earth",earthResized))
            aang.canFire = False
            earthSound.play()
        elif keysPressed[pygame.K_w] == True and aang.canFire:
            bulletList.append(Bullet(aang.x + aang.width,aang.y + aang.height/2-50,"Water",waterResized))
            aang.canFire = False
            waterSound.play()
        elif keysPressed[pygame.K_a] == True and aang.canFire:
            bulletList.append(Bullet(aang.x + aang.width,aang.y + aang.height/2-50,"Air",airResized))
            aang.canFire = False
            airSound.play()
        elif keysPressed[pygame.K_f] == True and aang.canFire:
            bulletList.append(Bullet(aang.x + aang.width,aang.y + aang.height/2-50,"Fire",fireResized))
            aang.canFire = False
            fireSound.play()
        


        ## player enemy collision controls
        for i in enemyList:
            if abs((i.x + 50 ) - (aang.x + player_width/2)) < player_width/2:
                 if abs((i.y + 40) - (aang.y + player_height/2)) < player_height/2:
                    aang.setDead(True)
                    print(aang.isDead)
                     
        
        # put code here that should be run every frame
        # of your game             
        pygame.display.update()



main()

