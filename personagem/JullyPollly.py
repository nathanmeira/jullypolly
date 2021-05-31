import pygame, sys
from pygame.locals import *

class JullyPollly(object):   

    def __init__(self):  
        self.exercicios = 100
        self.alimentacao = 100

        self.pesoExercicio = 0.4
        self.pesoAlimentacao = 0.6

        self.variacaoExercicio = 0.18
        self.variacaoAlimentacao = 0.13

        self.score = 0
        self.qtdCenoura = 0
        self.qtdUva = 0
        self.qtdMorango = 0
        self.qtdHotDog = 0
    
    def energiaGeralPorcentagem(self):
        return self.energiaGeral() / 100

    def energiaGeral(self):
        return ((self.exercicios * self.pesoExercicio) + (self.alimentacao * self.pesoAlimentacao))
        
    def setExercicios(self, variacao):
        self.exercicios += variacao
        if(self.exercicios <= 0):
            self.exercicios = 0
        if(self.exercicios > 100):
            self.exercicios = 100

    def setAlimentacao(self, variacao):
        self.alimentacao += variacao
        if(self.alimentacao <= 0):
            self.alimentacao = 0
        if(self.alimentacao > 100):
            self.alimentacao = 100

    def getExercicio(self):
        return self.exercicios / 100

    def getAlimentacao(self):
        return self.alimentacao / 100

    def tempoVidaRestanteSegundos(self):
        if(self.energiaGeral() > 1):
            return int(self.energiaGeral()) 
        return round(self.energiaGeral(), 2)

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def resetStatusPersonagem(self):
        self.exercicios = 100
        self.alimentacao = 100
        self.score = 0

        self.score = 0
        self.qtdCenoura = 0
        self.qtdUva = 0
        self.qtdMorango = 0
        self.qtdHotDog = 0

    def addStatusVida(self, fruit):
        variacao = 0
        if(fruit == 'carrot'):
            variacao = 3
            self.qtdCenoura += 1
        if(fruit == 'strawberry'):
            variacao = 4
            self.qtdMorango += 1
        if(fruit == 'grape'):
            variacao = 2
            self.qtdUva += 1
        self.setAlimentacao(variacao)

    def addStatusExercicio(self):
        self.setExercicios(1.5)

    def addScore(self, point):
        self.score += point
        self.qtdHotDog += 1
        if(self.score <= 0):
            self.score = 0

    def getScore(self): 
        return int(self.score)