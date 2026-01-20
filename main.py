import pygame
import sys
import funcoes
from constantes import largura, altura, BRANCO, PRETO
rodando = True 

pygame.init() #Inicialização

tela = pygame.display.set_mode((largura, altura)) #Tamanho da Janela
pygame.display.set_caption("RUn") #Título da janela

clock = pygame.time.Clock()#Determina o FPS
clock.tick(60)

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    
    tela.fill(PRETO)
    
    # Teste DDA (reta)
    funcoes.dda(tela, 0, 599, 0, 399, BRANCO)

    # Teste Bresenham (reta)
    funcoes.bresenham_reta(tela, 300, 500, 200, 350, BRANCO)

    # Teste CÍRCULO
    funcoes.bresenham_circulo(
        tela,
        xc=150,
        yc=200,
        r=80,
        cor=BRANCO
    )

    # Teste ELIPSE
    funcoes.bresenham_elipse(
        tela,
        xc=420,
        yc=200,
        a=120,   # raio horizontal
        b=60,    # raio vertical
        cor=BRANCO
    )

    pygame.display.flip() 

#Finalização
pygame.quit()
sys.exit()

    