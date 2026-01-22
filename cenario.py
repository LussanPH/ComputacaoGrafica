import pygame
import funcoes
from constantes import largura, altura, BRANCO, PRETO, CINZA, AZUL, CINZA_ESCURO,VERDE

def cenario(tela):
    y_topo = 0
    y_base = altura - 1
    fundo= [
        (0, y_topo),
        (largura - 1, y_topo),
        (largura - 1, y_base),
        (0, y_base)
    ]
    funcoes.desenhar_poligono(tela,fundo,AZUL)
    funcoes.scanline(tela, fundo, AZUL)

    y_topo = altura - altura // 3
    y_base = altura - 1
    chao = [
        (0, y_topo),
        (largura - 1, y_topo),
        (largura - 1, y_base),
        (0, y_base)
    ]
    funcoes.desenhar_poligono(tela, chao,CINZA)
    funcoes.scanline(tela, chao, CINZA)
    funcoes.desenhar_poligono(tela, [(0, y_topo), (largura, y_topo)], PRETO)

    largura_coluna = 40
    espacamento = largura // 4
    altura_base_capital = 15 

    for i in range(1, 4):
        x_centro = i * espacamento
        
        coluna = [
            (x_centro - largura_coluna // 2, 0),
            (x_centro + largura_coluna // 2, 0),
            (x_centro + largura_coluna // 2, y_topo),
            (x_centro - largura_coluna // 2, y_topo)
        ]
        funcoes.desenhar_poligono(tela, coluna, CINZA)
        funcoes.scanline(tela, coluna, CINZA)

        base = [
            (x_centro - (largura_coluna // 2 + 10), y_topo - altura_base_capital),
            (x_centro + (largura_coluna // 2 + 10), y_topo - altura_base_capital),
            (x_centro + (largura_coluna // 2 + 10), y_topo),
            (x_centro - (largura_coluna // 2 + 10), y_topo)
        ]
        funcoes.desenhar_poligono(tela, base, CINZA_ESCURO)
        funcoes.scanline(tela, base, CINZA_ESCURO)

        linha_sombra = [
            (x_centro + largura_coluna // 4, 0),
            (x_centro + largura_coluna // 4, y_topo - altura_base_capital)
        ]
        funcoes.desenhar_poligono(tela, linha_sombra, CINZA_ESCURO)