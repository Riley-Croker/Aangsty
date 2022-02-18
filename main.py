
import pygame 
import random
from Enemy import Enemy
from bullet import Bullet
from player import Player 
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
level1Screen = pygame.image.load('Assets\EarthScreen.png')
level1ScreenResize =pygame.transform.scale(level1Screen, (1200, 650))

level2Screen = pygame.image.load('Assets\WaterScreen.png')
level2ScreenResize =pygame.transform.scale(level2Screen, (1200, 650))

level3Screen = pygame.image.load('Assets\FireScreen.png')
level3ScreenResize =pygame.transform.scale(level3Screen, (1200, 650))

level4Screen = pygame.image.load('Assets\AirScreen.png')
level4ScreenResize =pygame.transform.scale(level4Screen, (1200, 650))

WinScreen = pygame.image.load('Assets\WinScreen.png')
WinScreenResize =pygame.transform.scale(WinScreen, (1200, 650))

LoseScreen = pygame.image.load('Assets\LoseScreen.png')
LoseScreenResize =pygame.transform.scale(LoseScreen, (1200, 650))

InstructScreen = pygame.image.load('Assets\instructScreen.png')
InstructScreenResize =pygame.transform.scale(InstructScreen, (1200, 650))

###########################
####### Level Setup #######
###########################

bulletList = []

###########################
##### Player Stuff ########
###########################

aang = Player(0, 450, aangPic)
player_height = aang.image.get_height()
player_width = aang.image.get_height()



############################
##### Make Enemies List ####
############################
enemyTypeList = ["fire", "water", "earth", "air"]
enemyNum = 2
enemyList = []
maxSpeed = 3

## Fills List With Random Enemies Based on Level Enemy Count ###
for i in range(enemyNum):
    xPos = (random.randrange(1250, 3000, 50))
    yPos = 500
    enemyType = (random.choice(enemyTypeList))
    enemySpeed = random.randrange(2,maxSpeed)
    enemy = Enemy( xPos, yPos, enemyType, enemySpeed )
    enemyList.append(enemy)

############################
#### Window and Text #######
############################
pygame.init()
FPS = 60
WIDTH = 1200
HEIGHT = 650
font = pygame.font.SysFont('arial', 55)


# make the game window object
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

# name the game window
pygame.display.set_caption("Aangsty")

############################
##### Helper Functions #####
############################


#Renders and moves to the left side of the sceen 
def animateEnemy():
     for i in enemyList:
        i.render(WINDOW, i.type)
        i.moveEnemy()
        if i.x < 0:  
            i.setPostion((random.randrange(1250, 3000, 50)),500)

        ### HERE IS WHERE THE ENEMIES CAN BE REMOVED FROM LIST WHEN HIT
        #if bullet hit detection 
         #enemyList.remove(i)


#rendering and move Bullets
def animateBullets():
    for bullet in bulletList:
        bullet.render(WINDOW)
        bullet.move()
        if bullet.x >= WINDOW.get_width():
            bulletList.remove(bullet)

# handle player movement
# this gets a list of booleans showing which keys are currently pressed
def playerMove():
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
def fireBullets():
    keysPressed = pygame.key.get_pressed()
    if keysPressed[pygame.K_e] == True and aang.canFire:
            bulletList.append(Bullet(aang.x + aang.width,aang.y + aang.height/2-50,"Earth",earthResized))
            aang.canFire = False
    elif keysPressed[pygame.K_w] == True and aang.canFire:
        bulletList.append(Bullet(aang.x + aang.width,aang.y + aang.height/2-50,"Water",waterResized))
        aang.canFire = False
    elif keysPressed[pygame.K_a] == True and aang.canFire:
        bulletList.append(Bullet(aang.x + aang.width,aang.y + aang.height/2-50,"Air",airResized))
        aang.canFire = False
    elif keysPressed[pygame.K_f] == True and aang.canFire:
        bulletList.append(Bullet(aang.x + aang.width,aang.y + aang.height/2-50,"Fire",fireResized))
        aang.canFire = False

