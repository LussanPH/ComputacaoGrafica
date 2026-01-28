import funcoes
from constantes import BRANCO, PRETO, AZUL, VERMELHO, CARAMELO, CARAMELO_ESCURO
import math
import pygame

def desenhar_jogador(p_array, x, y, textura, invencivel=False):
    tempo = pygame.time.get_ticks()

    # Ficar invisível após a colisão
    if invencivel and (tempo // 100) % 2 == 0:
        return
    
    velocidade_anim = 0.005 
    amplitude_anim = 60
    
    oscilacao = math.sin(tempo * velocidade_anim) * amplitude_anim
    angulo = -20 + oscilacao
    angulo_negativo = -20 - oscilacao

    # Braço de trás
    braco_tras = [(x + 4, y - 4), (x + 6, y), (x - 12, y + 20), (x - 14, y + 16)]
    
    braco_tras = funcoes.rotacionar(braco_tras, angulo, (x, y))
    braco_tras = funcoes.transladar_pontos(braco_tras, -10, 10)
    funcoes.desenhar_poligono(p_array, braco_tras, CARAMELO_ESCURO)
    funcoes.scanline(p_array, braco_tras, CARAMELO_ESCURO)

    # Desenhar Mochila
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
    mochila_aumentada = funcoes.transladar_pontos(mochila_aumentada, 10, -7)
    funcoes.desenhar_poligono(p_array, mochila_aumentada, PRETO)
    funcoes.scanline(p_array, mochila_aumentada, PRETO)
    
    mochila = funcoes.transladar_pontos(mochila, 10, -7)
    funcoes.desenhar_poligono(p_array, mochila, VERMELHO)
    funcoes.scanline(p_array, mochila, VERMELHO)

    # Desenhar corpo
    corpo = [(x + 4, y - 4), (x + 6, y), (x - 18, y + 52), (x - 20, y + 50)]

    corpo = funcoes.transladar_pontos(corpo, 0, -2)
    funcoes.desenhar_poligono(p_array, corpo, BRANCO)
    funcoes.scanline(p_array, corpo, BRANCO)
    
    # Desenhar cabeça
    distancia_origem = 14
    lista_x_pontos = [] 

    xc_cabeca = x + distancia_origem
    yc_cabeca = y - distancia_origem
    raio_cabeca = int(math.sqrt(distancia_origem**2 + distancia_origem**2))

    # Passamos p_array aqui se sua função bresenham_circulo esperar o primeiro argumento
    pontos_circulo = funcoes.bresenham_circulo(p_array, xc_cabeca, yc_cabeca, raio_cabeca + 1, BRANCO) 
    pontos_circulo = funcoes.escala(pontos_circulo, 0.7, 0.7)
    
    for ponto in pontos_circulo:
        funcoes.setPixel(p_array, ponto[0], ponto[1], BRANCO)
        lista_x_pontos.append(ponto[0])

    # Chamada atualizada para receber o array e a textura original
    funcoes.setTexturaCabeca(p_array, textura, xc_cabeca, yc_cabeca, raio_cabeca + 1)

    # Perna de trás
    perna_tras = [(x + 4, y - 4), (x + 6, y), (x - 15, y + 30), (x - 17, y + 26)]

    perna_tras = funcoes.rotacionar(perna_tras, angulo_negativo, (x, y))
    perna_tras = funcoes.transladar_pontos(perna_tras, -25, 50)
    funcoes.desenhar_poligono(p_array, perna_tras, CARAMELO_ESCURO)
    funcoes.scanline(p_array, perna_tras, CARAMELO_ESCURO)
    
    # Perna da frente
    perna_frente = [(x + 4, y - 4), (x + 6, y), (x - 15, y + 30), (x - 17, y + 26)]
    
    perna_frente = funcoes.rotacionar(perna_frente, angulo, (x, y))
    perna_frente = funcoes.transladar_pontos(perna_frente, -18, 52)
    funcoes.desenhar_poligono(p_array, perna_frente, CARAMELO)
    funcoes.scanline(p_array, perna_frente, CARAMELO)

    # Braço da frente 
    braco_frente = [(x + 4, y - 4), (x + 6, y), (x - 12, y + 20), (x - 14, y + 16)]

    braco_frente = funcoes.rotacionar(braco_frente, angulo_negativo, (x, y))
    braco_frente = funcoes.transladar_pontos(braco_frente, -5, 15)
    funcoes.desenhar_poligono(p_array, braco_frente, CARAMELO)
    funcoes.scanline(p_array, braco_frente, CARAMELO)


def desenhar_pulo(p_array, x, y, textura, velocidade, invencivel=False):
    
    tempo = pygame.time.get_ticks()

    # Ficar invisível no pulo
    if invencivel and (tempo // 100) % 2 == 0:
        return

    # Braço de trás
    braco_tras = [(x + 4, y - 4), (x + 6, y), (x - 12, y + 20), (x - 14, y + 16)]
    
    if velocidade < 0:
        braco_tras = funcoes.rotacionar(braco_tras, 30, (x, y))
    else:
        braco_tras = funcoes.rotacionar(braco_tras, 90, (x, y))

    braco_tras = funcoes.transladar_pontos(braco_tras, -10, 10)
    funcoes.desenhar_poligono(p_array, braco_tras, CARAMELO_ESCURO)
    funcoes.scanline(p_array, braco_tras, CARAMELO_ESCURO)

    # Desenhar Mochila
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
    mochila_aumentada = funcoes.transladar_pontos(mochila_aumentada, 10, -7)
    funcoes.desenhar_poligono(p_array, mochila_aumentada, PRETO)
    funcoes.scanline(p_array, mochila_aumentada, PRETO)

    mochila = funcoes.transladar_pontos(mochila, 10, -7)
    funcoes.desenhar_poligono(p_array, mochila, VERMELHO)
    funcoes.scanline(p_array, mochila, VERMELHO)

    # Desenhar corpo
    corpo = [(x + 4, y - 4), (x + 6, y), (x - 18, y + 52), (x - 20, y + 50)]

    corpo = funcoes.transladar_pontos(corpo, 0, -2)
    funcoes.desenhar_poligono(p_array, corpo, BRANCO)
    funcoes.scanline(p_array, corpo, BRANCO)
    
    # Desenhar cabeça
    distancia_origem = 14
    lista_x_pontos = []

    xc_cabeca = x + distancia_origem
    yc_cabeca = y - distancia_origem
    raio_cabeca = int(math.sqrt(distancia_origem**2 + distancia_origem**2))

    pontos_circulo = funcoes.bresenham_circulo(p_array, xc_cabeca, yc_cabeca, raio_cabeca + 1, BRANCO) 
    pontos_circulo = funcoes.escala(pontos_circulo, 0.7, 0.7)
    
    for ponto in pontos_circulo:
        funcoes.setPixel(p_array, ponto[0], ponto[1], BRANCO)
        lista_x_pontos.append(ponto[0])

    funcoes.setTexturaCabeca(p_array, textura, xc_cabeca, yc_cabeca, raio_cabeca + 1)

    # Perna de trás
    perna_tras = [(x + 4, y - 4), (x + 6, y), (x - 15, y + 30), (x - 17, y + 26)]

    perna_tras = funcoes.rotacionar(perna_tras, 30, (x, y))

    if velocidade < 0:
        perna_tras = funcoes.rotacionar(perna_tras, 30, (x, y))
    else:
        perna_tras = funcoes.rotacionar(perna_tras, 70, (x, y))

    perna_tras = funcoes.transladar_pontos(perna_tras, -25, 50)
    funcoes.desenhar_poligono(p_array, perna_tras, CARAMELO_ESCURO)
    funcoes.scanline(p_array, perna_tras, CARAMELO_ESCURO)
    
    # Perna da frente
    perna_frente = [(x + 4, y - 4), (x + 6, y), (x - 15, y + 30), (x - 17, y + 26)]
    
    if velocidade < 0:
        perna_frente = funcoes.rotacionar(perna_frente, -60, (x, y))
    else:
        perna_frente = funcoes.rotacionar(perna_frente, -120, (x, y))

    perna_frente = funcoes.transladar_pontos(perna_frente, -18, 52)
    funcoes.desenhar_poligono(p_array, perna_frente, CARAMELO)
    funcoes.scanline(p_array, perna_frente, CARAMELO)

    # Braço da frente 
    braco_frente = [(x + 4, y - 4), (x + 6, y), (x - 12, y + 20), (x - 14, y + 16)]

    if velocidade < 0:
        braco_frente = funcoes.rotacionar(braco_frente, -60, (x, y))
    else:
        braco_frente = funcoes.rotacionar(braco_frente, -120, (x, y))

    braco_frente = funcoes.transladar_pontos(braco_frente, -5, 15)
    funcoes.desenhar_poligono(p_array, braco_frente, CARAMELO)
    funcoes.scanline(p_array, braco_frente, CARAMELO)
    

def desenhar_vida(p_array, vidas):
    cor_coracao = VERMELHO
    espacamento = 35
    x_inicial = 40
    y_pos = 40

    for i in range(vidas + 1):
        x = x_inicial + (i * espacamento)
        
        # 1. Parte de cima (Dois círculos pequenos)
        # Círculo da esquerda
        funcoes.scanline_fill_circle(p_array, x - 7, y_pos, 7, cor_coracao)
        # Círculo da direita
        funcoes.scanline_fill_circle(p_array, x + 7, y_pos, 7, cor_coracao)
        
        triangulo = [
            (x - 14, y_pos + 2), 
            (x + 14, y_pos + 2), 
            (x, y_pos + 15)
        ]
        funcoes.scanline(p_array, triangulo, cor_coracao)

def calcular_hitbox_jogador(x, y):

    corpo = (x - 20, y - 4, 26, 56)
    
    cabeca = (x + 2, y - 26, 24, 24)
    
    return [corpo, cabeca]