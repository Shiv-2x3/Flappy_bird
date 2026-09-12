# Importing Pygame
import pygame

# Initializing Pygame
pygame.init()


# Game window Assest
Window_height = 700
Window_width = 500

# Creation of Gaming window
screen = pygame.display.set_mode((Window_height , Window_width))
pygame.display.set_caption("Flying Bakugo")

# Background
background_image = pygame.image.load("/home/Projects/Flappy_bird/Images/background Image.bmp").convert()

# Ground Image ( This is not static)
ground_image = pygame.image.load("/home/Projects/Flappy_bird/Images/ Ground Image.bmp").convert_alpha()

# Resized Background Image
reseized_background_image = pygame.transform.scale(
    background_image ,
    (Window_height , Window_width)
)



# Game loop 
running = True #Flag
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # using background in Game Loop
    screen.blit(reseized_background_image , ( 0 , 0))
    screen.blit(ground_image , (0 , Window_width))
    pygame.display.update()

#Quitting Pygame
pygame.quit()