import pygame, sys
from pygame.locals import *
import random


class HowToPlay(object):
    def __init__(self, screen, menu):
        self.menu = menu
        self.screen = screen

    def init(self):        
        while True:
            self.blitConteudo()

    def blitConteudo(self):
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

        self.message_display('Como jogar?', 75, (122,122,122), (250, 100))

        self.message_display('Para mexer o personagem, utilize as setas do seu teclado', 30, (122,122,122), (290, 160))
        self.message_display('Para atirar o frisbee, aperte espaço', 30, (122, 122, 122), (390, 160))
        self.message_display('O objetivo é coletar o máximo de frutas que puder e destruir o máximo de hotdogs possíveis', 30, (122, 122, 122), (450, 160))
        self.message_display('O jogo acaba quando 3 hotdogs atingirem o personagem', 30, (122, 122, 122), (500, 160))

        pygame.display.update()

    def message_display(self, text, font_size, font_color, posiBlit):
        largeText = pygame.font.SysFont('Roboto',font_size)
        TextSurf, TextRect = self.text_objects(text, largeText, font_color)
        self.screen.blit(TextSurf, posiBlit)

    def text_objects(self, text,font,font_color):
        textSurface = font.render(text, True, font_color)
        return textSurface, textSurface.get_rect()