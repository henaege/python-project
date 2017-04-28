import pygame

buttons = {'start_inactive': './images/start_button.png',
        'start_active':'./images/start_button_hover.png', 
        'quit_inactive':'./images/quit_button.png', 
        'quit_active':'./images/quit_button_hover.png'}

class Scene(object):
    def __init__(self, screen, name, bg, inactive_button, hover_button, quit_button, status=False):
        self.screen = screen
        self.name = name
        # self.script = script
        self.bg = bg
        self.inactive_button = inactive_button
        self.hover_button = hover_button
        self.status = status

    def enter(self):
        while not self.status:        
            self.screen.blit(self.bg, (0,0))
            self.button(self.screen, 50, 50, "next")
            # self.screen.blit(text_box, (240, 600))

    def button(self, scene, x, y, action=None):
        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # print(click)
        if self.inactive_button.get_rect(left=x, top=y).collidepoint(pygame.mouse.get_pos()):
            self.screen.blit(self.hover_button, (x, y))
            if click[0] == 1 and action != None:
                if action == "next":
                   scene.enter()
                   click[0] = False
                if action == "quit":
                    pygame.quit()
                    quit()
        else:
            self.screen.blit(self.inactive_button, (x, y))