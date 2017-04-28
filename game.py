import pygame
from textbox import TextBox
import sys
from textbox_script import input_questions
from scene import Scene
<<<<<<< HEAD

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
intro = Scene(screen, title_screen, start_button)

def run_game():
    # pygame.init()

    # screen_size = (1200, 750)
git commit
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
=======
# import classes

def run_game():
    pygame.init()

    screen_size = (1200, 750)
    screen = pygame.display.set_mode(screen_size)
    screen_rect = screen.get_rect()
    pygame.display.set_caption("Mystery House")
    background_img = pygame.image.load("images/house.jpg")
    intro = Scene(screen, background_img)
>>>>>>> 17ab679cdcbe49c1288432eb614fafa0b20027c2

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
