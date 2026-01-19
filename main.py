import pygame
import sys

largura, altura = 600, 400
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
rodando = True 

def setPixel(tela, x, y, cor):#Desenha um pixel
    if x < 0 or x > largura or y < 0 or y > altura:
        return
    else:
        tela.set_at((x, y), cor)

def dda(tela, x0, x1, y0, y1):#Desenha a reta
    deltaX = x1 - x0
    deltaY = y1 - y0

    passos = max(abs(deltaX), abs(deltaY))

    xIncremento = deltaX/passos
    yIncremento = deltaY/passos

    xNovo = x0
    yNovo = y0
    while yNovo != y1 and xNovo != x1:
        if tela.get_at((round(xNovo), round(yNovo))) == (255, 255, 255, 255):
            continue
        setPixel(tela, round(xNovo), round(yNovo), BRANCO)
        xNovo += xIncremento
        yNovo += yIncremento

def boundary_fill(surface,x,y,boundary_color,fill_color):
    stack=[]
    
    stack.append((x,y))
    while stack:
        x,y=stack.pop()
        if x < 0 or x >= largura or y < 0 or y >= altura:
           continue
        
        current_color=surface.get_at((x,y))
        
        if( current_color!= boundary_color and current_color != fill_color):
            setPixel(surface, x, y, fill_color)
            stack.append((x+1,y))
            stack.append((x-1,y))
            stack.append((x,y+1))
            stack.append((x,y-1))
             
def scanline(surface, pontos, cor):
    ys = [p[1] for p in pontos]
    ymin = min(ys)
    ymax = max(ys)

    n = len(pontos)

    for y in range(ymin, ymax):
        intersecoes = []

        for i in range(n):
            x0, y0 = pontos[i]
            x1, y1 = pontos[(i + 1) % n]

            # Ignorar arestas horizontais
            if y0 == y1:
                continue

            # Garantir y0 < y1
            if y0 > y1:
                x0, y0, x1, y1 = x1, y1, x0, y0

            # Scanline fora da aresta
            if y < y0 or y >= y1:
                continue

            # Cálculo da interseção
            x = x0 + (y - y0) * (x1 - x0) / (y1 - y0)
            intersecoes.append(x)

        intersecoes.sort()

        # Preenchimento entre pares
        for i in range(0, len(intersecoes), 2):
            if i + 1 < len(intersecoes):
                x_inicio = int(round(intersecoes[i]))
                x_fim = int(round(intersecoes[i + 1]))

                for x in range(x_inicio, x_fim + 1):
                    setPixel(surface, x, y, cor)

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

    dda(tela, 0, 600, 0, 400)

    pygame.display.flip()#Atualiza a tela 

#Finalização
pygame.quit()
sys.exit()

    