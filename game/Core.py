# Importing Pygame
import pygame

# importing bird class
import Bird 
import pipe
import Button
# Importing Randon Library for pipe class
import random

# Initializing Pygame
pygame.init()

# Frame rate
clock = pygame.time.Clock()
fps = 120

# Game window Variables
Window_height = 900 #--> Height
Window_width = 600 #--> Width

# Creation of Gaming window
screen = pygame.display.set_mode((Window_height , Window_width))  # Here The window is created
pygame.display.set_caption("Flying Bakugo") # Sets Caption to screen

# Background
background_image = pygame.image.load("/home/Projects/Flappy_bird/Images/Free-Nature-Backgrounds-Pixel-Art6(1).bmp").convert()

# Ground Image ( This is not static)
ground_image = pygame.image.load("/home/Projects/Flappy_bird/Images/ Ground Image.bmp").convert()

# Scrolling ground in x direction
ground_scroll = 0
scroll_speed = 180  # pixels per second (equivalent to 3 px/frame at 60 FPS)

# Resized Background Image
reseized_background_image = pygame.transform.scale(
    background_image ,
    (Window_height , Window_width)
)

# Variable for flying
flying = False

# Game over variable
Game_over = False

#gaps between the pipe 
pipe_gap = 150

# styling 
font = pygame.font.SysFont("roboto" , 60)
white = (255 , 255 , 255)

# pipe Frequency 
pipe_frequency = 1500 # Millisecond
last_pipe = pygame.time.get_ticks() - pipe_frequency
pipe_pass = False

# Works With score
score = 0

# restart button 
restart_button = pygame.image.load("/home/Projects/Flappy_bird/Images/restart.bmp")

# Function for drawing text
def draw_text(text , font , text_color , x , y):
    img = font.render(text , True , text_color)
    screen.blit(img , (x , y))




# creation of pipe class





    
# working with bird class
bird_group = pygame.sprite.Group() # Behaves like a list Inbuild funcanality 

flappy = Bird(100 , int(screen.get_height() / 2))  # Creating the usage for bird Class

bird_group.add(flappy) # Added inside bird_group

# Working with pipe class
pipe_group = pygame.sprite.Group()


button = Button(screen.get_width() // 2, screen.get_height() // 2, restart_button)



# Game loop 
running = True #Flag
while running:
    dt = min(clock.tick(fps) / 1000.0, 0.05)  # Cap long pauses to avoid physics jumps.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and Game_over
            and button.rect.collidepoint(event.pos)
        ):
            score = 0
            pipe_pass = False
            flying = False
            Game_over = False
            pipe_group.empty()
            ground_scroll = 0
            last_pipe = pygame.time.get_ticks()
            flappy.rect.center = (100, screen.get_height() // 2)
            flappy.y = float(flappy.rect.y)
            flappy.vert_velocity = 0
            flappy.index = 0
            flappy.animation_timer = 0.0
            flappy.clicked = False
            flappy.image = flappy.images[0]
            ground_scroll = 0

        if event.type == pygame.K_SPACE and flying == False and Game_over == False:
            flying = True

        
            

    # using background in Game Loop
    screen.blit(reseized_background_image , (0 , -100))

    # defining Bird
    bird_group.draw(screen)
    bird_group.update(dt)
    pipe_group.draw(screen)

    

    # condition when it touches the ground
    if flappy.rect.bottom > 500:
        flying = False
        Game_over = True



    # Ground Image in Game loop
    screen.blit(ground_image, (round(ground_scroll), 500))


    # Working on Counter
    if len(pipe_group) > 0:
        if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right and pipe_pass == False:
            pipe_pass = True
        if pipe_pass == True:
            if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                score += 1
                pipe_pass = False

    draw_text(str(score) , font , white ,int(screen.get_width() / 2) , 60)


    # look for game collision
    if pygame.sprite.groupcollide(bird_group , pipe_group , False , False) or flappy.rect.top < 0:
        Game_over= True
    # This conditons just resets the ground_scroll
    if Game_over == False:   
        # Move pipes and ground only while the game is active.
        ground_scroll -= scroll_speed * dt
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe >  pipe_frequency:
            pipe_height = random.randint(-100 , 100)
            bottom_pipe = pipe(Window_width , int(screen.get_height() / 2) +  pipe_height, -1)
            top_pipe = pipe(Window_width , int(screen.get_height()/2)+pipe_height ,  1)
            pipe_group.add(bottom_pipe)
            pipe_group.add(top_pipe)
            last_pipe = time_now
        pipe_group.update(dt)
        if abs(ground_scroll) > 35:
            ground_scroll = 0
    if Game_over == True:
        button.draw(screen)
    pygame.display.update()
#Quitting Pygame
pygame.quit()