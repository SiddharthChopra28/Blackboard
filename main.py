import pygame
from pygame.constants import RESIZABLE
import math

GREY = (44, 41, 40)
YELLOW = (223, 168, 33)


class Blackboard():
    def __init__(self):
        pygame.init()
        pygame.font.init()
        
        self.width = 500
        self.height = 500
        
        self.exit = False
        self.erase_on = False
        self.mouse_down = False

        self.clock = pygame.time.Clock()
        self.fps = math.inf

        self.bgcolor = GREY
        self.fgcolor = YELLOW

        self.size = 3
        self.drawing = set([])

        self.logo = pygame.image.load('logo.png')

        self.ctrl_pressed = True
        self.letter_key = None

        Blackboard.gameWindow = pygame.display.set_mode((self.width, self.height), RESIZABLE)
        Blackboard.windowName = pygame.display.set_caption("Blackboard")
        Blackboard.icon = pygame.display.set_icon(self.logo)

    def draw(self, color, pos, size=3):
        pygame.draw.circle(self.gameWindow, color, pos, size)
        self.drawing.add(pos)



    def run(self):
        self.gameWindow.fill(self.bgcolor)
        
        while not self.exit:
            self.letter_key = None
            self.mouse = pygame.mouse.get_pos()
            self.pressedkey = pygame.key.get_pressed()

            if self.mouse_down:
                self.draw(self.fgcolor, self.mouse, self.size)

            for event in pygame.event.get():
                
                if event.type  == pygame.QUIT:
                    self.exit = True
                if event.type == pygame.VIDEORESIZE:
                    self.gameWindow.fill(self.bgcolor)
                    for i in self.drawing:
                        self.draw(self.fgcolor, i, self.size)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_down = True
                if event.type == pygame.MOUSEBUTTONUP:
                    self.mouse_down = False
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LCTRL:
                        self.ctrl_pressed = True
                    self.letter_key = event.key
                    

            if self.ctrl_pressed and self.letter_key == pygame.K_c:
                self.gameWindow.fill(self.bgcolor)
                self.drawing = set([])

            if self.ctrl_pressed and self.letter_key == pygame.K_e:
                if not self.erase_on:
                    self.erase_on = True
                    self.fgcolor = GREY
                else:
                    self.erase_on = False
                    self.fgcolor = YELLOW

            if self.ctrl_pressed and self.letter_key == pygame.K_EQUALS:
                self.size +=1
                print(self.size)

            if self.ctrl_pressed and self.letter_key == pygame.K_MINUS:
                self.size -=1
                print(self.size)

            pygame.display.update()

            self.clock.tick(self.fps)

if __name__ == '__main__':
    Blackboard().run()