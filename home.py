import sys, pygame
from pygame.locals import *
from random import *

pygame.init()

display_width = 800
display_height = 600
screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Home Screen")
clock = pygame.time.Clock()

def text_objects(text,font,font_color):
    textSurface = font.render(text, True,font_color)
    return textSurface, textSurface.get_rect()

def message_display(text,width,height,font_size,font_color):
    largeText = pygame.font.Font('freesansbold.ttf',font_size)
    TextSurf, TextRect = text_objects(text, largeText, font_color)
    TextRect.center = (width,height)
    screen.blit(TextSurf, TextRect)

    pygame.display.update()

def display():
    message_display('Seja bem vindo ao JullyPolly',400,200,40,(96,96,96))
    message_display('Por favor, insira o nome do seu personagem abaixo:',400,250,30,(220,220,220))

pygame.event.set_blocked(pygame.MOUSEMOTION)
while True:
    for event in pygame.event.get():
        screen.fill((170,170,170))
        pygame.display.update()
        display()
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

