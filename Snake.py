import pygame
import sys
import tkinter
import pytest

class Test_menu ():
    def _init_ (self, Snake2):
        self.self = Snake2
        self.mid_w, self.mid_h = self.game.pygame.display_h/2, self.pygame.display_w/2
        self.run_display = True
        self.cursor_rect = pygame.Rect (0,0,20,20)
        self.offset = -100


        def draw_cursor(self):
            self.game.draw_text ('*',15,self.cursor_rect.x, self.cursor_rect.y)


        def blit_screen(self):
            self.game.window.blit(self.game.display,(0,0))
            pygame.display.update()
            self.game.reset_keys()


class primary_menu(Test_menu):
    def _init_ (self, Snake2):
        menu._init_ (self,Snake2)
        self.state = "start"
        self.startx, self.starty = 
