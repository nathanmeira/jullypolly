import pygame, sys
from pygame.locals import *
import random


class Ranking(object):   
    def __init__(self, screen, listPersonagens, menu):
        self.listPersosagens = listPersonagens
        self.menu = menu
        self.screen = screen

    def init(self):        
        while True:
            self.blitList()

    def blitList(self):
        clock = pygame.time.Clock()
        clock.tick(60)
        self.screen.fill((237,237,237))    
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()         
            if event.type == KEYDOWN:
                if event.key==K_ESCAPE:
                    self.menu.mainloop(self.screen)
                    exit

        order = 1
        for p in self.listPersosagens:
            self.message_display(p.getNome(), 25, (122,122,122), (20, 20 + (20 * order))) 
            order += 1
        pygame.display.update()

    def message_display(self, text, font_size, font_color, posiBlit):
        largeText = pygame.font.SysFont('Roboto',font_size)
        TextSurf, TextRect = self.text_objects(text, largeText, font_color)
        self.screen.blit(TextSurf, posiBlit)

    def text_objects(self, text,font,font_color):
        textSurface = font.render(text, True, font_color)
        return textSurface, textSurface.get_rect()