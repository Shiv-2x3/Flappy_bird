#import packages
import pygame
from pygame.locals import *

# initializing pygame 
pygame.init()

#Screen Variables
screen_height = 936
screen_width = 864

ground_scroll = 0
scroll_speed = 4

clock = pygame.time.Clock()
fps = 60
screen = pygame.display.set_mode((screen_width , screen_height))
pygame.display.set_caption("Fallpy Bird")
# Images 
bg = pygame.image.load("/home/Projects/Flappy_bird/images/bglong.png")
ground = pygame.image.load("/home/Projects/Flappy_bird/images/ground.png")


#flag
running = True

# Game Loop
while running:
    clock.tick(fps)
    screen.blit(bg , (0 , 0 ))
    screen.blit(ground , (ground_scroll , 768))
    ground_scroll -= scroll_speed
    if abs(ground_scroll) > 35:
        ground_scroll = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()