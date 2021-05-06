import pygame, sys
from pygame.locals import *

class JullyPollly(object):   

    def __init__(self):  
        self.exercicios = 100
        self.alimentacao = 100

        self.pesoExercicio = 0.4
        self.pesoAlimentacao = 0.6

    def energiaGeral(self):
        return ((self.exercicios * self.pesoExercicio) + (self.alimentacao * self.pesoAlimentacao)) / 100
        
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