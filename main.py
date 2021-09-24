import pygame
from pygame.constants import MOUSEMOTION, RESIZABLE
import math

GREY = (44, 41, 40)
YELLOW = (223, 168, 33)
DARK_GREY = (141,140,141)
BLACK = (0, 0, 0)
LIGHT_GREY = (230,239,201)


class Blackboard():
    def __init__(self):
        pygame.init()
        
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

        self.prev_pos = None
        self.is_down_count = 0

        self.right_click_undo_box = None
        self.right_click_change_pen_color_box = None
        self.right_click_change_bg_color_box = None
        self.right_click_clear_box = None
        self.right_click_help_box = None

        self.right_click_undo_box_border = None
        self.right_click_change_pen_color_box_border = None
        self.right_click_change_bg_color_box_border = None
        self.right_click_clear_box_border = None
        self.right_click_help_box_border = None

        self.right_click_undo_text = None
        self.right_click_change_pen_color_text = None
        self.right_click_change_bg_color_text = None
        self.right_click_clear_text = None
        self.right_click_help_text = None

        self.arial = pygame.font.SysFont('Arial', 15)


        Blackboard.gameWindow = pygame.display.set_mode((self.width, self.height), RESIZABLE)
        Blackboard.windowName = pygame.display.set_caption("Blackboard")
        Blackboard.icon = pygame.display.set_icon(self.logo)


    def complete_line(self, srf, color, start, end, radius=1):
        if end is None:
            end = start
        dx = end[0]-start[0]
        dy = end[1]-start[1]
        distance = max(abs(dx), abs(dy))
        for i in range(distance):
            x = int( start[0]+float(i)/distance*dx)
            y = int( start[1]+float(i)/distance*dy)
            pygame.draw.circle(srf, color, (x, y), radius)
            self.drawing.add((x, y, color, radius))

    def draw(self, color, pos, completeLine, size=3):
        pygame.draw.circle(self.gameWindow, color, (pos[0], pos[1]), size)
        self.drawing.add((pos[0], pos[1], color, size))
        if completeLine:
            self.complete_line(self.gameWindow, color, (pos[0], pos[1]), self.prev_pos,  size)
        self.prev_pos = (pos[0], pos[1])


        

    def redraw_text(self):
        self.gameWindow.fill(self.bgcolor)
        for i in self.drawing:
            self.draw(i[2], i[:2], False, i[3])


        self.right_click_undo_box = None
        self.right_click_change_pen_color_box = None
        self.right_click_change_bg_color_box = None
        self.right_click_clear_box = None
        self.right_click_help_box = None

        self.right_click_undo_box_border = None
        self.right_click_change_pen_color_box_border = None
        self.right_click_change_bg_color_box_border = None
        self.right_click_clear_box_border = None
        self.right_click_help_box_border = None

        self.right_click_undo_text = None
        self.right_click_change_pen_color_text = None
        self.right_click_change_bg_color_text = None
        self.right_click_clear_text = None
        self.right_click_help_text = None


    def erase(self, pos, size, completeLine):
        drawing = list(self.drawing)
        for index, i in enumerate(drawing):

            if abs(i[0] - pos[0]) < size  and abs(i[1] - pos[1]) < size:
                i = list(i)
                i[2] = self.bgcolor
                i = tuple(i)
                drawing[index] = i
                
            else:
                self.drawing.add((pos[0], pos[1], self.bgcolor, size))

        
        self.drawing = set(drawing)
        self.redraw_text()


    def right_click(self, pos):
        self.redraw_text()
        # undo
        # change pen color
        # change bg color
        # clear
        # help

        box_width = 130
        box_len = 26
        border_width = 1
        text_margin_left = 5

        self.right_click_undo_box = pygame.Rect(pos[0], pos[1], box_width, box_len)
        self.right_click_change_pen_color_box = pygame.Rect(pos[0], pos[1]+ box_len, box_width, box_len)
        self.right_click_change_bg_color_box = pygame.Rect(pos[0], pos[1]+ 2*box_len, box_width, box_len)
        self.right_click_clear_box = pygame.Rect(pos[0], pos[1]+ 3*box_len, box_width, box_len)
        self.right_click_help_box = pygame.Rect(pos[0], pos[1]+ 4*box_len, box_width, box_len)

        self.right_click_undo_box_border = pygame.Rect(pos[0], pos[1], box_width, box_len)
        self.right_click_change_pen_color_box_border = pygame.Rect(pos[0], pos[1]+ box_len, box_width, box_len)
        self.right_click_change_bg_color_box_border = pygame.Rect(pos[0], pos[1]+ 2*box_len, box_width, box_len)
        self.right_click_clear_box_border = pygame.Rect(pos[0], pos[1]+ 3*box_len, box_width, box_len)
        self.right_click_help_box_border = pygame.Rect(pos[0], pos[1]+ 4*box_len, box_width, box_len)

        self.right_click_undo_text = self.arial.render('Undo', True, BLACK)
        self.right_click_change_pen_color_text = self.arial.render('Change pen color', True, BLACK)
        self.right_click_change_bg_color_text = self.arial.render('Change board color', True, BLACK)
        self.right_click_clear_text = self.arial.render('Clear Board', True, BLACK)
        self.right_click_help_text = self.arial.render('More Settings', True, BLACK)

        rect_center1 = self.right_click_undo_text.get_rect(midleft=(self.right_click_undo_box.midleft[0]+text_margin_left, self.right_click_undo_box.midleft[1]))
        rect_center2 = self.right_click_change_pen_color_text.get_rect(midleft=(self.right_click_change_pen_color_box.midleft[0]+text_margin_left, self.right_click_change_pen_color_box.midleft[1]))
        rect_center3 = self.right_click_change_bg_color_text.get_rect(midleft=(self.right_click_change_bg_color_box.midleft[0]+text_margin_left, self.right_click_change_bg_color_box.midleft[1]))
        rect_center4 = self.right_click_clear_text.get_rect(midleft=(self.right_click_clear_box.midleft[0]+text_margin_left, self.right_click_clear_box.midleft[1]))
        rect_center5 = self.right_click_help_text.get_rect(midleft=(self.right_click_help_box.midleft[0]+text_margin_left, self.right_click_help_box.midleft[1]))

        pygame.draw.rect(self.gameWindow, LIGHT_GREY, self.right_click_undo_box)
        pygame.draw.rect(self.gameWindow, LIGHT_GREY, self.right_click_change_pen_color_box)
        pygame.draw.rect(self.gameWindow, LIGHT_GREY, self.right_click_change_bg_color_box)
        pygame.draw.rect(self.gameWindow, LIGHT_GREY, self.right_click_clear_box)
        pygame.draw.rect(self.gameWindow, LIGHT_GREY, self.right_click_help_box)

        pygame.draw.rect(self.gameWindow, DARK_GREY, self.right_click_undo_box_border, border_width)
        pygame.draw.rect(self.gameWindow, DARK_GREY, self.right_click_change_pen_color_box_border, border_width)
        pygame.draw.rect(self.gameWindow, DARK_GREY, self.right_click_change_bg_color_box_border, border_width)
        pygame.draw.rect(self.gameWindow, DARK_GREY, self.right_click_clear_box_border, border_width)
        pygame.draw.rect(self.gameWindow, DARK_GREY, self.right_click_help_box_border, border_width)

        self.gameWindow.blit(self.right_click_undo_text, rect_center1)
        self.gameWindow.blit(self.right_click_change_pen_color_text, rect_center2)
        self.gameWindow.blit(self.right_click_change_bg_color_text, rect_center3)
        self.gameWindow.blit(self.right_click_clear_text, rect_center4)
        self.gameWindow.blit(self.right_click_help_text, rect_center5)

    def run(self):
        self.gameWindow.fill(self.bgcolor)
        
        while not self.exit:
            self.letter_key = None
            self.mouse = pygame.mouse.get_pos()
            self.pressedkey = pygame.key.get_pressed()
            
            if self.mouse_down:
                if not self.erase_on:
                    if self.is_down_count > 0:
                        self.draw(self.fgcolor, self.mouse, True, self.size)
                    else:
                        self.draw(self.fgcolor, self.mouse, False, self.size)
                else:
                    if self.is_down_count > 0:
                        self.erase(self.mouse, self.size, True)
                    else:
                        self.erase(self.mouse, self.size, False)
            else:
                self.is_down_count = 0


            for event in pygame.event.get():


                if event.type  == pygame.QUIT:
                    self.exit = True

                if event.type == pygame.VIDEORESIZE:
                    self.redraw_text()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if event.button != 3:
                        if self.right_click_undo_box or self.right_click_change_pen_color_box or self.right_click_change_bg_color_box or self.right_click_clear_box or self.right_click_help_box:
                            if not self.right_click_undo_box_border.collidepoint(self.mouse) and not self.right_click_change_pen_color_box_border.collidepoint(self.mouse) and not self.right_click_change_bg_color_box_border.collidepoint(self.mouse) and not self.right_click_clear_box_border.collidepoint(self.mouse) and not self.right_click_help_box_border.collidepoint(self.mouse):
                                self.redraw_text()
                                self.right_click_box = None
                                self.mouse_down = True

                            elif self.right_click_undo_box_border.collidepoint(self.mouse):
                                self.undo()
                            elif self.right_click_change_pen_color_box_border.collidepoint(self.mouse):
                                self.change_pen_color()
                            elif self.right_click_change_bg_color_box_border.collidepoint(self.mouse):
                                self.change_bg_color()
                            elif self.right_click_clear_box_border.collidepoint(self.mouse):
                                self.gameWindow.fill(self.bgcolor)
                                self.drawing = set([])
                            elif self.right_click_help_box_border.collidepoint(self.mouse):
                                self.show_help_page()

                        else:
                            self.mouse_down = True

                if event.type == MOUSEMOTION:
                    if self.mouse_down:
                        self.is_down_count+=1
                        print(self.is_down_count)


                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button != 3:
                        self.mouse_down = False
                    else:
                        self.right_click(self.mouse)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LCTRL:
                        self.ctrl_pressed = True
                    self.letter_key = event.key
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.redraw_text()
                        
                    

            if self.ctrl_pressed and self.letter_key == pygame.K_c:
                self.gameWindow.fill(self.bgcolor)
                self.drawing = set([])

            if self.ctrl_pressed and self.letter_key == pygame.K_e:
                if not self.erase_on:
                    self.erase_on = True
                else:
                    self.erase_on = False

            if self.ctrl_pressed and self.letter_key == pygame.K_EQUALS:
                self.size +=1

            if self.ctrl_pressed and self.letter_key == pygame.K_MINUS:
                self.size -=1

            pygame.display.update()

            self.clock.tick(self.fps)

if __name__ == '__main__':
    Blackboard().run()