import pygame
from textbox import TextBox
import sys
from textbox_script import input_questions
from scene import Scene, DrivingScene, Foyer, Library, Bedroom, Kitchen, Final
from game_function import input_box, get_user_input, check_user_input

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
    entry = TextBox(rect=(680, 700, 200, 30))
    driving_a = DrivingScene(screen, text_box)
    driving_b = DrivingScene(screen, text_box)
    driving_c = DrivingScene(screen, text_box)
    driving_d = DrivingScene(screen, text_box)
    driving_e = DrivingScene(screen, text_box)
    foyer = Foyer(screen, text_box)
    # drivingtext1 set true to display only once in its lifetime in main loop iterations
    drivingtext1 = True
    # drivingtext3 = True
    foyertext1 = True
    foyertext3 = True

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            entry.get_event(event)

        intro.enter()
        if intro.check_scene():
            driving.enter()
            input_box(entry, screen)
            friend_name = get_user_input(entry)
            drivingtext1 = True


            if drivingtext1:
                driving_a.text_generator(screen,"You're driving with your best friend, heading home after a day of hiking.", (100, 460))
                driving_b.text_generator(screen,"Rain is beating hard on the roof of your car, the wipers swishing fast.", (100, 490))
                driving_c.text_generator(screen,"Your GPS takes you to some backroads, empty of light and other cars.", (100, 520))
                driving_d.text_generator(screen,"Suddenly, you and your friend jolt in your seats! You've hit something!", (100, 550))
                #tells main loop to stop entering drivingtext1
                drivingtext1 = False

                #call function again to draw over drivingtext1
                driving.enter()

                drivingtext2 = True

                pygame.time.delay(1000)

                driving_a.text_generator("What do you do? Enter a number:", (100,460))
                driving_b.text_generator("1. Get out of the car and check it out.", (100,490))
                driving_c.text_generator("2. Stay in the car.", (100,520))
                driving_d.text_generator("3. Quit Game. This is too scary.", (100, 550))

                pygame.time.delay(2000)

            # if user_input == 1:
            #     if drivingtext3:
            #         driving_a.text_generator("You leave your car, but see nothing What did you hit?", (100,460))
            #         driving_b.text_generator("When you go back inside the car, it won't start.", (100,490))
            #         driving_c.text_generator("Nothing you true works. Your and your friend try you phones.", (100,520))
            #         driving_d.text_generator("No signal. You see a huge house not too far off, its lights on.", (100, 550))
            #
            #         drivingtext3 = False
            #
            #         driving.enter()
            #
            #         drivingtext4 = True
            #         pygame.time.delay(2000)
            #
            #         driving_a.text_generator("What do you do next? Enter a number:", (100,460))
            #         driving_b.text_generator("1. Go the mansion for help.", (100,490))
            #         driving_d.text_generator("2. Stay in the car.", (100, 550))
            #         driving_d.text_generator("3. Quit game. This is too scary.", (100, 550))
            #
            #         pygame.time.delay(2000)



            # if user_input == 2:
            #
            #     if drivingtext4:
            #         driving_a.text_generator("Your friend says,'That sounded awful.' We should check it out.", (100,460))
            #         driving_b.text_generator("You both leave the car, but see nothing. What did you hit?", (100,490))
            #         driving_c.text_generator("When you back inside, the car won't start. Nothing you try works.", (100,520))
            #         driving_d.text_generator("You try your cell phones. No signal. You see a huge house ahead, its lights on.", (100, 550))
            #
            # if user_input == 3:
            #     sys.exit()
            #
            #     drivingtext4 = False
            #
            #     driving.enter()
            #
            #     drivingtext5 = True
            #     pygame.time.delay(2000)
            #
            #     driving_a.text_generator("What do you do next? Enter a number:", (100,460))
            #     driving_b.text_generator("1. Go the mansion for help.", (100,490))
            #     driving_c.text_generator("2. Quit game. This is too scary.", (100, 550))
            #
            #     pygame.time.delay(2000)
            #
            #         # if user_input == 1 #not sure what do here, call the driving.check_scene() function?
            # if user_input == 3:
            #             sys.exit()
            #


            # driving. text_generator("")
            # pygame.time.delay(60)
            pygame.time.wait(2)



        if driving.check_scene():
            foyer.enter()
            if foyertext1:
                driving_a.text_generator("You enter the house with your friend and ring the bell. No answer.", (100,460))
                driving_b.text_generator("Your friend shrugs and pushes the door. You both enter and see three", (100,490))
                driving_c.text_generator("people standing in the foyer: an elderly man, a woman in a red dress and heels,", (100,520))
                driving_d.text_generator("and a teenage boy in goth makeup.", (100, 550))
                #tells main loop to stop entering foyertext1
                foyertext1 = False

                #call function again to draw over foyertext1
                foyer.enter()

                foyertext2 = True

                pygame.time.delay(1000)


                driving_a.text_generator("What do you do? Enter a number:", (100,460))
                driving_b.text_generator("1. Talk to the elderly man", (100,490))
                driving_c.text_generator("2. Talk to the beautiful woman.", (100,520))
                driving_d.text_generator("3. Talk to the gothic teenager.", (100, 550))

                pygame.time.delay(2000)

                # if user_input == 1:
                #     if foyertext3:
                #         driving_a.text_generator("'Well, hello there! Welcome to my home. I'm Sir Rupert Wilkinson,''", (100,460))
                #         driving_b.text_generator("the old man says. 'What brings you here on such a rainy night as this?'", (100,490))
                #         driving_a.text_generator("You tell him how your car broke down and need to use a phone.", (100,460))
                #         driving_b.text_generator("'That's terrible! Of course you can use my phone, of course!''", (100,490))
                #
                #         foyertext3 = False
                #
                #         foyer.enter()
                #
                #         foyertext4 = True
                #
                #         pygame.time.delay(2000)
                #
                #         driving_a.text_generator("Suddenly the lights flicker off and on! Your friend screams!", (100,460))
                #         driving_b.text_generator("You find your frined splayed on the floor in an X, unconsious.", (100,490))
                #         driving_a.text_generator("You check your friend's pulse. Nothing. You heartbeat spikes.", (100,460))
                #         driving_b.text_generator("You panic and run for the door but it's locked! You turn around.", (100,490))
                #
                #
#         pygame.time.delay(2000)

            # foyer.enter()
            #
            # if foyertext5:
            #     driving_a.text_generator("Sir Wilkinson says,'Now, now. No running away! I'm afraid one", (100,460))
            #     driving_b.text_generator("of use killed your dear friend. Let's play a game, shall we?'", (100,490))
            #     driving_c.text_generator("'If you can figure out which one of is the killer, we will let you go.'", (100,520))
            #     driving_d.text_generator("'However, make the wrong guess and you will die too'", (100, 550))
            #     driving_e.text_generator("'Now, which room shall you enter to look for clues?'")
            #
            #     foyertext5 = False
            #
            #     foyer.enter()
            #
            #     foyertext6 = True
            #     pygame.time.delay(2000)
            #
            #     driving_a.text_generator("Which room will you go to? Enter a number.", (100,460))
            #     driving_b.text_generator("1. Enter the library", (100,490))
            #     driving_c.text_generator("2. Enter the kitchen", (100,520))
            #     driving_d.text_generator("3 Enter the master bedroom", (100, 550))
            #
            #     pygame.time.delay(2000)












        if foyer.check_scene():
            final.enter()



        pygame.display.flip()

# Final is the user input from the textbox
# def print_on_enter(id, final):
#     print('enter pressed, textbox contains {}'.format(final))


run_game()
