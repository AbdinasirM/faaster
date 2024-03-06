# import pygame
# import random

# # a function that returns random rectangles as a platform
# def generatePlatforms():    
#     rectangle_platforms = []
#     for _ in range(10):
#         rectangle_platform = pygame.Rect(random.randint(100, 700), random.randint(100, 500), 75, 75)
#         rectangle_platforms.append(rectangle_platform)
#     return rectangle_platforms



# platforms.py

# platforms.py
# platforms.py

# platforms.py

import pygame
import random

# a function that returns ordered rectangles as a platform
def generatePlatforms():    
    rectangle_platforms = []
    spacing = 60  # Adjust the spacing between rectangles
    initial_height = 620  # Adjust the initial height
    
    for i in range(10):
        # Set the x-coordinate based on the spacing
        # Set the y-coordinate based on the initial height and decrement the y-coordinate for each iteration
        rectangle_platform = pygame.Rect(i * spacing, initial_height - 50 * (i + 1), 50, 50 * (i + 1))
        rectangle_platforms.append(rectangle_platform)
    
    return rectangle_platforms
