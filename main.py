import pygame
import sys
import cenario
import jogador
from constantes import *

pygame.init()
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Djonga RUn")

clock = pygame.time.Clock()
rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill(AZUL)

    cenario.atualizar()
    cenario.desenhar(tela)

    jogador.desenhar_jogador(tela, 175, 200)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()