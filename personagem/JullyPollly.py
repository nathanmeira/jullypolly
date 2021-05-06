import pygame, sys
from pygame.locals import *

class JullyPollly(object):   

    def __init__(self):  
        self.exercicios = 100
        self.alimentacao = 100

        self.pesoExercicio = 0.4
        self.pesoAlimentacao = 0.6

        self.variacaoExercicio = 0.03
        self.variacaoAlimentacao = 0.02
    
    def energiaGeralPorcentagem(self):
        return self.energiaGeral() / 100

    def energiaGeral(self):
        return ((self.exercicios * self.pesoExercicio) + (self.alimentacao * self.pesoAlimentacao))
        
    def setExercicios(self, variacao):
        self.exercicios += variacao
        if(self.exercicios <= 0):
            self.exercicios = 0

    def setAlimentacao(self, variacao):
        self.alimentacao += variacao
        if(self.alimentacao <= 0):
            self.alimentacao = 0

    def getExercicio(self):
        return self.exercicios / 100

    def getAlimentacao(self):
        return self.alimentacao / 100

    def tempoVidaRestanteSegundos(self):
        return int(self.energiaGeral()) 