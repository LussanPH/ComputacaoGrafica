import pygame
import sys
import math

from constantes import *
import funcoes

pygame.init()
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Testes – Algoritmos Gráficos")
clock = pygame.time.Clock()

pixel_array = pygame.PixelArray(tela)

# ===== MODOS DE TESTE =====
TESTE = 9
# 1 - DDA e Bresenham (retas)
# 2 - Polígono + Scanline
# 3 - Círculo (Bresenham + Fill)
# 4 - Elipse (Bresenham + Fill)
# 5 - Transformações (escala, translação, rotação)
# 6 - Clipping (Sutherland–Hodgman)
# 7 - Boundary Fill
# 8 - Gradiente Scanline
# 9 - Viewport

def desenhar_teste():
    tela.fill(AZUL)

    if TESTE == 1:
        funcoes.dda(pixel_array, 50, 300, 50, 200, PRETO)
        funcoes.bresenham_reta(pixel_array, 300, 100, 50, 250, VERMELHO)

    elif TESTE == 2:
        poligono = [(100,100),(300,120),(280,300),(120,280)]
        funcoes.desenhar_poligono(pixel_array, poligono, PRETO)
        funcoes.scanline(pixel_array, poligono, AZUL)

    elif TESTE == 3:
        pontos = funcoes.bresenham_circulo(pixel_array, 300, 200, 80, PRETO)
        for x,y in pontos:
            funcoes.setPixel(pixel_array, x, y, PRETO)
        funcoes.scanline_fill_circle(pixel_array, 300, 200, 78, VERMELHO)

    elif TESTE == 4:
        pontos = funcoes.bresenham_elipse(pixel_array, 300, 200, 120, 70, PRETO)
        for x,y in pontos:
            funcoes.setPixel(pixel_array, x, y, PRETO)
        funcoes.scanline_fill_ellipse(pixel_array, 300, 200, 118, 68, VERDE)

    elif TESTE == 5:
        pol = [(200,150),(300,150),(300,250),(200,250)]
        funcoes.desenhar_poligono(pixel_array, pol, PRETO)

        pol = funcoes.escala(pol, 1.3, 0.7)
        pol = funcoes.transladar_pontos(pol, 80, 0)
        centro = funcoes.calcular_centro_media(pol)
        pol = funcoes.rotacionar(pol, 30, centro)

        funcoes.desenhar_poligono(pixel_array, pol, VERMELHO)

    elif TESTE == 6:
        pol = [(50,50),(400,80),(350,300),(80,280)]
        clip = funcoes.sutherland_hodgman(pol, 150, 100, 450, 300)

        funcoes.desenhar_poligono(pixel_array, pol, PRETO)
        funcoes.desenhar_poligono(pixel_array, clip, VERMELHO)

    elif TESTE == 7:
        pol = [(150,150),(450,150),(450,350),(150,350)]
        funcoes.desenhar_poligono(pixel_array, pol, PRETO)
        funcoes.boundary_fill(pixel_array, 200, 200, PRETO, AZUL)

    elif TESTE == 8:
        pol = [(150,100),(450,120),(420,350),(180,330)]
        cores = [VERMELHO, AZUL, VERDE, LARANJA]
        funcoes.scanline_fill_gradiente(pixel_array, pol, cores)
        funcoes.desenhar_poligono(pixel_array, pol, PRETO)

    elif TESTE == 9:
        funcoes.viewport(pixel_array, largura//6, altura-60)

    pygame.display.flip()


# ===== LOOP PRINCIPAL =====
rodando = True
while rodando:
    clock.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_1: TESTE = 1
            if evento.key == pygame.K_2: TESTE = 2
            if evento.key == pygame.K_3: TESTE = 3
            if evento.key == pygame.K_4: TESTE = 4
            if evento.key == pygame.K_5: TESTE = 5
            if evento.key == pygame.K_6: TESTE = 6
            if evento.key == pygame.K_7: TESTE = 7
            if evento.key == pygame.K_8: TESTE = 8
            if evento.key == pygame.K_9: TESTE = 9

    desenhar_teste()

pixel_array.close()
pygame.quit()
sys.exit()