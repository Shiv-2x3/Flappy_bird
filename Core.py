# Importing Pygame
import pygame

# Initializing Pygame
pygame.init()

#Frame rate
clock = pygame.time.Clock()
fps = 60

# Game window Assest
Window_height = 900
Window_width = 600

# Creation of Gaming window
screen = pygame.display.set_mode((Window_height , Window_width))
pygame.display.set_caption("Flying Bakugo")

# Background
background_image = pygame.image.load("/home/Projects/Flappy_bird/Images/Free-Nature-Backgrounds-Pixel-Art6(1).bmp").convert()

# Ground Image ( This is not static)
ground_image = pygame.image.load("/home/Projects/Flappy_bird/Images/ Ground Image.bmp").convert()

# Scrolling ground in x direction
ground_scroll = 0
scroll_speed = 3

# Resized Background Image
reseized_background_image = pygame.transform.scale(
    background_image ,
    (Window_height , Window_width)
)

# Bird Class With Sprite Function
class Bird(pygame.sprite.Sprite):
    def __init__(self , x , y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("/home/Projects/Flappy_bird/Images/Bird/bird1.bmp")
        self.rect = self.image.get_rect()
        self.rect.center = [x , y]

bird_group = pygame.sprite.Group() # Behaves like a list Inbuild funcanality 

flappy = Bird(100 , int(screen.get_height() / 2))

bird_group.add(flappy)




# Game loop 
running = True #Flag
while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # using background in Game Loop
    screen.blit(reseized_background_image , (0 , -100))

    # defining Bird
    bird_group.draw(screen)


    # Ground Image in Game loop
    screen.blit(ground_image, (ground_scroll , 500))

    # For Moving Ground Image
    ground_scroll -= scroll_speed

    # This conditons just resets the ground_scroll
    if abs(ground_scroll) > 35:
        ground_scroll = 0
    pygame.display.update()

#Quitting Pygame
pygame.quit()