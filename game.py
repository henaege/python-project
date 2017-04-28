import pygame
import sys
from scene import Scene

pygame.init()

screen_size = (1200, 750)

title_screen = pygame.image.load('./images/house.jpg')
scene1_bg = pygame.image.load('./images/scene1_bg.jpg')
scene2_bg = pygame.image.load('./images/scene2_bg.jpg')
start_button = pygame.image.load('./images/start_button.png')
start_button_hover = pygame.image.load('./images/start_button_hover.png')
quit_button = pygame.image.load('./images/quit_button.png')
quit_button_hover = pygame.image.load('./images/quit_button_hover.png')
instructions_button = pygame.image.load('./images/instructions_button.png')
instructions_button_hover = pygame.image.load('./images/instructions_button_hover.png')
text_box = pygame.image.load('./images/text_box.png')
woman = pygame.image.load('./images/beautiful_woman.png')
elderly_man = pygame.image.load('./images/elderly_man.png')
goth_teen = pygame.image.load('./images/goth_teen.png')



screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Mystery House")
intro = Scene(screen, 'intro', title_screen, start_button, start_button_hover)

def run_game():
    # pygame.init()

    # screen_size = (1200, 750)

    # title_screen = pygame.image.load('./images/house.jpg')
    # scene1_bg = pygame.image.load('./images/scene1_bg.jpg')
    # scene2_bg = pygame.image.load('./images/scene2_bg.jpg')
    # start_button = pygame.image.load('./images/start_button.png')
    # start_button_hover = pygame.image.load('./images/start_button_hover.png')
    # quit_button = pygame.image.load('./images/quit_button.png')
    # quit_button_hover = pygame.image.load('./images/quit_button_hover.png')
    # instructions_button = pygame.image.load('./images/instructions_button.png')
    # instructions_button_hover = pygame.image.load('./images/instructions_button_hover.png')
    # text_box = pygame.image.load('./images/text_box.png')
    # woman = pygame.image.load('./images/beautiful_woman.png')
    # elderly_man = pygame.image.load('./images/elderly_man.png')
    # goth_teen = pygame.image.load('./images/goth_teen.png')



    # screen = pygame.display.set_mode(screen_size)
    # pygame.display.set_caption("Mystery House")
    

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
                
        # pygame.mouse.set_pos(600, 375)
        screen.blit(title_screen, (0, 0))
        # screen.blit(text)
        # mouse = pygame.mouse.get_pos()
        # x = 528
        # y = 520
        # if start_button.get_rect(left=x, top=y).collidepoint(pygame.mouse.get_pos()):
        #     screen.blit(start_button_hover, (528, 520))
        # else:
        #     screen.blit(start_button, (528, 520))


        pygame.display.flip()

# def button(screen, x, y, ic, ac, action=None):
#     mouse = pygame.mouse.get_pos()
#     click = pygame.mouse.get_pressed()
#     # print(click)
#     if ic.get_rect(left=x, top=y).collidepoint(pygame.mouse.get_pos()):
#         screen.blit(ac, (x, y))
#         if click[0] == 1 and action != None:
#             if action == "next":
#                 scene1.enter()
#                 click[0] = False
#             if action == "quit":
#                 pygame.quit()
#                 quit()
#     else:
#         screen.blit(ic, (x, y))





run_game()