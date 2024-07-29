import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First Game")

x = 50
y = 50
width = 40
height = 60
vel = 5

run = True

while run:
    pygame.time.delay(100) # This will delay the game the given amount of milliseconds. In our casee 0.1 seconds will be the delay

    for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
        if event.type == pygame.QUIT: # Checks if the red button in the corner of the window is clicked
            run = False  # Ends the game loop
    
    keys = pygame.key.get_pressed()  # This will give us a dictonary where each key has a value of 1 or 0. Where 1 is pressed and 0 is not pressed.

    if keys[pygame.K_LEFT]: # We can check if a key is pressed like this
         x -= vel

    if keys[pygame.K_RIGHT]:
          x += vel

    if keys[pygame.K_UP]:
          y -= vel

    if keys[pygame.K_DOWN]:
          y += vel

    pygame.draw.rect(win, (255,0,0), (x, y, width, height))  #This takes: window/surface, color, rect 
    pygame.display.update() # This updates the screen so we can see our rectangle

pygame.quit()  