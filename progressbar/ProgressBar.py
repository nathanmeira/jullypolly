import pygame, sys
from pygame.locals import *

class ProgressBar(object):
    def __init__(self, surfacePrincipal, widthBar, heightBar, progress, widthBox, blitPosion, titulo, colorBar):
        self.font = pygame.font.SysFont('Roboto', 25)
        self.widthBar = widthBar
        self.widthBox = widthBox
        self.heightBar = heightBar
        self.left = 10
        self.top = 5
        self.progress = progress
        self.titulo = titulo
        self.colorBar = colorBar
        self.colorTitle = (122, 122, 122)
        self.backgroundFundo = (255, 255, 255)
        self.blitPosion = blitPosion
        self.surfacePrincipal = surfacePrincipal
        self.adicionarBar()

    def adicionarBar(self):
        self.surface = pygame.surface.Surface((self.widthBox, self.heightBar + 10))     
        self.surface.fill(self.backgroundFundo)    
        rectProgress = pygame.Rect(0,self.top,self.widthBar*self.progress,self.heightBar)
        self.rect = pygame.draw.rect(self.surface, self.colorBar, rectProgress)
        self.surfacePrincipal.blit(self.surface, self.blitPosion)               

    def adicionarTitle(self):
        text = self.font.render(self.titulo, True, self.colorTitle) 
        text_rect = text.get_rect(center=(int(self.widthBar / 2), (self.heightBar + 7 )/2))
        self.surface.blit(text, text_rect)
        self.surfacePrincipal.blit(self.surface, self.blitPosion)    

