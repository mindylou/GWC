# part 1.2
import pygame
import random

# part 1.4a: add screen to scroller method draw
# part 1.4f
from scroller import Scroller as Scroller

# part 2
class Block(pygame.sprite.Sprite):
    
    # part 2.1
    def __init__(self, file_name):
        super.__init__()

        # Loading the sprite from the file
        
        # part 2a-2b
        self.image = pygame.image.load(file_name)

        # part 2c-2d
        # This sets the background of the image.
        # Setting it to white makes it so that it blends in the rest of screen
        self.image.set_colorkey(WHITE)

        self.rect = self.image.get_rect()

# part 1.3
pygame.init()
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])

# part 2.4
all_sprites_list = pygame.sprite.Group()

# part 2.3
player = Block("Melissa.png")

# part 2.5
def make_blocks():
    all_sprites_list.add(player)

# part 1.6a
any_scroller = Scroller(screen_width, 300, screen_height, (255, 100, 100), 2)

# part 1.5a-5b
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

    # part 1.6b
    screen.fill(WHITE)
    
    # part 2.6a
    pos = pygame.mouse.get_pos
    
    # part 2.6b
    player.rect.x = pos[0]
    player.rect.y = pos[1]
    
    # part 1.6c
    any_scroller.draw_buildings(screen)
    any_scroller.move_buildings()
    
    # part 2.6d
    all_sprites_list.draw(screen)
    
    # part 1.5c
    pygame.display.flip()
    clock.tick(60)

# part 1.5d
pygame.quit()
exit()