import pygame
import sys
import funcoes
import telas
import jogador
import cachorro
import cenario
from constantes import largura, altura, BRANCO, PRETO,AZUL, LARANJA
import pombo

lista_pombos = [
    {"x": 700, "y": 100, "fase": 0, "vel": 4},
    {"x": 900, "y": 150, "fase": 30, "vel": 2} # Esse está em outra fase da batida
]

lista_cachorros = [
    {"x": 600, "y": 280, "fase": 0, "vel": 3}
]

rodando = True 

pygame.init() #Inicialização

tela = pygame.display.set_mode((largura, altura)) #Tamanho da Janela
pygame.display.set_caption("Djonga RUn") #Título da janela

telas.tela_start(tela)
clock = pygame.time.Clock()#Determina o FPS

angulo_jogador = 0

while rodando:

    dt = clock.tick(60) / 1000.0 

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    
    tela.fill(AZUL)

    cenario.atualizar(dt) 
    cenario.desenhar(tela)

    cachorro.processar_cachorros(tela, lista_cachorros)
    pombo.processar_pombos(tela, lista_pombos)
    
    jogador.desenhar_jogador(tela, 175, 225)

    pygame.display.flip()
#Finalização
pygame.quit()
sys.exit()

    