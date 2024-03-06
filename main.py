# Example file showing a basic pygame "game loop"
import pygame 
import Movements
import time as t
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

isJumping = False
jumpCount = 10
m = 1
pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

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
