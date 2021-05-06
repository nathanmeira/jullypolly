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
while True:
    screen.fill((237,237,237))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()  
    
    message_display('Olá, Daniel!',400,200,25,(122,122,122), (20, 20))         
    drawRectBtnConfig()

    progress1 = ProgressBar(screen, 550, 35, jully.energiaGeral(), 550, (20,70), 'Energia Geral', (255, 201, 7))
    progress1.adicionarTitle()

    progress2 = ProgressBar(screen, 390, 35, jully.getExercicio(), 380, (380,150), 'Exercicio', (51, 51, 51))
    progress2.adicionarTitle()

    progress3 = ProgressBar(screen, 390, 35, jully.getAlimentacao(), 380, (380,210), 'Alimentação', (255, 118, 118))
    progress3.adicionarTitle()

    jully.setExercicios(-0.03)
    jully.setAlimentacao(-0.02)
    pygame.display.update()