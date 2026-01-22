import constantes
import funcoes

def desenhar_pombo(tela, x, y):
    # 1. ASA DE TRÁS 
    asa_1 = [(x, y - 5), (x + 10, y - 40), (x + 25, y - 5)]
    funcoes.scanline(tela, asa_1, constantes.CINZA_CHUMBO)
    funcoes.desenhar_poligono(tela, asa_1, constantes.PRETO)

    # 2. CAUDA 
    cauda = [(x + 20, y), (x + 45, y - 10), (x + 20, y + 10)]
    funcoes.scanline(tela, cauda, constantes.CINZA_CHUMBO)
    funcoes.desenhar_poligono(tela, cauda, constantes.PRETO) 

    # 3. CORPO 
    funcoes.scanline_fill_ellipse(tela, x, y, 25, 12, constantes.CINZA_ESCURO)
    funcoes.bresenham_elipse(tela, x, y, 25, 12, constantes.PRETO)

    # 4. ASA DA FRENTE 
    asa_2 = [(x - 10, y), (x - 5, y - 45), (x + 15, y)]
    funcoes.scanline(tela, asa_2, constantes.CINZA_CLARO)
    funcoes.desenhar_poligono(tela, asa_2, constantes.PRETO)

    # 5. CABEÇA E PESCOÇO
    funcoes.scanline_fill_circle(tela, x - 28, y - 8, 9, constantes.CINZA_ESCURO)
    funcoes.bresenham_circulo(tela, x - 28, y - 8, 9, constantes.PRETO)

    # 6. BICO E OLHO
    bico = [(x - 36, y - 8), (x - 44, y - 6), (x - 36, y - 4)]
    funcoes.scanline(tela, bico, constantes.LARANJA)
    funcoes.desenhar_poligono(tela, bico, constantes.PRETO)
    
    # Detalhe do Olho 
    funcoes.setPixel(tela, x - 32, y - 10, constantes.BRANCO)
    
