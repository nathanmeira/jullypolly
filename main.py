import sys, pygame
import pygame
import pygame_menu
import pygame_menu.themes
from pygame.locals import *
from random import *
from pygame_menu.themes import Theme
from Painel import Painel

THEME_BLUE = Theme(
    background_color=(182, 64, 149),
    focus_background_color=(182, 64, 149),
    scrollbar_shadow=True,
    widget_border_width=0,
    scrollbar_slider_color=(150, 200, 230),
    scrollbar_slider_hover_color=(00, 00, 00),
    scrollbar_slider_pad=2,
    selection_color=(00, 00, 00),
    title_background_color=(182, 64, 149),
    title_font_color=(00, 00, 00),
    title_font_shadow=False,
    widget_font_color=(00, 00, 00)
)

pygame.init()
display_width = 800
display_height = 600
screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("JullyPolly")
painel = Painel(screen, display_width, display_height)

def painelJogo():    
    painel.jully.resetStatusPersonagem()   
    painel.init()

def set_difficulty(value, isAtivarSom):
    if(isAtivarSom == 1):
        painel.ativarSom()  
    else:
        painel.desativarSom()       
        
def set_nome(nome):
    painel.jully.setNome(nome)


menu = pygame_menu.Menu('', display_width, display_height, theme=THEME_BLUE)

menu.add.text_input('Nome: ', default='', onchange=set_nome)
menu.add.selector('Som: ', [('Não', 0), ('Sim', 1)], onchange=set_difficulty)
menu.add.button('Jogar', painelJogo)
menu.add.button('Sair', pygame_menu.events.EXIT)

painel.setMenu(menu)
menu.mainloop(screen)












