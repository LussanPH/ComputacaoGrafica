import funcoes
from constantes import BRANCO, PRETO, AZUL, VERMELHO
import math

def desenhar_jogador(tela, x, y):
    
    #Desenhar Mochila
    x_superior_direito = x - 10
    y_superior_direito = y + 10
    x_superior_esquerdo = x - 20
    y_superior_esquerdo = y
    x_inferior_direito = x - 30
    y_inferior_direito = y + 40
    x_inferior_esquerdo = x - 40
    y_inferior_esquerdo = y + 30
    mochila = [
        (x_superior_direito, y_superior_direito),
        (x_superior_esquerdo, y_superior_esquerdo),
        (x_inferior_esquerdo, y_inferior_esquerdo),
        (x_inferior_direito, y_inferior_direito)
    ]
    mochila_aumentada = funcoes.escala(mochila, 1.05, 1.05)
    funcoes.desenhar_poligono(tela, mochila_aumentada, PRETO)
    funcoes.scanline(tela, mochila_aumentada, PRETO)
    funcoes.desenhar_poligono(tela, mochila, VERMELHO)
    funcoes.scanline(tela, mochila, VERMELHO)

    #Desenhar cabeça
    distancia_origem = 14
    lista_x_pontos = [] #Vai ser necessário para calcular o novo raio

    xc_cabeca = x + distancia_origem
    yc_cabeca = y - distancia_origem
    raio_cabeca = int(math.sqrt(distancia_origem**2 + distancia_origem**2))

    pontos_circulo = funcoes.bresenham_circulo(tela, xc_cabeca, yc_cabeca, raio_cabeca, BRANCO)
    pontos_circulo = funcoes.escala(pontos_circulo, 0.7, 0.7)
    pontos_circulo = funcoes.transladar_pontos(pontos_circulo, -13, 13)
    for ponto in pontos_circulo:
        funcoes.setPixel(tela, ponto[0], ponto[1], BRANCO)

    pontos_circulo = funcoes.bresenham_circulo(tela, xc_cabeca, yc_cabeca, raio_cabeca+1, BRANCO) #Adicionar Grossura
    pontos_circulo = funcoes.escala(pontos_circulo, 0.7, 0.7)
    pontos_circulo = funcoes.transladar_pontos(pontos_circulo, -13, 13)
    for ponto in pontos_circulo:
        funcoes.setPixel(tela, ponto[0], ponto[1], BRANCO)
        lista_x_pontos.append(ponto[0])
    
    x_max_direita = max(lista_x_pontos)
    x_max_esquerda = min(lista_x_pontos)
    raio_escalonado = int((abs(x_max_direita - x_max_esquerda))/2)

    xc_cabeca -= 13
    yc_cabeca += 13

    funcoes.scanline_fill_circle(tela, xc_cabeca, yc_cabeca, raio_escalonado, BRANCO)

    #Desenhar olho
    distancia_origem_x = 20
    distancia_origem_y = 15

    xc_olho = x + distancia_origem_x
    yc_olho = y - distancia_origem_y
    raio_olho = 2

    pontos_circulo = funcoes.bresenham_circulo(tela, xc_olho, yc_olho, raio_olho, PRETO)
    pontos_circulo = funcoes.transladar_pontos(pontos_circulo, -13, 13)
    for ponto in pontos_circulo:
        funcoes.setPixel(tela, ponto[0], ponto[1], PRETO)

    xc_olho -= 13
    yc_olho += 13

    funcoes.scanline_fill_circle(tela, xc_olho, yc_olho, raio_olho, PRETO)

    #Desenhar óculos
    a = 5
    b = 8

    pontos_elipse = funcoes.bresenham_elipse(tela, xc_olho, yc_olho, a, b, AZUL)
    for ponto in pontos_elipse:
        funcoes.setPixel(tela, ponto[0], ponto[1], VERMELHO)

    x_inicio_pe_oculos = xc_olho - a
    x_fim_pe_oculos = x_inicio_pe_oculos - 8
    funcoes.bresenham_reta(tela, x_inicio_pe_oculos, x_fim_pe_oculos, yc_olho, yc_olho, AZUL)
    x_fim_oculos = x_fim_pe_oculos - 3
    y_fim_oculos = yc_olho + 3
    funcoes.bresenham_reta(tela, x_fim_pe_oculos, x_fim_oculos, yc_olho, y_fim_oculos, AZUL)

    #Desenhar corpo
    x_fim_corpo_coxa_traseira = x - 50
    y_fim_corpo_coxa_traseira = y + 65
    pontos_escalonados = funcoes.escala([(x, y),
                                         (x_fim_corpo_coxa_traseira, y_fim_corpo_coxa_traseira)], 0.7, 0.7)
    funcoes.bresenham_reta(tela,
        pontos_escalonados[0][0], 
        pontos_escalonados[1][0], 
        pontos_escalonados[0][1], 
        pontos_escalonados[1][1], BRANCO)

    funcoes.bresenham_reta(tela, 
        pontos_escalonados[0][0], 
        pontos_escalonados[1][0],
        pontos_escalonados[0][1]+1,
        pontos_escalonados[1][1]+1, BRANCO) #Adicionar Grossura
    
    #Desenhar perna de trás
    x_fim_perna_tras = x_fim_corpo_coxa_traseira - 30
    y_fim_perna_tras = y_fim_corpo_coxa_traseira - 15
    pontos_escalonados = funcoes.escala([(x_fim_corpo_coxa_traseira, y_fim_corpo_coxa_traseira), 
                                         (x_fim_perna_tras, y_fim_perna_tras)], 0.7, 0.7)
    
    pontos_escalonados = funcoes.transladar_pontos(pontos_escalonados, 12, -5)

    funcoes.bresenham_reta(tela,
        pontos_escalonados[0][0], 
        pontos_escalonados[1][0], 
        pontos_escalonados[0][1], 
        pontos_escalonados[1][1], BRANCO)
    
    funcoes.bresenham_reta(tela, 
        pontos_escalonados[0][0], 
        pontos_escalonados[1][0],
        pontos_escalonados[0][1]+1,
        pontos_escalonados[1][1]+1, BRANCO) #Adicionar Grossura

    #Desenhar coxa da frente
    x_inicio_coxa_frente = x - 37
    y_inicio_coxa_frente = y + 50
    x_fim_coxa_frente = x_inicio_coxa_frente + 30
    y_fim_coxa_frente = y_inicio_coxa_frente - 5
    pontos_escalonados = funcoes.escala([(x_inicio_coxa_frente, y_inicio_coxa_frente), 
                                         (x_fim_coxa_frente, y_fim_coxa_frente)], 0.7, 0.7)
    
    pontos_escalonados = funcoes.transladar_pontos(pontos_escalonados, -5, 0)

    funcoes.bresenham_reta(tela,
        pontos_escalonados[0][0], 
        pontos_escalonados[1][0], 
        pontos_escalonados[0][1], 
        pontos_escalonados[1][1], BRANCO)
    
    funcoes.bresenham_reta(tela, 
        pontos_escalonados[0][0], 
        pontos_escalonados[1][0],
        pontos_escalonados[0][1]+1,
        pontos_escalonados[1][1]+1, BRANCO) #Adicionar Grossura #Adicionar Grossura

    #Desenhar perna da frente
    x_fim_perna_frente = x_fim_coxa_frente - 20
    y_fim_perna_frente = y_fim_coxa_frente + 35
    pontos_escalonados = funcoes.escala([(x_fim_coxa_frente, y_fim_coxa_frente),
                                         (x_fim_perna_frente, y_fim_perna_frente)], 0.7, 0.7)
    
    pontos_escalonados = funcoes.transladar_pontos(pontos_escalonados, -6, -5)
    funcoes.bresenham_reta(tela,
        pontos_escalonados[0][0], 
        pontos_escalonados[1][0], 
        pontos_escalonados[0][1], 
        pontos_escalonados[1][1], BRANCO)
    
    funcoes.bresenham_reta(tela, 
        pontos_escalonados[0][0], 
        pontos_escalonados[1][0],
        pontos_escalonados[0][1]+1,
        pontos_escalonados[1][1]+1, BRANCO) #Adicionar Grossura

    #Desenhar braços
    x_braco_tras = x - 30
    x_braco_frente = x + 10
    y_braco_frente = y + 30
    pontos_escalonados = funcoes.escala([(x_braco_tras, y),
                                         (x_braco_frente, y_braco_frente)], 0.7, 0.7)
    funcoes.bresenham_reta(tela,
        pontos_escalonados[0][0], 
        pontos_escalonados[1][0], 
        pontos_escalonados[0][1], 
        pontos_escalonados[1][1], BRANCO)
    
    funcoes.bresenham_reta(tela, 
        pontos_escalonados[0][0], 
        pontos_escalonados[1][0],
        pontos_escalonados[0][1]+1,
        pontos_escalonados[1][1]+1, BRANCO) #Adicionar Grossura

    #Desenhar antebraço de trás
    x_fim_antebraco_tras = x_braco_tras - 15
    y_fim_antebraco_tras = y + 10
    pontos_escalonados = funcoes.escala([(x_braco_tras, y), 
                                         (x_fim_antebraco_tras, y_fim_antebraco_tras)], 0.7, 0.7)
    
    pontos_escalonados = funcoes.transladar_pontos(pontos_escalonados, 8, 2)

    funcoes.bresenham_reta(tela,
        pontos_escalonados[0][0], 
        pontos_escalonados[1][0], 
        pontos_escalonados[0][1], 
        pontos_escalonados[1][1], BRANCO)
    
    funcoes.bresenham_reta(tela, 
        pontos_escalonados[0][0], 
        pontos_escalonados[1][0],
        pontos_escalonados[0][1]+1,
        pontos_escalonados[1][1]+1, BRANCO) #Adicionar Grossura

    #Desenhar antebraço da frente
    x_fim_antebraco_frente = x_braco_frente + 15
    y_fim_antebraco_frente = y_braco_frente - 10
    pontos_escalonados = funcoes.escala([(x_braco_frente, y_braco_frente),
                                         (x_fim_antebraco_frente, y_fim_antebraco_frente)], 0.7, 0.7)
    
    pontos_escalonados = funcoes.transladar_pontos(pontos_escalonados, -7, -2)

    funcoes.bresenham_reta(tela,
        pontos_escalonados[0][0], 
        pontos_escalonados[1][0], 
        pontos_escalonados[0][1], 
        pontos_escalonados[1][1], BRANCO)
    
    funcoes.bresenham_reta(tela, 
        pontos_escalonados[0][0], 
        pontos_escalonados[1][0],
        pontos_escalonados[0][1]+1,
        pontos_escalonados[1][1]+1, BRANCO) #Adicionar Grossura


    
