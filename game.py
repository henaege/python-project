import pygame
from textbox import TextBox
import sys
from textbox_script import input_questions
from scene import Scene, DrivingScene, Foyer, Library, Bedroom, Kitchen, Final
from puzzles import *

# import classes
def run_game():
    pygame.init()

    screen_size = (1200, 750)
    screen = pygame.display.set_mode(screen_size)
    screen_rect = screen.get_rect()
    pygame.display.set_caption("Mystery House")
    text_box = pygame.image.load('./images/text_box.png')
    final_text_box = pygame.image.load('./images/final_text_box.png')
    intro = Scene(screen)
    driving = DrivingScene(screen, text_box)
    foyer = Foyer(screen, text_box)
    library = Library(screen, text_box)
    bedroom = Bedroom(screen, text_box)
    kitchen = Kitchen(screen, text_box)
    final = Final(screen, final_text_box)
    pygame.mixer.init()
    pygame.mixer.music.load('./music/old city theme.ogg')
    pygame.mixer.music.play(-1)

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
        if intro.check_scene():
            driving.enter()
            pygame.time.wait(2)
        if driving.check_scene():
            foyer.enter()
        if foyer.check_scene():
            final.enter()
        


        pygame.display.flip()

# Final is the user input from the textbox
# def print_on_enter(id, final):
#     print('enter pressed, textbox contains {}'.format(final))


run_game()