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
    xc_cabeca = x + distancia_origem
    yc_cabeca = y - distancia_origem
    raio_cabeca = int(math.sqrt(distancia_origem**2 + distancia_origem**2))
    funcoes.bresenham_circulo(tela, xc_cabeca, yc_cabeca, raio_cabeca, BRANCO)
    funcoes.bresenham_circulo(tela, xc_cabeca, yc_cabeca, raio_cabeca+1, BRANCO) #Adicionar Grossura
    funcoes.scanline_fill_circle(tela, xc_cabeca, yc_cabeca, raio_cabeca+1, BRANCO)

    #Desenhar olho
    distancia_origem_x = 20
    distancia_origem_y = 15
    xc_olho = x + distancia_origem_x
    yc_olho = y - distancia_origem_y
    raio_olho = 2
    funcoes.bresenham_circulo(tela, xc_olho, yc_olho, raio_olho, PRETO)
    funcoes.scanline_fill_circle(tela, xc_olho, yc_olho, raio_olho, PRETO)

    #Desenhar óculos
    a = 5
    b = 8
    funcoes.bresenham_elipse(tela, xc_olho, yc_olho, a, b, AZUL)
    x_inicio_pe_oculos = xc_olho - a
    x_fim_pe_oculos = x_inicio_pe_oculos - 15
    funcoes.bresenham_reta(tela, x_inicio_pe_oculos, x_fim_pe_oculos, yc_olho, yc_olho, AZUL)
    x_fim_oculos = x_fim_pe_oculos - 10
    y_fim_oculos = yc_olho + 10
    funcoes.bresenham_reta(tela, x_fim_pe_oculos, x_fim_oculos, yc_olho, y_fim_oculos, AZUL)

    #Desenhar corpo
    x_fim_corpo_coxa_traseira = x - 50
    y_fim_corpo_coxa_traseira = y + 75
    funcoes.bresenham_reta(tela, x, x_fim_corpo_coxa_traseira, y, y_fim_corpo_coxa_traseira, BRANCO)
    funcoes.bresenham_reta(tela, x, x_fim_corpo_coxa_traseira, y+1, y_fim_corpo_coxa_traseira+1, BRANCO) #Adicionar Grossura

    #Desenhar perna de trás
    x_fim_perna_tras = x_fim_corpo_coxa_traseira - 40
    y_fim_perna_tras = y_fim_corpo_coxa_traseira - 25
    funcoes.bresenham_reta(tela, x_fim_corpo_coxa_traseira, x_fim_perna_tras, y_fim_corpo_coxa_traseira, y_fim_perna_tras, BRANCO)
    funcoes.bresenham_reta(tela, x_fim_corpo_coxa_traseira, x_fim_perna_tras, y_fim_corpo_coxa_traseira+1, y_fim_perna_tras+1, BRANCO) #Adicionar Grossura

    #Desenhar coxa da frente
    x_inicio_coxa_frente = x - 32
    y_inicio_coxa_frente = y + 50
    x_fim_coxa_frente = x_inicio_coxa_frente + 35
    y_fim_coxa_frente = y_inicio_coxa_frente - 5
    funcoes.bresenham_reta(tela, x_inicio_coxa_frente, x_fim_coxa_frente, y_inicio_coxa_frente, y_fim_coxa_frente, BRANCO)
    funcoes.bresenham_reta(tela, x_inicio_coxa_frente, x_fim_coxa_frente, y_inicio_coxa_frente+1, y_fim_coxa_frente+1, BRANCO) #Adicionar Grossura

    #Desenhar perna da frente
    x_fim_perna_frente = x_fim_coxa_frente - 20
    y_fim_perna_frente = y_fim_coxa_frente + 35
    funcoes.bresenham_reta(tela, x_fim_coxa_frente, x_fim_perna_frente, y_fim_coxa_frente, y_fim_perna_frente, BRANCO)
    funcoes.bresenham_reta(tela, x_fim_coxa_frente, x_fim_perna_frente, y_fim_coxa_frente+1, y_fim_perna_frente+1, BRANCO) #Adicionar Grossura

    #Desenhar braços
    x_braco_tras = x - 30
    x_braco_frente = x + 10
    y_braco_frente = y + 30
    funcoes.bresenham_reta(tela, x_braco_tras, x_braco_frente, y, y_braco_frente, BRANCO)
    funcoes.bresenham_reta(tela, x_braco_tras, x_braco_frente, y+1, y_braco_frente+1, BRANCO) #Adicionar Grossura

    #Desenhar antebraço de trás
    x_fim_antebraco_tras = x_braco_tras - 15
    y_fim_antebraco_tras = y + 10
    funcoes.bresenham_reta(tela, x_braco_tras, x_fim_antebraco_tras, y, y_fim_antebraco_tras, BRANCO)
    funcoes.bresenham_reta(tela, x_braco_tras, x_fim_antebraco_tras, y+1, y_fim_antebraco_tras+1, BRANCO) #Adicionar Grossura

    #Desenhar antebraço da frente
    x_fim_antebraco_frente = x_braco_frente + 15
    y_fim_antebraco_frente = y_braco_frente - 10
    funcoes.bresenham_reta(tela, x_braco_frente, x_fim_antebraco_frente, y_braco_frente, y_fim_antebraco_frente, BRANCO)
    funcoes.bresenham_reta(tela, x_braco_frente, x_fim_antebraco_frente, y_braco_frente+1, y_fim_antebraco_frente+1, BRANCO) #Adicionar Grossura


    
