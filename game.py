import pygame
from textbox import TextBox
import sys
from textbox_script import input_questions
from scene import Scene, DrivingScene, Foyer, Library, MasterBedroom

# import classes
def run_game():
    pygame.init()

    screen_size = (1200, 750)
    screen = pygame.display.set_mode(screen_size)
    screen_rect = screen.get_rect()
    pygame.display.set_caption("Mystery House")
    text_box = pygame.image.load('./images/text_box.png')
    intro = Scene(screen)
    driving = DrivingScene(screen, text_box)
    foyer = Foyer(screen, text_box)
    library = Library(screen, text_box)
    bedroom = MasterBedroom(screen, text_box)
    pygame.mixer.init()
    pygame.mixer.music.load('./music/old city theme.ogg')
    pygame.mixer.music.play(-1)
    entry = TextBox(rect=(680, 700, 200, 30))

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            entry.get_event(event)

        intro.enter()
        if intro.check_scene():
            driving.enter()
            driving.input_box(entry)
            friend_name = driving.get_user_input(entry)
            
            # pygame.time.wait(2)
        if driving.check_scene():
            foyer.enter()
        if foyer.check_scene():
            library.enter()




        pygame.display.flip()

# Final is the user input from the textbox
# def print_on_enter(id, final):
#     print('enter pressed, textbox contains {}'.format(final))


run_game()
