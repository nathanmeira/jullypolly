import sys, pygame
from pygame.locals import *
from random import *

pygame.init()
display_width = 800
display_height = 600
screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Home Screen")
clock = pygame.time.Clock()
pygame.event.set_blocked(pygame.MOUSEMOTION)

def font(size):
    font = pygame.font.Font('freesansbold.ttf', size)
    return font

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = pygame.Color(96,96,96)
        self.text = text
        self.txt_surface = font(33).render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = font(33).render(self.text, True, self.color)

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)
        pygame.display.flip()

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

def button(msg,x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #if x+w > mouse[0] > x and y+h > mouse[1] > y:
    smallText = font(20)
    textSurf, textRect = text_objects(msg, smallText, (255,255,255))
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    pygame.draw.rect(screen, (51,51,255), (x,y,w,h))
    screen.blit(textSurf, textRect)
    pygame.display.update() 
    
input_box = InputBox(205, 300, 400, 40)
while True:
    for event in pygame.event.get():
        screen.fill((170,170,170))
        display()
        input_box.handle_event(event)
        input_box.draw(screen)
        button('Iniciar',320,400,150,65)

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
 
