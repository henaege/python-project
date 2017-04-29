import pygame

def input_box(entry, screen):
    entry.update()
    entry.draw(screen)

def get_user_input(entry):
    return entry.final

def check_user_input(entry, option_list):
    # use for loop and if statement to decide if user has enter the right input
    user_input = get_user_input(entry)
    for option in option_list:
        try:
            if user_input == option:
                pygame.time.wait(2)
                # need to decide what would happen after user enter a input
                pass
        except ValueError:
            # display some message to the user to enter a valid input
            pass
