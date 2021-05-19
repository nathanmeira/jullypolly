import pygame, sys
from pygame.locals import *
from progressbar.ProgressBar import ProgressBar
from personagem.JullyPollly import JullyPollly


class Painel(object):   
    def __init__(self, screen):
        self.screen = screen  
        self.jully = JullyPollly()
        self.fontDefault = pygame.font.SysFont('Roboto',30)
        self.jullyImg = pygame.image.load('personagem/imagens/jully.png')
        self.som = False
        
    def init(self):
        clock = pygame.time.Clock()
        self.tocarMusica()
        while True:
            clock.tick(60)
            self.screen.fill((237,237,237))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()  

            

            self.message_display('Olá, ' + str(self.jully.getNome()) + '!', 25, (122,122,122), (20, 20)) 
            self.drawRectBtnConfig()

            self.blitProgressStatusVida()

            self.diminuirProgressivamenteVidaPersonagem()

            self.blitQuantificacaoVidaPersonagem()           

            self.blitPersonagem()
            
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


