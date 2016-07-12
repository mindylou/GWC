# part 1.2: At the top import random and pygame modules
import pygame
import random

# part 1.4a: Add screen to scroller method draw

# part 1.4f: At the top of runner_game.py (below the import statements for pygame and random), you will import city scroller
from scroller import Scroller as Scroller

# part 1.3:
# a. Initialize Pygame by calling init
# b. Create screen_width and screen_height variables.
# c. Create a screen variable so your program has a surface to draw on.
pygame.init()
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])

# part 1.6a: Using the Scroller class that you imported, make three scrolling backgrounds.
any_scroller = Scroller(screen_width, 300, screen_height, (255, 100, 100), 2)

# part 1.5a-5b: Write a basic game loop. Make sure to include a way to exit out of the loop
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
        # optional:
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and can_restart:
                score = 0
                lives = 5
                level = 1
                make_sprites(level)
                can_restart = False
            elif event.key == pygame.K_n and next_level:
                lives = 5
                level += 1
                make_sprites(level)
                next_level = False

    # part 1.6b: Give the screen a background color.
    screen.fill(WHITE)
    
    # part 1.6c: Using the instances of the Scroller class you created earlier draw the buildings to the screen and move the buildings.
    any_scroller.draw_buildings(screen)
    any_scroller.move_buildings()

    # part 1.5c: Make sure to include the code that flips screen and the code that controls how many times the clock ticks.
    pygame.display.flip()
    clock.tick(60)

# part 1.5d:After the loop make sure to write pygame.quit() and then exit()
pygame.quit()
exit()