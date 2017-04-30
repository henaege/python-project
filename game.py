import pygame
from textbox import TextBox
import sys
import time
from scene import Scene, DrivingScene, Foyer, Library, Bedroom, Kitchen, Final, moving_scene
from game_function import input_box
from scroll_text import ScrollText
from textbox_script import driving_scene
from puzzles import Library_puzzle

clock = pygame.time.Clock()
def text_generator(screen, string, pos):
        # text = ''
        # for i in range(len(string)):
        #     print 2
        #     text += string[i]
    font = pygame.font.SysFont("Consolas", 40)
    message_display_text = font.render(string, True, (255, 255, 255))
    screen.blit(message_display_text, pos)
        # pygame.display.update(pygame.Rect(100, 460, 10, 10))
        # clock.tick(30)

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
    foyer = Foyer(screen, text_box)
    library_puzzle = Library_puzzle()

    # pass_intro = True
    # drivingtext1 = True
    # drivingtext2 = False
    # foyertext2 = False
    # foyertext1 = True

    while 1:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            entry.get_event(event)

            intro.enter()
        if intro.check_scene():
            driving.enter()
            # if drivingtext1:
                # print 1
                # text_generator(screen, clock, "You're driving with your best friend, heading home after a day of hiking.", (100,460))
                # # text_generator(screen, clock, "Rain is beating hard on the roof of your car, the wipers swishing fast.", (100,490))
                # # text_generator(screen, clock, "Your GPS takes you to some backroads, empty of light and other cars.", (100,520))
                # # text_generator(screen, clock, "Suddenly, you and your friend jolt in your seats! You've hit something!", (100, 550))
                # drivingtext1 = False
                # pygame.time.delay(1000)
                # pygame.display.update()
            # elif drivingtext2:
            #     driving.enter()
            #     text_generator(screen, clock, "What do you do? Enter a number:", (100,460))
            #     text_generator(screen, clock, "1. Get out of the car and check it out.", (100,490))
            #     text_generator(screen, clock, "2. Stay in the car.", (100,520))
            #     text_generator(screen, clock, "3. Quit Game. This is too scary.", (100, 550))
            #     pygame.time.delay(2000)
            #     pygame.time.wait(2)
            input_box(entry, screen)
            driving.next_scene(entry.check_user_input("1"))
            # drivingtext2 = True
            # clock.tick(30)
        if driving.check_scene():
            foyer.enter()
            if moving_scene['library']:
                library.enter()
                if library.puzzle_active:
                    text_generator(screen, "Zkdw jrhv edfn dqg iruwk frqvwdqwob, exw qhyhu lq d vwudljkw olqh?", (200, 300))
                    library_puzzle.check_answer(entry.get_user_input(), "3")
                    if library_puzzle.puzzle_solved:
                        text_generator(screen, "What goes back and forth constantly, but never in a straight line?", (200, 400))
                        library_puzzle.check_answer(entry.get_user_input(), "pendulum")
                        # text_generator(screen, )
                    input_box(entry, screen)
            if moving_scene['bedroom']:
                print 2
                bedroom.enter()
            if moving_scene['kitchen']:
                print 3
                kitchen.enter()
        pygame.display.flip()
        clock.tick(30)

# Final is the user input from the textbox
# def print_on_enter(id, final):
#     print('enter pressed, textbox contains {}'.format(final))


run_game()
