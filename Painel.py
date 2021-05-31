import pygame, sys
from pygame.locals import *
import random
from progressbar.ProgressBar import ProgressBar
from personagem.JullyPollly import JullyPollly
from frisbol.FrisBol import FrisBol


class Painel(object):   
    def __init__(self, screen, width, height):
        self.screen = screen  
        self.width = width
        self.height = height
        self.jullyImg = pygame.image.load('personagem/imagens/jullyV2.png')
        self.fontDefault = pygame.font.SysFont('Roboto',30)
        self.som = False
        self.nomeJully = 'Jully'

    def initJully(self):
        self.jully = JullyPollly()
        self.jully.setNome(self.nomeJully)

    def init(self):        
        self.tocarMusica()
        jogarFrisbol = False
        while True:
            if(jogarFrisbol):
                jogarFrisbol = self.initFrisbol()
            else: 
                self.resumoStatus()

    def initFrisbol(self):
        jogo = FrisBol(self.width, self.height, self.screen, self.jully)
        return jogo.init()

    def resumoStatus(self):
        clock = pygame.time.Clock()
        clock.tick(60)
        self.screen.fill((237,237,237))        
        x_btn = 135
        y_btn = 400
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()         
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.isEventSobBtnJogarFrisbol(pygame.mouse.get_pos(), x_btn, y_btn):
                    self.initFrisbol()

        self.message_display('Olá, ' + str(self.jully.getNome()) + '!', 25, (122,122,122), (20, 20)) 
        self.message_display('Pontos: ' + str(self.jully.getScore()), 25, (122,122,122), (400, 20)) 
        self.drawRectBtnConfig()

        self.blitProgressStatusVida()

        self.diminuirProgressivamenteVidaPersonagem()

        self.blitQuantificacaoVidaPersonagem()           

        self.blitPersonagem()
       
        self.drawButton(x_btn, y_btn)
        
        if(self.jully.tempoVidaRestanteSegundos() <= 0):
            self.menu.mainloop(self.screen)
            exit
        
        pygame.display.update()

    def message_display(self, text, font_size, font_color, posiBlit):
        largeText = pygame.font.SysFont('Roboto',font_size)
        TextSurf, TextRect = self.text_objects(text, largeText, font_color)
        self.screen.blit(TextSurf, posiBlit)
                    
    def drawRectBtnConfig(self):
        button = pygame.Rect(self.screen.get_rect().right - 80, 10, 40, 40)
        pygame.draw.rect(self.screen, [255, 0, 0], button)

    def text_objects(self, text,font,font_color):
        textSurface = font.render(text, True, font_color)
        return textSurface, textSurface.get_rect()

    def createProgressBar(self, screen, widthBar, heightBar, progress, widthBox, blitPosion, titulo, colorBar):
        progress1 = ProgressBar(screen, widthBar, heightBar, progress, widthBox, blitPosion, titulo, colorBar)
        progress1.adicionarTitle()

    def blitProgressStatusVida(self):
        self.createProgressBar(self.screen, 550, 35, self.jully.energiaGeralPorcentagem(), 550, (20,70), 'Energia Geral', (255, 201, 7))
        self.createProgressBar(self.screen, 390, 35, self.jully.getExercicio(), 380, (380,150), 'Exercicio', (51, 51, 51))
        self.createProgressBar(self.screen, 390, 35, self.jully.getAlimentacao(), 380, (380,210), 'Alimentação', (255, 118, 118))

    def diminuirProgressivamenteVidaPersonagem(self):
        self.jully.setExercicios(self.jully.variacaoExercicio * -1)
        self.jully.setAlimentacao(self.jully.variacaoAlimentacao * -1)

    def blitPersonagem(self):
        self.screen.blit(self.jullyImg, (150, 260))

    def blitQuantificacaoVidaPersonagem(self):
        self.screen.blit(self.fontDefault.render(str('Vida Restante:'), True, (0, 0, 0)), (500, 280))
        self.screen.blit(self.fontDefault.render(str(self.jully.tempoVidaRestanteSegundos()), True, (0, 0, 0)), (560, 310))

    def ativarSom(self):
        self.som = True

    def desativarSom(self):
        self.som = False

    def tocarMusica(self):
        if(self.som):
            pygame.mixer.init()
            pygame.mixer.music.load('som/catch.mp3')
            pygame.mixer.music.play(-1)

    def drawButton(self, x_btn, y_btn):
        color_light = (170,170,170)
        color_dark = (100,100,100)
        if self.isEventSobBtnJogarFrisbol(pygame.mouse.get_pos(), x_btn, y_btn):
            pygame.draw.rect(self.screen,color_light,[x_btn,y_btn,140,40])          
        else:
            pygame.draw.rect(self.screen,color_dark,[x_btn,y_btn,140,40])
        text = self.fontDefault.render('Jogar', True, (255,255,255)) 
        text_rect = text.get_rect(center=(int(x_btn) + 70, y_btn + 20))
        self.screen.blit(text, text_rect) 

    def isEventSobBtnJogarFrisbol(self, mouse, x_btn, y_btn):
        return x_btn <= mouse[0] <= x_btn+140 and y_btn <= mouse[1] <= y_btn+40

    def setMenu(self, menu):
        self.menu = menu

    def getJully(self):
        return self.jully
    
    def setNomePersonagem(self, nome):
        self.nomeJully = nome