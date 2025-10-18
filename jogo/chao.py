import pygame

class Chao:
    def __init__(self, y, cor=(50, 205, 50)):
        self.y = y
        self.cor = cor
        self.altura = 30

    def desenhar(self, tela, largura):
        pygame.draw.rect(tela, self.cor, (0, self.y, largura, self.altura))