import pygame
import time
from pygame.locals import *

def draw_block():
    screen.fill((100,100,30))
    screen.blit(block, (block_x, block_y))
    pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    screen.fill((100,100,30))
    block = pygame.image.load("resources/block.jpg").convert()
    block_x = 100
    block_y = 100
    screen.blit(block, (block_x, block_y))
    pygame.display.flip()
    pygame.display.set_caption("Snake Game ")
    #time.sleep(6)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                
                if event.key == pygame.K_UP:
                    block_y -= 10
                    draw_block()
                if event.key == pygame.K_DOWN:
                    block_y += 10
                    draw_block()
                if event.key == pygame.K_LEFT:
                    block_x -= 10
                    draw_block()
                if event.key == pygame.K_RIGHT:
                    block_x += 10
                    draw_block()  
            elif event.type == pygame.QUIT:
                running = False
