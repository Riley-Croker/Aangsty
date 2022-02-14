
import pygame 
import random
from Enemy import Enemy
from player import Player 
###########################
######### IMAGES ##########
###########################

startScreen = pygame.image.load('Assets\StartScreen2.png')
startScreenResized = pygame.transform.scale(startScreen, (1200, 650))
aangPic = pygame.image.load('Assets\Aang.png')

###########################
##### Player Stuff ########
###########################

aang = Player(0, 450, aangPic)
player_height = aang.image.get_height()
player_width = aang.image.get_height()

print (player_height)
print (player_width)


##### Make Enemies List ####
enemyTypeList = ["fire", "water", "earth"]
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
            i.render(WINDOW, i.type)
            i.moveEnemy()
            if i.x < 25:
                enemyList.remove(i)
            prevEnemy = i
         


        #render aang
        aang.render(WINDOW)

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

