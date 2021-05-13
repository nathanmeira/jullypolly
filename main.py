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

def painelJogo():
    painel = Painel(screen)
    painel.init()


def set_difficulty(value, difficulty):
    print(difficulty)
    pass


menu = pygame_menu.Menu('', display_width, display_height, theme=THEME_BLUE)

menu.add.text_input('Nome :', default='')
menu.add.selector('Som :', [('Sim', 1), ('Não', 0)], onchange=set_difficulty)
menu.add.button('Jogar', painelJogo)
menu.add.button('Sair', pygame_menu.events.EXIT)

menu.mainloop(screen)












