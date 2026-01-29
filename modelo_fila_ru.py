from constantes import *
import funcoes
import math
import pygame


def desenhar_modelo(tela, x, y, cor, textura):
    #Braço de tras
    braco_tras = [(x + 4, y - 4), (x + 6, y), (x - 12, y + 20), (x - 14, y + 16)]

    braco_tras = funcoes.transladar_pontos(braco_tras, 0, 10)
    funcoes.desenhar_poligono(tela, braco_tras, CARAMELO_ESCURO)
    funcoes.scanline(tela, braco_tras, CARAMELO_ESCURO)

    #Desenhar Mochila
    x_superior_direito = x - 10
    y_superior_direito = y + 10
    x_superior_esquerdo = x - 20
    y_superior_esquerdo = y + 5
    x_inferior_direito = x - 25
    y_inferior_direito = y + 40
    x_inferior_esquerdo = x - 34
    y_inferior_esquerdo = y + 37
    mochila = [
        (x_superior_direito, y_superior_direito),
        (x_superior_esquerdo, y_superior_esquerdo),
        (x_inferior_esquerdo, y_inferior_esquerdo),
        (x_inferior_direito, y_inferior_direito)
    ]
    mochila_aumentada = funcoes.escala(mochila, 1.05, 1.05)
    mochila_aumentada = funcoes.rotacionar(mochila_aumentada, -20, (x,y))
    mochila_aumentada = funcoes.transladar_pontos(mochila_aumentada, 10, -7)
    funcoes.desenhar_poligono(tela, mochila_aumentada, PRETO)
    funcoes.scanline(tela, mochila_aumentada, PRETO)
    mochila = funcoes.rotacionar(mochila, -20, (x,y))
    mochila = funcoes.transladar_pontos(mochila, 10, -7)
    funcoes.desenhar_poligono(tela, mochila, cor)
    funcoes.scanline(tela, mochila, cor)

    #Desenhar corpo
    corpo = [(x + 4, y - 4), (x + 6, y), (x - 18, y + 52), (x - 20, y + 50)]

    corpo = funcoes.rotacionar(corpo, -23, (x, y))

    corpo = funcoes.transladar_pontos(corpo, 0, -2)
    funcoes.desenhar_poligono(tela, corpo, BRANCO)
    funcoes.scanline(tela, corpo, BRANCO)
    
    #Desenhar cabeça
    distancia_origem = 14

    yc_cabeca = int(y - distancia_origem)
    raio_cabeca = int(math.sqrt(distancia_origem**2 + distancia_origem**2))

    pontos_circulo = funcoes.bresenham_circulo(tela, x + 4, yc_cabeca, raio_cabeca+1, BRANCO) 
    pontos_circulo = funcoes.escala(pontos_circulo, 0.7, 0.7)

    funcoes.setTexturaCabeca(tela, textura, x + 4, yc_cabeca, raio_cabeca+1)

    #Perna de trás
    perna_tras = [(x + 4, y - 4), (x + 6, y), (x - 15, y + 30), (x - 17, y + 26)]

    perna_tras = funcoes.rotacionar(perna_tras, -10, (x, y))

    perna_tras = funcoes.transladar_pontos(perna_tras, -5, 50)
    funcoes.desenhar_poligono(tela, perna_tras, CARAMELO_ESCURO)
    funcoes.scanline(tela, perna_tras, CARAMELO_ESCURO)
    
    #Perna da frente
    perna_frente = [(x + 4, y - 4), (x + 6, y), (x - 15, y + 30), (x - 17, y + 26)]

    perna_frente = funcoes.rotacionar(perna_frente, -50, (x, y))

    perna_frente = funcoes.transladar_pontos(perna_frente, 0, 52)
    funcoes.desenhar_poligono(tela, perna_frente, CARAMELO)
    funcoes.scanline(tela, perna_frente, CARAMELO)

    #Braço da frente 
    braco_frente = [(x + 4, y - 4), (x + 6, y), (x - 12, y + 20), (x - 14, y + 16)]

    braco_frente = funcoes.rotacionar(braco_frente, -60, (x, y))

    braco_frente = funcoes.transladar_pontos(braco_frente, 5, 15)
    funcoes.desenhar_poligono(tela, braco_frente, CARAMELO)
    funcoes.scanline(tela, braco_frente, CARAMELO)

