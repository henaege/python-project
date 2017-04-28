import pygame

button_list = {'start': ['./images/start_button_hover.png', './images/start_button.png'],
        'quit': ['./images/quit_button_hover.png', './images/quit_button.png']
        }
action = ['next', 'quit', 'instruction']


class Scene(object):
<<<<<<< HEAD
    def __init__(self, screen, bg, button, status=False):
=======
    def __init__(self, screen, bg, status=False):
>>>>>>> 17ab679cdcbe49c1288432eb614fafa0b20027c2
        self.screen = screen
        self.bg = bg
        self.status = status

class Intro(Scene):
    def __init__(self):
        super(Intro, self).__init__()
        pass


    def enter(self):
        # while not self.status:
            self.screen.blit(self.bg, (0, 0))
            self.create_button("start", 50, 50, action[0])
            self.create_button("quit", 50, 50, action[1])
            # self.screen.blit(text_box, (240, 600))

<<<<<<< HEAD
    def create_button(self, scene, x, y, action=None):
        start_button = pygame.image.load('./images/start_button.png')
        start_button_hover = pygame.image.load('./images/start_button_hover.png')
        quit_button = pygame.image.load('./images/quit_button.png')
        quit_button_hover = pygame.image.load('./images/quit_button_hover.png')
        instructions_button = pygame.image.load('./images/instructions_button.png')
        instructions_button_hover = pygame.image.load('./images/instructions_button_hover.png')
=======
    def create_button(self, button, x, y, action=None):
        load_button_active = pygame.image.load(button_list[button][0])
        load_button_inactive = pygame.image.load(button_list[button][1])
>>>>>>> 17ab679cdcbe49c1288432eb614fafa0b20027c2
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # print(click)
        if load_button_active.get_rect(left=x, top=y).collidepoint(mouse):
            self.screen.blit(load_button_inactive, (x, y))
            if click[0] == 1 and action != None:
                if action == "next":
                    self.enter()
                    click[0] = False
                if action == "quit":
                    pygame.quit()
                    quit()
        else:
            self.screen.blit(load_button_inactive, (x, y))