# creates a hit box around aang that if crossed by an enemy 
# will cause boolean isDead to turn true and game to end   
# to returns a boolean true when dead and false when alive       
def playerEnemyCollision():
   
    for i in enemyList:
        if abs((i.x + 50 ) - (aang.x + player_width/2)) < player_width/2:
            if abs((i.y + 40) - (aang.y + player_height/2)) < player_height/2:
                aang.setDead(True)
                print(aang.isDead)
       



# main game function
def main():
    # make a clock object that will be used
    # to make the game run at a consistent framerate
    clock = pygame.time.Clock()
    levelVal = 0
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
        
      
    
        #Start Screen Display

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
            if (not bullet.hasMadeContact):
                bullet.render(WINDOW)
            else:
                bulletList.remove(bullet)
            bullet.move()
            if bullet.x >= WINDOW.get_width():
                bulletList.remove(bullet)
        if levelVal == 0:
            # This fills the game window to be the given RGB color
            WINDOW.fill((0,255,0))
            WINDOW.blit(startScreenResized, (0, 0))
            
            
            startMessage = "Press SPACE to play"
            instructMessage = "Press ENTER for instructions "
            start = font.render(startMessage, True, (0,0,0))
            WINDOW.blit(start, (390, 50))

            instruct = font.render(instructMessage, True, (0,0,0))
            WINDOW.blit(instruct, (300, 150))

            keysPressed = pygame.key.get_pressed()
            if keysPressed[pygame.K_SPACE] == True :
                  levelVal = 1
            elif keysPressed[pygame.K_RETURN] == True :
                  levelVal = 7
            
            pygame.display.update()
        
        #Losing Screen 
        elif levelVal == 6: 
            WINDOW.fill((0,255,0))
            WINDOW.blit(LoseScreenResize, (0, 0))

            startMessage = "You Lost"
            start = font.render(startMessage, True, (0,0,0))
            WINDOW.blit(start, (500, 20))
            pygame.display.update()

        #instruction Screen 
        elif levelVal == 7: 
            WINDOW.fill((0,255,0))
            WINDOW.blit(InstructScreenResize, (0, 0))

            startMessage = "Game Play: Press SPACE to return to home screen"
            start = font.render(startMessage, True, (0,0,0))
            WINDOW.blit(start, (100, 20))

            instructM1 = "\n Press W to shoot water element "
            instruct1 = font.render(instructM1, True, (0,0,0))

            instructM2 = "\n Press E to shoot Earth element" 
            instruct2 = font.render(instructM2, True, (0,0,0))

            instructM3 = "\n Press A to shoot air element"
            instruct3 = font.render(instructM3, True, (0,0,0))

            instructM4 = "\n Press F to shoot fire element"
            instruct4 = font.render(instructM4, True, (0,0,0))

            instructM5 = "\n Use Arrow Keys to move"
            instruct5 = font.render(instructM5, True, (0,0,0))

            instructM6 = "\n Each enemy has a corresponding element weakness "
            instruct6 = font.render(instructM6, True, (0,0,0))

            WINDOW.blit(instruct1, (100, 150))
            WINDOW.blit(instruct2, (100, 200))
            WINDOW.blit(instruct3, (100, 250))
            WINDOW.blit(instruct4, (100, 300))
            WINDOW.blit(instruct5, (100, 350))
            WINDOW.blit(instruct6, (100, 400))


            
            keysPressed = pygame.key.get_pressed()
            if keysPressed[pygame.K_SPACE] == True :
                  levelVal = 0
                  pygame.time.delay(200)
            pygame.display.update()

        #First Level Game Running Block
        elif levelVal == 1: 
            WINDOW.fill((0,255,0))
            WINDOW.blit(level1ScreenResize, (0, 0))

            startMessage = "Level 1"
            start = font.render(startMessage, True, (0,0,0))
            WINDOW.blit(start, (500, 20))


            #render aang and update his timer
            aang.render(WINDOW)
            aang.updateTime()
            playerMove()
            animateEnemy()
            animateBullets()
            fireBullets()
            playerEnemyCollision()
           
            if aang.isDead == True: levelVal = 6

            # This sets up the enemy list for the next level # 
            # It also provides a delay for the player to rest #
            if bool(enemyList) == False:
                for i in range(5):
                    xPos = (random.randrange(1250, 3000, 50))
                    yPos = 500
                    enemyType = (random.choice(enemyTypeList))
                    enemySpeed = random.randrange(2,maxSpeed)
                    enemy = Enemy( xPos, yPos, enemyType, enemySpeed )
                    enemyList.append(enemy)
                levelVal = 2
                pygame.time.delay(2000)
            pygame.display.update()

        elif levelVal == 2: 
            WINDOW.fill((0,255,0))
            WINDOW.blit(level2ScreenResize, (0, 0))

            startMessage = "Level 2"
            start = font.render(startMessage, True, (0,0,0))
            WINDOW.blit(start, (500, 20))

            #render aang and update his timer
            aang.render(WINDOW)
            aang.updateTime()
            playerMove()
            animateEnemy()
            animateBullets()
            fireBullets()
            playerEnemyCollision()
            
            if aang.isDead == True:
                levelVal = 6

            
            # This sets up the enemy list for the next level # 
            # It also provides a delay for the player to rest #
            if bool(enemyList) == False:
                for i in range(10):
                    xPos = (random.randrange(1250, 3000, 50))
                    yPos = 500
                    enemyType = (random.choice(enemyTypeList))
                    enemySpeed = random.randrange(2,7)
                    enemy = Enemy( xPos, yPos, enemyType, enemySpeed )
                    enemyList.append(enemy)
                levelVal = 3
                pygame.time.delay(2000)

            pygame.display.update()  

        elif levelVal == 3:
            WINDOW.fill((0,255,0))
            WINDOW.blit(level3ScreenResize, (0, 0))

            startMessage = "Level 3"
            start = font.render(startMessage, True, (0,0,0))
            WINDOW.blit(start, (500, 20))

            #render aang and update his timer
            aang.render(WINDOW)
            aang.updateTime()
            playerMove()
            animateEnemy()
            animateBullets()
            fireBullets()
            playerEnemyCollision()
            
            if aang.isDead == True:
                levelVal = 6

            
            # This sets up the enemy list for the next level # 
            # It also provides a delay for the player to rest #
            if bool(enemyList) == False:
                for i in range(10):
                    xPos = (random.randrange(1250, 3000, 50))
                    yPos = 500
                    enemyType = (random.choice(enemyTypeList))
                    enemySpeed = random.randrange(2,9)
                    enemy = Enemy( xPos, yPos, enemyType, enemySpeed )
                    enemyList.append(enemy)
                pygame.time.delay(2000)
                levelVal = 4

            pygame.display.update()

        elif levelVal == 4:
            WINDOW.fill((0,255,0))
            WINDOW.blit(level4ScreenResize, (0, 0))

            startMessage = "Level 4"
            start = font.render(startMessage, True, (0,0,0))
            WINDOW.blit(start, (500, 20))

            #render aang and update his timer
            aang.render(WINDOW)
            aang.updateTime()
            playerMove()
            animateEnemy()
            animateBullets()
            fireBullets()
            playerEnemyCollision()
            
            if aang.isDead == True:
                levelVal = 6

            
            # This sets up the enemy list for the next level # 
            # It also provides a delay for the player to rest #
            if bool(enemyList) == False:
                for i in range(10):
                    xPos = (random.randrange(1250, 3000, 50))
                    yPos = 500
                    enemyType = (random.choice(enemyTypeList))
                    enemySpeed = random.randrange(2,9)
                    enemy = Enemy( xPos, yPos, enemyType, enemySpeed )
                    enemyList.append(enemy)
                pygame.time.delay(2000)
                levelVal = 5

            pygame.display.update()   


        elif levelVal == 5:
            WINDOW.fill((0,255,0))
            WINDOW.blit(WinScreenResize, (0, 0))
            pygame.display.update()

    

main()

