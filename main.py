import pygame
from Enemy import Enemy
from bullet import Bullet
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

aang = Player(0,0,aangPic)


##### Make Enemies ####
fireEnemy =  Enemy(200, 200, "fire")
waterEnemy = Enemy(0,0, "water")
earthEnemy = Enemy(100, 100, "earth")


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
            
        #renders the enemies
        fireEnemy.render(WINDOW, "fire")
        waterEnemy.render(WINDOW, "water")
        earthEnemy.render(WINDOW, "earth")

        #render aang
        aang.render(WINDOW)

        #rendering and move Bullets
        for bullet in bulletList:
            bullet.render(WINDOW)
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

        #firing bullets
        if keysPressed[pygame.K_e] == True:
            bulletList.append(Bullet(aang.x + aang.width,aang.y + aang.height/2,"Earth"))
        elif keysPressed[pygame.K_w] == True:
            bulletList.append(Bullet(aang.x + aang.width,aang.y + aang.height/2,"Water"))
        elif keysPressed[pygame.K_a] == True:
            bulletList.append(Bullet(aang.x + aang.width,aang.y + aang.height/2,"Air"))
        elif keysPressed[pygame.K_f] == True:
            bulletList.append(Bullet(aang.x + aang.width,aang.y + aang.height/2,"Fire"))
        
        
        # put code here that should be run every frame
        # of your game             
        pygame.display.update()




main()