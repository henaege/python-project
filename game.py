import pygame
import sys

def run_game():
    pygame.init()

    screen_size = (1200, 750)

    background_image = pygame.image.load('./images/house.jpg')
    start_button = pygame.image.load('./images/start_button.png')
    start_button_hover = pygame.image.load('./images/start_button_hover.png')
    quit_button = pygame.image.load('./images/quit_button.png')
    quit_button_hover = pygame.image.load('./images/quit_button_hover.png')

    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Mystery House")
    

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
                
        # pygame.mouse.set_pos(600, 375)
        screen.blit(background_image, (0, 0))
        # mouse = pygame.mouse.get_pos()
        # x = 528
        # y = 520
        # if start_button.get_rect(left=x, top=y).collidepoint(pygame.mouse.get_pos()):
        #     screen.blit(start_button_hover, (528, 520))
        # else:
        #     screen.blit(start_button, (528, 520))
        button(screen, 528, 520, start_button, start_button_hover, "print")
        button(screen, 528, 610, quit_button, quit_button_hover, "quit")


        pygame.display.flip()

def button(screen, x, y, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print(click)
    if ic.get_rect(left=x, top=y).collidepoint(pygame.mouse.get_pos()):
        screen.blit(ac, (x, y))
        if click[0] == 1 and action != None:
            if action == "print":
                print_message()
            elif action == "quit":
                pygame.quit()
                quit()
    else:
        screen.blit(ic, (x, y))

def print_message():
    print("button clicked!")

run_game()