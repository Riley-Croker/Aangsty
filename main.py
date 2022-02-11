
import pygame 
import random
from Enemy import Enemy


###########################
######### IMAGES ##########
###########################

startScreen = pygame.image.load('Assets\StartScreen2.png')
startScreenResized = pygame.transform.scale(startScreen, (1200, 650))


##### Make Enemies List ####
enemyTypeList = ["fire", "water", "earth", "air"]
levelVal = 5
enemyList = []

## Fills List With Random Enemies Based on Level Enemy Count ###


for i in range(levelVal):
    xPos = (random.randrange(500, 1000))
    yPos = 650 - 150 
    enemyType = (random.choice(enemyTypeList))
    enemy = Enemy( xPos, yPos, enemyType )
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
            if i.x < 50:
                enemyList.remove(i) 

        # handle player movement
        # this gets a list of booleans showing which keys are currently pressed
        keysPressed = pygame.key.get_pressed()



        
        # put code here that should be run every frame
        # of your game             
        pygame.display.update()




main()