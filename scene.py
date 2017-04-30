import pygame

clock = pygame.time.Clock()


button_list = {'start': ['./images/start_button_hover.png', './images/start_button.png'],
        'quit': ['./images/quit_button_hover.png', './images/quit_button.png'],
        'instruction': ['./images/Instructions_button_hover.png', './images/Instructions_button.png'],
        'woman': ['./images/beautiful_woman_hover.png', './images/beautiful_woman.png'],
        'man': ['./images/elderly_man_hover.png', './images/elderly_man.png'],
        'teen': ['./images/goth_teen_hover.png', './images/goth_teen.png'],
        'note1': ['./images/note1.png', './images/note1.png'],
        'note2': ['./images/note2.png', './images/note2.png'],
        'watch': ['./images/watch.png', './images/watch.png'],
        'skyline': ['./images/skyline1.png', './images/skyline1.png'],
        'locket': ['./images/locket1.png', './images/locket1.png'],
        'phone': ['./images/phone1.png', './images/phone1.png']
        }
action = ['next', 'quit', 'instruction', 'library', 'bedroom', 'kitchen', 'final']
moving_scene = {
    'library': False,
    'bedroom': False,
    'kitchen': False,
    'final': False,
}



class Scene(object):
    def __init__(self, screen, scene_on=False):
        self.screen = screen
        self.bg = pygame.image.load("images/house.jpg")
        self.scene_on = scene_on

    def enter(self):
        # while not self.status:
        self.screen.blit(self.bg, (0, 0))
        self.create_button("start", 528, 520, action[0])
        self.create_button("quit", 528, 600, action[1])
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
                elif action == "quit":
                    pygame.quit()
                    quit()
                if action == "library":
                    print 1
                    moving_scene['library'] = True
                elif action == "bedroom":
                    moving_scene['bedroom'] = True
                elif action == "kitchen":
                    moving_scene['kitchen'] = True
                elif action == "final":
                    moving_scene['final'] = True

        else:
            self.screen.blit(load_button_inactive, (x, y))

    def compare_list(player_list, master_list):
        if player_list == master_list:
            return True
        else:
            return False

class DrivingScene(Scene):
    def __init__(self, screen, text_box):
        super(DrivingScene, self).__init__(screen)
        self.bg = pygame.image.load("images/driving1.jpg")
        self.text_box = text_box
        # self.script = script

    def enter(self):
        # while not self.status:
            self.screen.blit(self.bg, (0, 0))
            self.screen.blit(self.text_box, (240, 580))
            self.create_button("instruction", 50, 50, action[2])
            self.create_button("quit", 1000, 40, action[1])

    def next_scene(self, check_user_input):
        if check_user_input:
            self.scene_on = True
        else:
            print("Wrong!")





class Foyer(Scene):
    def __init__(self, screen, text_box):
        super(Foyer, self).__init__(screen)
        self.bg = pygame.image.load('./images/scene2_bg.jpg')
        self.text_box = text_box

    def enter(self):
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.text_box, (240, 580))
        # self.create_button('instruction', 40, 50, action[2])
        self.create_button('woman', 300, 390, action[3])
        self.create_button('man', 150, 425, action[4])
        self.create_button('teen', 700, 385, action[5])

class Library(Scene):
    def __init__(self, screen, text_box):
        super(Library, self).__init__(screen)
        self.bg = pygame.image.load('./images/library_bg.jpg')
        self.text_box = text_box

    def enter(self):
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.text_box, (240, 580))
        # self.create_button('instruction', 40, 50, action[2])
        woman_img = pygame.image.load('./images/beautiful_woman.png')
        self.screen.blit(woman_img, (60, 350))
        self.create_button('note1', 275, 550, action[1])
        self.create_button('note2', 695, 500, action[1])
        # self.create_button()

class Bedroom(Scene):
    def __init__(self, screen, text_box):
        super(Bedroom, self).__init__(screen)
        self.bg = pygame.image.load('./images/bedroom.jpg')
        self.text_box = text_box

    def enter(self):
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.text_box, (240, 580))
        # self.create_button('instruction', 40, 50, action[2])
        self.create_button('watch', 425, 560, action [1])
        self.create_button('skyline', 643, 300, action[1])
        man_img = pygame.image.load('./images/elderly_man.png')
        self.screen.blit(man_img, (45, 335))

class Kitchen(Scene):
    def __init__(self, screen, text_box):
        super(Kitchen, self).__init__(screen)
        self.bg = pygame.image.load('./images/kitchen.jpg')
        self.text_box = text_box

    def enter(self):
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.text_box, (240, 580))
        # self.create_button('instruction', 40, 50, action[2])
        self.create_button('phone', 100, 435, action[1])
        self.create_button('locket', 950, 430, action[1])
        teen_img = pygame.image.load('./images/goth_teen3.png')
        self.screen.blit(teen_img, (600, 220))

class Final(Scene):
    def __init__(self, screen, text_box):
        super(Final, self).__init__(screen)
        self.bg = pygame.image.load('./images/final.jpg')
        self.text_box = text_box

    def enter(self):
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.text_box, (340, 100))
