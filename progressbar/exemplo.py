import pygame, sys
import time
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)

left = 10
top = 10
maxwidth = 390
progress = 1
height = 35

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
        progress = self.progress
        if(progress >= 0.96):
            progress = 0.96
        rectProgress = pygame.Rect(self.left,self.top,self.widthBar*progress,self.heightBar)
        self.rect = pygame.draw.rect(self.surface, self.colorBar, rectProgress)
        self.surfacePrincipal.blit(self.surface, self.blitPosion)        

    def adicionarTitle(self):
        text = self.font.render(self.titulo, True, self.colorTitle) 
        text_rect = text.get_rect(center=(int(self.widthBar / 2), (self.heightBar + 7 )/2))
        self.surface.blit(text, text_rect)
        self.surfacePrincipal.blit(self.surface, self.blitPosion)    


while True:
    DISPLAYSURF.fill((196, 196, 196))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()       
    progress1 = ProgressBar(DISPLAYSURF, 390, 35, 0.98, 380, (10,15), 'Saúde', (255, 201, 7))
    progress1.adicionarTitle()

    progress2 = ProgressBar(DISPLAYSURF, 390, 35, 0.35, 380, (10,70), 'Alimentação', (255, 118, 118))
    progress2.adicionarTitle()

    progress2 = ProgressBar(DISPLAYSURF, 390, 35, 0.3, 380, (10,125), 'Teste', (51, 51, 51))
    progress2.adicionarTitle()
    
    pygame.display.update()
    
