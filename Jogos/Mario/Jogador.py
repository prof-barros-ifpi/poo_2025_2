import pygame

class Jogador:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidade = 5
        self.gravidade = 2
        self.velocidade_vertical = 0
        self.altura_pulo = 15
        self.no_ar = False
        self.largura = 50
        self.altura = 70
        self.cor = (0, 128, 255)

    def mover(self, teclas, chao_y):
        # Movimento horizontal
        if teclas[pygame.K_LEFT]:
            self.x -= self.velocidade
        if teclas[pygame.K_RIGHT]:
            self.x += self.velocidade

        # Pulo
        if not self.no_ar and teclas[pygame.K_UP]:
            self.velocidade_vertical = -self.altura_pulo
            self.no_ar = True

        # Aplicar gravidade
        self.velocidade_vertical += self.gravidade
        self.y += self.velocidade_vertical

        # Colisão com o chão
        if self.y + self.altura >= chao_y:
            self.y = chao_y - self.altura
            self.no_ar = False
            self.velocidade_vertical = 0

        # Abaixar (sem interferir no pulo)
        if teclas[pygame.K_DOWN] and not self.no_ar:
            self.altura = 40
        else:
            self.altura = 70

        # Limites de tela
        if self.x < 0:
            self.x = 0
        if self.x + self.largura > 800:
            self.x = 800 - self.largura

    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, (self.x, self.y, self.largura, self.altura))