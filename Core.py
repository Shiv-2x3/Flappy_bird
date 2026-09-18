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
        self.images = [] # Acts as a list and handles the frames of animation
        self.index = 0 # Itreates over the list
        self.counter = 0
        for num in range(1 , 4): # itteration
            img = pygame.image.load(f"/home/Projects/Flappy_bird/Images/Bird/bird{num}.bmp")
            self.images.append(img)
        self.image = pygame.image.load("/home/Projects/Flappy_bird/Images/Bird/bird1.bmp")
        self.rect = self.image.get_rect()
        self.rect.center = [x , y]

    def update(self): # This function is inbuild in pygame and updats the animationn as well
        self.counter += 1 # Updation of counter ( indicates the number of itteration )
        flap_cooldown = 5 # Indicates the necessary frames

        if self.counter > flap_cooldown: # Condition for updation
            self.counter = 0 
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
        self.image = self.images[self.index]

bird_group = pygame.sprite.Group() # Behaves like a list Inbuild funcanality 

flappy = Bird(100 , int(screen.get_height() / 2))  # Creating the usage for bird Class

bird_group.add(flappy) # Added inside bird_group




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
    bird_group.update()


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