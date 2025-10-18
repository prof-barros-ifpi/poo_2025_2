import pygame
from Jogador import Jogador
from chao import Chao

# Inicialização
pygame.init()

# Configuração da tela
LARGURA = 800
ALTURA = 400
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Versão 0.2 - Gravidade e Chão")

# Cores
AZUL_CEU = (135, 206, 250)
relogio = pygame.time.Clock()

# Criar objetos
jogador = Jogador(100, 250)
chao = Chao(ALTURA - 50)

# Loop principal
rodando = True
while rodando:
    relogio.tick(30)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    teclas = pygame.key.get_pressed()
    jogador.mover(teclas, chao.y)

    tela.fill(AZUL_CEU)
    chao.desenhar(tela, LARGURA)
    jogador.desenhar(tela)
    pygame.display.update()

pygame.quit()
