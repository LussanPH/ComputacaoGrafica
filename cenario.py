import pygame
import funcoes
from constantes import largura, altura, BRANCO, PRETO, CINZA, AZUL, CINZA_ESCURO,VERDE,BEGE,TELHA

def cenario_padrao(tela):
    #Definir cor de fundo
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

    #Desenhar chão
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
     
    #Desenhar colunas e detalhes em cinza escuro 
    largura_coluna = 40
    espacamento = largura // 4
    altura_base_capital = 15 

    for i in range(1,4):
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
        
def cenario_ru(tela):
    # Definir cor de fundo
    y_topo = 0
    y_base = altura - 1
    fundo = [
        (0, y_topo),
        (largura - 1, y_topo),
        (largura - 1, y_base),
        (0, y_base)
    ]
    funcoes.desenhar_poligono(tela, fundo, AZUL)
    funcoes.scanline(tela, fundo, AZUL)

    # Desenhar chão
    y_topo = altura - altura // 3
    y_base = altura - 1
    chao = [
        (0, y_topo),
        (largura - 1, y_topo),
        (largura - 1, y_base),
        (0, y_base)
    ]
    funcoes.desenhar_poligono(tela, chao, CINZA)
    funcoes.scanline(tela, chao, CINZA)
    funcoes.desenhar_poligono(tela, [(0, y_topo), (largura - 1, y_topo)], PRETO)

    # Desenhar colunas e detalhes em cinza escuro 
    largura_coluna = 40
    espacamento = largura // 4
    altura_base_capital = 15

    for i in range(1, 3):
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

    # retângulo bege (RU)
    y_topo = altura - altura // 3
    largura_ru = largura - largura // 6
    y_base = 0
    chao_bege = [
        (largura_ru, y_topo),
        (largura - 1, y_topo),
        (largura - 1, y_base),
        (largura_ru, y_base)
    ]
    funcoes.desenhar_poligono(tela, chao_bege, BEGE)
    funcoes.scanline(tela, chao_bege, BEGE)

    # teto telha
    y_topo_teto = altura - 3 * altura // 4
    largura_teto = largura - 360
    y_base_teto = y_topo_teto - 20
    teto = [
        (largura_teto, y_topo_teto),
        (largura_ru, y_topo_teto),
        (largura_ru, y_base_teto),
        (largura_teto, y_base_teto)
    ]
    funcoes.desenhar_poligono(tela, teto, TELHA)
    funcoes.scanline(tela, teto, TELHA)
    
    y_topo_teto2 = y_base_teto
    largura_teto2 = largura_teto+30
    y_base_teto2 = y_topo_teto2 - 20
    teto = [
        (largura_teto2, y_topo_teto2),
        (largura_ru, y_topo_teto2),
        (largura_ru, y_base_teto2),
        (largura_teto2, y_base_teto2)
    ]
    funcoes.desenhar_poligono(tela, teto, TELHA)
    funcoes.scanline(tela, teto, TELHA)
    
    y_topo_teto3 = y_base_teto2
    largura_teto3 = largura_teto2+30
    y_base_teto3 = y_topo_teto3 - 20
    teto = [
        (largura_teto3, y_topo_teto3),
        (largura_ru, y_topo_teto3),
        (largura_ru, y_base_teto3),
        (largura_teto3, y_base_teto3)
    ]
    funcoes.desenhar_poligono(tela, teto, TELHA)
    funcoes.scanline(tela, teto, TELHA)
    
    espacamento = (largura_teto + largura_ru) // 2 - 70
    y_topo_chao = altura - altura // 3
    largura_coluna = 20

    coluna_teto = [
        (espacamento - largura_coluna // 2, y_topo_teto),
        (espacamento + largura_coluna // 2, y_topo_teto),
        (espacamento + largura_coluna // 2, y_topo_chao),
        (espacamento - largura_coluna // 2, y_topo_chao)
    ]
    funcoes.desenhar_poligono(tela, coluna_teto, CINZA)
    funcoes.scanline(tela, coluna_teto, CINZA)

    base_teto = [
        (espacamento - (largura_coluna // 2 + 10), y_topo_chao - altura_base_capital),
        (espacamento + (largura_coluna // 2 + 10), y_topo_chao - altura_base_capital),
        (espacamento + (largura_coluna // 2 + 10), y_topo_chao),
        (espacamento - (largura_coluna // 2 + 10), y_topo_chao)
    ]
    funcoes.desenhar_poligono(tela, base_teto, CINZA_ESCURO)
    funcoes.scanline(tela, base_teto, CINZA_ESCURO)

    #Texto RU
    font_size = max(12, int((y_topo) * 0.25))  
    font = pygame.font.SysFont(None, font_size, bold=True)
    text_surf = font.render("RU", True, PRETO)
    center_x = (largura_ru + (largura - 1)) // 2
    center_y = y_topo // 2
    text_rect = text_surf.get_rect(center=(center_x, center_y))
    tela.blit(text_surf, text_rect)

    
        