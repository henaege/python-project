import pygame


button_list = {'start': ['./images/start_button_hover.png', './images/start_button.png'],
        'quit': ['./images/quit_button_hover.png', './images/quit_button.png'],
        'instruction': ['./images/Instructions_button_hover.png', './images/Instructions_button.png']
        }
action = ['next', 'quit', 'instruction']


class Scene(object):
    def __init__(self, screen, scene_on=False):
        self.screen = screen
        self.bg = pygame.image.load("images/house.jpg")
        self.scene_on = scene_on

    def enter(self):
        # while not self.status:
        self.screen.blit(self.bg, (0, 0))
        self.create_button("start", 400, 500, action[0])
        self.create_button("quit", 400, 600, action[1])
            # self.screen.blit(text_box, (240, 600))

    def check_scene(self):
        return self.scene_on

    def create_button(self, button, x, y, action=None):
        load_button_active = pygame.image.load(button_list[button][0])
        load_button_inactive = pygame.image.load(button_list[button][1])
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # print(click)
        if load_button_inactive.get_rect(left=x, top=y).collidepoint(mouse):
            self.screen.blit(load_button_active, (x, y))
            if click[0] == 1 and action != None:
                if action == "next":
                    self.scene_on = True
                if action == "quit":
                    pygame.quit()
                    quit()
        else:
            self.screen.blit(load_button_inactive, (x, y))


class DrivingScene(Scene):
    def __init__(self, screen):
        super(DrivingScene, self).__init__(screen)
        self.bg = pygame.image.load("images/driving1.jpg")
        # self.script = script

    def enter(self):
        # while not self.status:
            self.screen.blit(self.bg, (0, 0))
            self.create_button("instruction", 50, 50, action[0])
            self.create_button("quit", 40, 50, action[1])


class Foyer(Scene):
    def __init__(self, screen):
        super(Foyer, self).__init__(screen)
        self.bg = pygame.image.load('./images/scene2_bg.jpg')

    def enter(self):
        self.screen.blit(self.bg, (0, 0))
        self.create_button('quit', 40, 50, action[1])
  
    # def next_scene(self, screen, input):

