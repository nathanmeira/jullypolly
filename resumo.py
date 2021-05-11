import sys, pygame
from pygame.locals import *
from random import *
from progressbar.ProgressBar import ProgressBar
from personagem.JullyPollly import JullyPollly

pygame.init()


display_width = 800
display_height = 600
screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("JullyPolly")
clock = pygame.time.Clock()

jullyImg = pygame.image.load('personagem/imagens/jully.png')


# pygame.event.set_blocked(pygame.MOUSEMOTION)

def text_objects(text,font,font_color):
    textSurface = font.render(text, True,font_color)
    return textSurface, textSurface.get_rect()

def message_display(text,width,height,font_size,font_color, posiBlit):
    largeText = pygame.font.SysFont('Roboto',font_size)
    TextSurf, TextRect = text_objects(text, largeText, font_color)
    screen.blit(TextSurf, posiBlit)

def drawRectBtnConfig():
    button = pygame.Rect(screen.get_rect().right - 80, 10, 40, 40)
    pygame.draw.rect(screen, [255, 0, 0], button)


jully = JullyPollly()
font = pygame.font.SysFont('Roboto',30)
timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, 1000)
while True:
    clock.tick(60)
    screen.fill((237,237,237))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()  
    
    message_display('Olá, Daniel!',400,200,25,(122,122,122), (20, 20))         
    drawRectBtnConfig()

    progress1 = ProgressBar(screen, 550, 35, jully.energiaGeralPorcentagem(), 550, (20,70), 'Energia Geral', (255, 201, 7))
    progress1.adicionarTitle()

    progress2 = ProgressBar(screen, 390, 35, jully.getExercicio(), 380, (380,150), 'Exercicio', (51, 51, 51))
    progress2.adicionarTitle()

    progress3 = ProgressBar(screen, 390, 35, jully.getAlimentacao(), 380, (380,210), 'Alimentação', (255, 118, 118))
    progress3.adicionarTitle()

    jully.setExercicios(jully.variacaoExercicio * -1)
    jully.setAlimentacao(jully.variacaoAlimentacao * -1)

    screen.blit(font.render(str('Vida Restante:'), True, (0, 0, 0)), (500, 280))
    screen.blit(font.render(str(jully.tempoVidaRestanteSegundos()), True, (0, 0, 0)), (560, 310))

    screen.blit(jullyImg, (150, 260))
    pygame.display.update()
    # clock.tick(60)
