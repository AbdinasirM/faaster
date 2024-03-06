# Example file showing a basic pygame "game loop"
import pygame 
import Movements
import time as t
import platforms
# pygame setup
pygame.init()

screenWidth  = 1280
screenHeight = 720

screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()
running = True

isJumping = False
jumpCount = 10
m = 1
pos = pygame.Vector2(10, screen.get_height()-25)
rectangle_platforms = platforms.generatePlatforms()  # Call the function to generate platforms

while running:
   #print(pos)
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("White")
    
    # RENDER YOUR GAME HERE
    # flip() the display to put your work on screen
    pygame.draw.circle(screen, "Purple", pos, 40) 

    for rectangle_platform in rectangle_platforms:
            pygame.draw.rect(screen, (255, 0, 0), rectangle_platform)  # Use a tuple for the color

    Movements.BasicMove(pygame=pygame,pos=pos,t=t,isJumping=isJumping,jumpCount=jumpCount,m=m)

    keys = pygame.key.get_pressed()
    if not(isJumping):

         if keys[pygame.K_w]:
             isJumping = True
    if isJumping: 
        if jumpCount >= -10:
            print(jumpCount)

            F =(1 / 2)*m*(jumpCount**2)

            pos.y -= F
            
            jumpCount = jumpCount - 1

            if jumpCount < 0: 
                m = -1
            
            if jumpCount == -11: 

                isJumping = False
                jumpCount = 10
                m = 1

    
    pygame.display.flip()
    
    clock.tick(60)  # limits FPS to 60

pygame.quit()
