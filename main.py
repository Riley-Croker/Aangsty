import pygame 
from Enemy import Enemy


###########################
######### IMAGES ##########
###########################

startScreen = pygame.image.load('Assets\StartScreen2.png')
startScreenResized = pygame.transform.scale(startScreen, (1200, 650))


##### Make Enemies ####
fireEnemy =  Enemy(200, 200, "fire")
waterEnemy = Enemy(0,0, "water")
earthEnemy = Enemy(100, 100, "earth")


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

            
        #renders the enemies
        fireEnemy.render(WINDOW, "fire")
        waterEnemy.render(WINDOW, "water")
        earthEnemy.render(WINDOW, "earth")

        # handle player movement
        # this gets a list of booleans showing which keys are currently pressed
        keysPressed = pygame.key.get_pressed()



        
        # put code here that should be run every frame
        # of your game             
        pygame.display.update()




main()