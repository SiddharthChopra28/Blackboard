import pygame
from pygame.constants import RESIZABLE

GREY = (44, 41, 40)
YELLOW = (223, 168, 33)

class Blackboard():
    def __init__(self):
        pygame.init()
        pygame.font.init()
        
        self.width = 500
        self.height = 500
        
        self.exit = False

        self.mouse_down = False

        self.bgcolor = GREY
        self.fgcolor = YELLOW

        self.drawing = set([])

        Blackboard.gameWindow = pygame.display.set_mode((self.width, self.height), RESIZABLE)
        Blackboard.windowName = pygame.display.set_caption("Blackboard")

    def draw(self, color, pos):
        pygame.draw.circle(self.gameWindow, color, pos, 3)
        self.drawing.add(pos)

    def fill_gaps(self, color):
        pygame.draw.lines(self.gameWindow, color, True, list(self.drawing))


    def run(self):
        self.gameWindow.fill(self.bgcolor)
        
        while not self.exit:
            self.mouse = pygame.mouse.get_pos()
            self.pressedkey = pygame.key.get_pressed()

            if self.mouse_down:
                print(self.mouse)
                self.draw(self.fgcolor, self.mouse)

            for event in pygame.event.get():
                if event.type  == pygame.QUIT:
                    self.exit = True
                if event.type == pygame.VIDEORESIZE:
                    self.gameWindow.fill(self.bgcolor)
                    for i in self.drawing:
                        self.draw(self.fgcolor, i)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_down = True
                if event.type == pygame.MOUSEBUTTONUP:
                    self.mouse_down = False


            if self.pressedkey[pygame.K_LCTRL] and self.pressedkey[pygame.K_c]:
                self.gameWindow.fill(self.bgcolor)
                self.drawing = set([])


            
            
            pygame.display.update()



if __name__ == '__main__':
    Blackboard().run()