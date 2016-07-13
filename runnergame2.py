# part 1.2
import pygame
import random

# part 1.4f
from scroller import Scroller as Scroller

class Block(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        # part 2.1
        super().__init__()

        # part 2.2a-b
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        
        # part 2.2c-2d
        self.rect = self.image.get_rect()
        self.rect.x = screen_width

            
# part 1.3
pygame.init()
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])

# part 2.4
all_sprites_list = pygame.sprite.Group()

# part 2.3
player = Block(RED, 20, 15)


def make_blocks():
    # part 2.5
    all_sprites_list.add(player)
    
# part 1.6a
any_scroller = Scroller(screen_width, 300, screen_height, (255, 100, 100), 2)

# part 1.5a-5b
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
        # optional
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and can_restart:
                score = 0
                lives = 5
                all_sprites_list.empty()
                make_blocks()
                can_restart = False

# part 1.6b
    screen.fill(WHITE)

# part 2.6a
    pos = pygame.mouse.get_pos()

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

