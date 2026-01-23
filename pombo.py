import math
from constantes import CINZA_CHUMBO, CINZA_CLARO, CINZA_ESCURO, PRETO, LARANJA, BRANCO
from funcoes import rotacionar, scanline, desenhar_poligono, scanline_fill_ellipse, bresenham_elipse, scanline_fill_circle, bresenham_circulo, setPixel

def desenhar_pombo(tela, x, y, fase):
    # LÓGICA DE ANIMAÇÃO
    velocidade_batida = 0.2
    # Ângulo oscila entre -45 e 45 graus
    angulo_asa = math.sin(fase * velocidade_batida) * 30

    # Balanço vertical do corpo sincronizado com a batida
    balanco = int(abs(math.sin(fase * velocidade_batida)) * 4)
    y_corpo = y + balanco
    x = int(x)

    # CABEÇA E DETALHES
    x_head, y_head = x - 28, y_corpo - 8
    scanline_fill_circle(tela, x_head, y_head, 9, CINZA_ESCURO)
    bresenham_circulo(tela, x_head, y_head, 9, PRETO)
    
    # Bico
    bico = [(x_head - 8, y_head), (x_head - 16, y_head + 2), (x_head - 8, y_head + 4)]
    scanline(tela, bico, LARANJA)
    desenhar_poligono(tela, bico, PRETO)
    
    # Olho
    setPixel(tela, int(x_head - 3), int(y_head - 2), BRANCO)

    # --- 2. ASA DE TRÁS (Fundo) ---
    asa_base_1 = [(x, y_corpo - 5), (x + 30, y_corpo - 40), (x + 15, y_corpo - 5)]
    ombro_1 = (x, y_corpo - 5)
    
    asa_1_rot = rotacionar(asa_base_1, angulo_asa + 10, ombro_1)
    
    scanline(tela, asa_1_rot, CINZA_CHUMBO)
    desenhar_poligono(tela, asa_1_rot, PRETO)

    # CAUDA E CORPO
    cauda = [(x + 20, y_corpo), (x + 45, y_corpo - 10), (x + 20, y_corpo + 10)]
    scanline(tela, cauda, CINZA_CHUMBO)
    desenhar_poligono(tela, cauda, PRETO)

    scanline_fill_ellipse(tela, x, y_corpo, 25, 12, CINZA_ESCURO)
    bresenham_elipse(tela, x, y_corpo, 25, 12, PRETO)

    # ASA DA FRENTE 
    asa_base_2 = [(x - 10, y_corpo), (x - 20, y_corpo - 45), (x + 10, y_corpo)]
    ombro_2 = (x - 5, y_corpo)
    asa_2_rot = rotacionar(asa_base_2, -angulo_asa, ombro_2)
    
    scanline(tela, asa_2_rot, CINZA_CLARO)
    desenhar_poligono(tela, asa_2_rot, PRETO)
    
def processar_pombos(tela, lista):
    for p in lista[:]:
        p["x"] -= p["vel"]
        p["fase"] += 1
        
        # Chamada do desenho
        desenhar_pombo(tela, p["x"], p["y"], p["fase"])
        
        # Lógica de remoção para otimização
        if p["x"] < -100:
            lista.remove(p)