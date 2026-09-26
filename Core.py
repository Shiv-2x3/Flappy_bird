# Importing Pygame
import pygame
import random
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

# Variable for flying stuff
flying = False

# Game over variable
Game_over = False

#gaps between the pipe 
pipe_gap = 150


# pipe Frequency 
pipe_frequency = 1500 # Millisecond

last_pipe = pygame.time.get_ticks() - pipe_frequency


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
        self.vert_velocity = 0  # definibg the vertical velocity
        self.clicked = False # discrbing a flag

    def update(self): # This function is inbuild in pygame and updats the animationn as well

        if Game_over == False:
            # Gravity
            self.vert_velocity += 0.5 # Convention here is increment is falling 

            if self.vert_velocity > 5: # handels the override condition
                self.vert_velocity = 5
            
            if self.rect.bottom < 500: # handels the position at bottom
                self.rect.y += int(self.vert_velocity)

            # Velocity (user input)
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True 
                self.vert_velocity = -10

            if pygame.mouse.get_pressed()[0] == 0:
                        self.clicked = False

            self.counter += 1 # Updation of counter ( indicates the number of itteration )
            flap_cooldown = 5 # Indicates the necessary frames

            if self.counter > flap_cooldown: # Condition for updation
                self.counter = 0 
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
            self.image = self.images[self.index]

            # Rotaing the bird 
            self.image = pygame.transform.rotate(self.images[self.index] , self.vert_velocity * -3)
        else:
             self.image = pygame.transform.rotate(self.images[self.index],-90)



# creation of pipe class
class pipe(pygame.sprite.Sprite):
    def __init__(self , x , y, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("/home/Projects/Flappy_bird/Images/pipe.bmp")
        self.rect = self.image.get_rect()
        # for position = 1 is from top and -1 is from bottom
        if position == 1:
            self.image = pygame.transform.flip(self.image ,False , True)
            self.rect.bottomleft = [x , y - int(pipe_gap / 2)]

        if position == -1:
            self.rect.topleft = [x , y+ int(pipe_gap / 2)]

    def update(self):
        self.rect.x -= scroll_speed
        if self.rect.right < 0 :
            self.kill()


# working with bird class
bird_group = pygame.sprite.Group() # Behaves like a list Inbuild funcanality 

flappy = Bird(100 , int(screen.get_height() / 2))  # Creating the usage for bird Class

bird_group.add(flappy) # Added inside bird_group

# Working with pipe class
pipe_group = pygame.sprite.Group()






# Game loop 
running = True #Flag
while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.K_SPACE and flying == False and Game_over == False:
            flying = True

        
            

    # using background in Game Loop
    screen.blit(reseized_background_image , (0 , -100))

    # defining Bird
    bird_group.draw(screen)
    bird_group.update()
    pipe_group.draw(screen)
    pipe_group.update()

    

    # condition when it touches the ground
    if flappy.rect.bottom > 500:
        flying = False
        Game_over = True



    # Ground Image in Game loop
    screen.blit(ground_image, (ground_scroll , 500))


    # look for game collision
    if pygame.sprite.groupcollide(bird_group , pipe_group , False , False) or flappy.rect.top < 0:
        Game_over= True
    # For Moving Ground Image
    ground_scroll -= scroll_speed

    # This conditons just resets the ground_scroll
    if Game_over == False:   
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe >  pipe_frequency:
            pipe_height = random.randint(-100 , 100)
            bottom_pipe = pipe(Window_width , int(screen.get_height() / 2) +  pipe_height, -1)
            top_pipe = pipe(Window_width , int(screen.get_height()/2)+pipe_height ,  1)
            pipe_group.add(bottom_pipe)
            pipe_group.add(top_pipe)
            last_pipe = time_now
        pipe_group.update()
        if abs(ground_scroll) > 35:
            ground_scroll = 0
        pygame.display.update()

#Quitting Pygame
pygame.quit()