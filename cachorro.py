import funcoes
import constantes

def desenhar_cachorro(tela, x, y):
    
    h_perna = 25
    w_perna = 10

    # Pernas Traseiras (Fundo) 
    perna_tras_esq = [(x - 42, y), (x - 32, y), (x - 32, y + h_perna), (x - 42, y + h_perna)]
    perna_tras_dir = [(x - 12, y), (x - 2, y), (x - 2, y + h_perna), (x - 12, y + h_perna)]

    # Pernas Dianteiras (Frente)
    perna_frente_esq = [(x - 48, y + 2), (x - 38, y + 2), (x - 38, y + h_perna + 2), (x - 48, y + h_perna + 2)]
    perna_frente_dir = [(x - 18, y + 2), (x - 8, y + 2), (x - 8, y + h_perna + 2), (x - 18, y + h_perna + 2)]

    # Rabo e Orelha (Triangulares e retos)
    rabo = [(x + 5, y - 10), (x + 30, y - 35), (x + 15, y - 5)]
    orelha = [(x - 65, y - 40), (x - 50, y - 40), (x - 58, y - 20)]
    pescoco = [(x - 55, y - 10), (x - 40, y - 5), (x - 50, y - 25), (x - 60, y - 25)]

    # 1. DESENHAR AS PERNAS DO FUNDO (Preenchimento + Contorno)
    for perna in [perna_tras_esq, perna_tras_dir]:
        funcoes.scanline(tela, perna, constantes.CARAMELO)
        funcoes.desenhar_poligono(tela, perna, constantes.PRETO)

    # 2. DESENHAR O CORPO (Elipse mais achatada/menor)
    # Centro (xc, yc), Raios (rx, ry)
    xc_corpo, yc_corpo = x - 25, y - 12
    rx_corpo, ry_corpo = 35, 15 # Elipse menor que a versão anterior
    funcoes.scanline_fill_ellipse(tela, xc_corpo, yc_corpo, rx_corpo, ry_corpo, constantes.CARAMELO)
    funcoes.bresenham_elipse(tela, xc_corpo, yc_corpo, rx_corpo, ry_corpo, constantes.PRETO)

    # 3. PESCOÇO, RABO E ORELHA
    funcoes.scanline(tela, pescoco, constantes.CARAMELO)
    
    funcoes.scanline(tela, rabo, constantes.CARAMELO)
    funcoes.desenhar_poligono(tela, rabo, constantes.PRETO)

    funcoes.scanline(tela, orelha, constantes.CARAMELO)
    funcoes.desenhar_poligono(tela, orelha, constantes.PRETO)

    # 4. CABEÇA E FOCINHO (Círculo e elipse pequenos)
    xc_cabeca, yc_cabeca = x - 60, y - 30
    r_cabeca = 14
    funcoes.scanline_fill_circle(tela, xc_cabeca, yc_cabeca, r_cabeca, constantes.CARAMELO)
    funcoes.bresenham_circulo(tela, xc_cabeca, yc_cabeca, r_cabeca, constantes.PRETO)

    # Focinho pequeno
    funcoes.scanline_fill_ellipse(tela, x - 72, y - 28, 10, 6, constantes.CARAMELO)
    funcoes.bresenham_elipse(tela, x - 72, y - 28, 10, 6, constantes.PRETO)

    # 5. DESENHAR AS PERNAS DA FRENTE (Por cima do corpo)
    for perna in [perna_frente_esq, perna_frente_dir]:
        funcoes.scanline(tela, perna, constantes.CARAMELO)
        funcoes.desenhar_poligono(tela, perna, constantes.PRETO)

    #6. ORELHAS (Triângulos poligonais) ---
    orelha = [(x - 62, y - 40), (x - 52, y - 40), (x - 57, y - 30)]
    funcoes.scanline(tela, orelha, constantes.CARAMELO)
    funcoes.desenhar_poligono(tela, orelha, constantes.PRETO)

    # 7. DETALHES FINAIS (Rosto)
    # Olho
    funcoes.scanline_fill_circle(tela, x - 65, y - 33, 2, constantes.BRANCO)
    # Nariz (Ponta do focinho)
    funcoes.scanline_fill_circle(tela, x - 80, y - 28, 3, constantes.PRETO)
    # Boca
    funcoes.bresenham_reta(tela, x - 78, x - 70, y - 23, y - 23, constantes.VERMELHO_ESCURO)