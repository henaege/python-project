import pygame
from textbox import TextBox
import sys
from textbox_script import input_questions
from scene import Scene
# import classes

def run_game():
    pygame.init()

    screen_size = (1200, 750)
    screen = pygame.display.set_mode(screen_size)
    screen_rect = screen.get_rect()
    pygame.display.set_caption("Mystery House")
    background_img = pygame.image.load("images/house.jpg")
    intro = Scene(screen, background_img)

    # settings = {
    # "text": input_questions["driving_scece1"],
    # "inactive_on_enter": False,
    # }
    # entry = TextBox(rect=(150, 600, 200, 30), **settings)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #     entry.get_event(event)
        # entry.update()
        # screen.blit(background_image, (0, 0))
        # entry.text_display(screen)
        # entry.draw(screen)
        intro.enter()



        pygame.display.flip()

# Final is the user input from the textbox
# def print_on_enter(id, final):
#     print('enter pressed, textbox contains {}'.format(final))


run_game()
