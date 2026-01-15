import pygame
import sys

def setPixel(tela, x, y, cor):#Desenha um pixel
    tela.set_at((x, y), cor)

largura, altura = 600, 400
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
rodando = True 

pygame.init() #Inicialização

tela = pygame.display.set_mode((largura, altura)) #Tamanho da Janela
pygame.display.set_caption("Tigrinho") #Título da janela

clock = pygame.time.Clock()#Determina o FPS
clock.tick(60)

while rodando:
    for evento in pygame.event.get():#Verifica se algum evento foi acionado
        if evento.type == pygame.QUIT:#evento de saída
            rodando = False
    
    tela.fill(PRETO)#Preenche a tela com uma cor
    setPixel(tela, 100, 100, BRANCO)
    setPixel(tela, 100, 101, BRANCO)
    setPixel(tela, 100, 102, BRANCO)
    setPixel(tela, 100, 103, BRANCO)

    pygame.display.flip()#Atualiza a tela 

#Finalização
pygame.quit()
sys.exit()

    