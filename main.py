# Example file showing a basic pygame "game loop"
import pygame;
import platforms
from platforms import generatePlatforms
# pygame setup
pygame.init()

screenWidth  = 1280
screenHeight = 720

screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()
running = True


pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
rectangle_platforms = generatePlatforms()  # Call the function to generate platforms

while running:
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

    if pygame.key.get_pressed()[pygame.K_w]: 
       #pygame.draw.circle(screen, "Purple", pos + (20,10), 40) 
        pos.y += -10
    pygame.display.flip()
    
    clock.tick(60)  # limits FPS to 60

pygame.quit()
