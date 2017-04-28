import pygame
import sys

def run_game():
    pygame.init()

    screen_size = (1200, 750)

    background_image = pygame.image.load('./images/house.jpg')

    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Mystery House")

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.blit(background_image, (0, 0))


        pygame.display.flip()

run_game()