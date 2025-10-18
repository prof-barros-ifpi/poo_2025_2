import pygame
from Jogador import Jogador

# Inicialização
pygame.init()

# Configuração da tela
LARGURA = 800
ALTURA = 400
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Versão 0.1 - Movimento Básico")

# Cores
BRANCO = (255, 255, 255)

# Criar jogador
jogador = Jogador(100, 300)

# Loop principal
rodando = True
relogio = pygame.time.Clock()

while rodando:
    relogio.tick(30)  # FPS

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Ler teclas pressionadas
    teclas = pygame.key.get_pressed()
    jogador.mover(teclas)

    # Atualizar tela
    tela.fill(BRANCO)
    jogador.desenhar(tela)
    pygame.display.update()

pygame.quit()
