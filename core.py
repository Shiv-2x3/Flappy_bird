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
class Bird(pygame.sprite.Sprite):
    def __init__(self , x , y ):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1 , 4):
            img = pygame.image.load(f'/home/Projects/Flappy_bird/images/bird{num}.png')
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x , y]

    def update(self):
        #Handle animation
        self.counter += 1
        flap_cooldown = 5

        if self.counter > flap_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
        self.image = self.images[self.index]

bird_group = pygame.sprite.Group()
flappy = Bird(100 , int(screen_height / 2))
bird_group.add(flappy)
#flag
running = True

# Game Loop
while running:
    clock.tick(fps)
    screen.blit(bg , (0 , 0 ))
    bird_group.draw(screen)
    bird_group.update()
    screen.blit(ground , (ground_scroll , 768))
    ground_scroll -= scroll_speed
    if abs(ground_scroll) > 35:
        ground_scroll = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()