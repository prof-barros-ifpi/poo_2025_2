import pygame

class Jogador:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidade = 5
        self.altura_pulo = 10
        self.pulando = False
        self.forca_pulo = self.altura_pulo
        self.largura = 50
        self.altura = 70
        self.cor = (0, 128, 255)

    def mover(self, teclas):
        # Movimento horizontal
        if teclas[pygame.K_LEFT]:
            self.x -= self.velocidade
        if teclas[pygame.K_RIGHT]:
            self.x += self.velocidade

        # Pulo
        if not self.pulando:
            if teclas[pygame.K_UP]:
                self.pulando = True
        else:
            if self.forca_pulo > -self.altura_pulo:
                direcao = 1
                if self.forca_pulo < 0:
                    direcao = -1
                self.y -= (self.forca_pulo ** 2) * 0.5 * direcao
                self.forca_pulo -= 1
            else:
                self.pulando = False
                self.forca_pulo = self.altura_pulo

        # Abaixar
        if teclas[pygame.K_DOWN]:
            self.altura = 40
        else:
            self.altura = 70

    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, (self.x, self.y, self.largura, self.altura))
