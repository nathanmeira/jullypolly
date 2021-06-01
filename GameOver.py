from game import WIDTH
import pygame, sys
from pygame.locals import *
import random

class GameOver(object):   
    def __init__(self, screen, jully, menu):
        self.menu = menu
        self.screen = screen
        self.jully = jully
        
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
        
        self.message_display('Game Over!', 75, (122,122,122), (100)) 

        self.message_display(str(self.jully.getNome()) + ', você fez: ', 40, (122,122,122), (160)) 

        self.message_display('Morango(s) coletados: ' + str(self.jully.qtdMorango), 40, (122,122,122), (290)) 
        self.message_display('Cenoura(s) coletados: ' + str(self.jully.qtdCenoura), 40, (122,122,122), (230)) 
        self.message_display('Uva(s) coletados: ' + str(self.jully.qtdUva), 40, (122,122,122), (350)) 
        #self.message_display('HotDogs destruídos: ' + str(self.jully.qtdHotDog), 40, (122,122,122), (410)) 

        self.message_display('Pontos: ' + str(self.jully.score), 60, (122,122,122), (440)) 
                    
        pygame.display.update()

    def message_display(self, text, font_size, font_color, Y_posiBlit):
        largeText = pygame.font.SysFont('Roboto',font_size)
        TextSurf, TextRect = self.text_objects(text, largeText, font_color)
        X_posiBlit = WIDTH/2 - TextSurf.get_width()/2
        self.screen.blit(TextSurf, (X_posiBlit, Y_posiBlit))

    def text_objects(self, text,font,font_color):
        textSurface = font.render(text, True, font_color)
        return textSurface, textSurface.get_rect()