import pygame
from textbox import TextBox
import sys
from textbox_script import input_questions
from scene import Scene, DrivingScene, Foyer, Library, Bedroom, Kitchen, Final
from game_function import input_box, get_user_input, check_user_input
from scroll_text import ScrollText

# import classes
def run_game():
    pygame.init()

    screen_size = (1200, 750)
    screen = pygame.display.set_mode(screen_size)
    screen_rect = screen.get_rect()
    pygame.display.set_caption("Mystery House")
    text_box = pygame.image.load('./images/text_box.png')
    clock = pygame.time.Clock()
    intro = Scene(screen)
    driving = DrivingScene(screen, text_box)
    foyer = Foyer(screen, text_box)
    library = Library(screen, text_box)
    bedroom = Bedroom(screen, text_box)
    kitchen = Kitchen(screen, text_box)
    final = Final(screen, text_box)
    pygame.mixer.init()
    pygame.mixer.music.load('./music/old city theme.ogg')
    pygame.mixer.music.play(-1)
    entry = TextBox(rect=(680, 700, 200, 30))
    message = (
        ScrollText(screen, "You're driving with your best friend, heading home after a day of hiking.", 400, pygame.Color(255,255,0)),
        )
    fps = 25
    foyer = Foyer(screen, text_box)

    while 1:
        clock.tick(fps)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            entry.get_event(event)

        intro.enter()
        if intro.check_scene():
            driving.enter()
            for thing in message:
                thing.update()

            # driving.text_generator("You're driving with your best friend, heading home after a day of hiking.", (100, 300))
            # driving.text_generator("Rain is beating hard on the roof of your car, the wipers swishing fast.", (100,400))
            # driving.text_generator("Your GPS takes you to some backroads, empty of light and other cars.", (100,500))
            # driving.text_generator("Suddenly, you and your friend jolt in your seats! You've hit something!", (100, 600))
            #     #tells main loop to stop entering drivingtext1

                #call function again to draw over drivingtext1

            # driving.text_generator("What do you do? Enter a number:", (100,460))
            # driving.text_generator("1. Get out of the car and check it out.", (100,490))
            # driving.text_generator("2. Stay in the car.", (100,520))
            # driving.text_generator("3. Quit Game. This is too scary.", (100, 550))

            # pygame.time.wait(2)
        if driving.check_scene():
            foyer.enter()

        if driving.check_scene():
            foyer.enter()

        if foyer.check_scene():
            library.enter()
            input_box(entry)




        pygame.display.flip()

# Final is the user input from the textbox
# def print_on_enter(id, final):
#     print('enter pressed, textbox contains {}'.format(final))


run_game()
