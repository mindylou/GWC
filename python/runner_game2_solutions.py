# part 1.2: At the top import random and pygame modules
import pygame
import random

# part 1.4a: Add screen to scroller method draw

# part 1.4f: At the top of runner_game.py (below the import statements for pygame and random), you will import city scroller

from scroller import Scroller as Scroller

# part 2:

class Block(pygame.sprite.Sprite):
    
    # part 2.1
    '''
    Create a class called 'RunnerSprite' that inherits from 'pygame.sprite.Sprite.' This sprite will represent the player character.
    The Sprite class contains methods that draw an object and check if it is colliding with another object.
    This game requires us to check whether two sprites are colliding and to keep track of how many times the sprites have collided. 
    In the RunnerSprite constructor, make sure to call the parent class constructor.
    The runner sprite will need to be a color and a size. Pass those attributes in as parameters to the constructor.
    '''
    def __init__(self, file_name):
        super.__init__()

        # Loading the sprite from the file
        
        # part 2a-2b: To give an image attribute, set self.image to an instance of the pygame.Surface and pass in the width and height parameters.
        # Give the image a color by calling the fill method on self.image and passing in the color parameter.
        self.image = pygame.image.load(file_name)

        # part 2c-2d: To set the self.rect call the get_rect function on self.image attribute.
        # This is important because without the self.image property the sprite won't be able to be drawn on the screen, and without the self.rect we won't be able to move it.

        # This sets the background of the image.
        # Setting it to white makes it so that it blends in the rest of screen
        self.image.set_colorkey(WHITE)

        self.rect = self.image.get_rect()

# part 1.3:
# a. Initialize Pygame by calling init
# b. Create screen_width and screen_height variables.
# c. Create a screen variable so your program has a surface to draw on.
pygame.init()
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])

# part 2.4: Create a sprite group to hold all the sprites our game is going to have in a variable called all_sprites_list.
all_sprites_list = pygame.sprite.Group()

# part 2.3: To create a player, create a variable that is set to an instance of the RunnerSprite class.
player = Block("Melissa.png")

# part 2.5: Add your player to the all_sprites_list.
def make_blocks():
    all_sprites_list.add(player)

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
    
    # part 2.6a: Get the position of the mouse.
    pos = pygame.mouse.get_pos
    
    # part 2.6b: The rect attribute of your RunnerSprites class also has its own attributes.
    # They can be used to set the position of any instance of that class.
    # Since your player is an instance of the RunnerSprites class we can use its rect attribute to set its position.
    # You can find out about the attributes of the rect attribute here. (Be sure to check out the x, y, midright and center attributes).
    # part 2.6c: Set the position of your player to the position of the mouse you got earlier.
    
    player.rect.x = pos[0]
    player.rect.y = pos[1]
    
    # part 1.6c: Using the instances of the Scroller class you created earlier draw the buildings to the screen and move the buildings.
    any_scroller.draw_buildings(screen)
    any_scroller.move_buildings()
    
    # part 2.6d: BELOW the code that draws the scrolling background call the draw method on your all_sprites_list passing in the global screen variable.
    all_sprites_list.draw(screen)
    
    # part 1.5c: Make sure to include the code that flips screen and the code that controls how many times the clock ticks.
    pygame.display.flip()
    clock.tick(60)

# part 1.5d:After the loop make sure to write pygame.quit() and then exit()
pygame.quit()
exit()