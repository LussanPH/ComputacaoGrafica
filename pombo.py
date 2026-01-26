import math
from constantes import CINZA_CHUMBO, CINZA_CLARO, CINZA_ESCURO, PRETO, LARANJA, BRANCO
from funcoes import rotacionar, scanline, desenhar_poligono, scanline_fill_ellipse, bresenham_elipse, scanline_fill_circle, bresenham_circulo, setPixel

def desenhar_pombo(tela, x, y, fase, mostrar_hitbox=False):
    # LÓGICA DE ANIMAÇÃO 
    velocidade_batida = 0.2
    angulo_asa = math.sin(fase * velocidade_batida) * 30
    balanco = int(abs(math.sin(fase * velocidade_batida)) * 4)
    y_corpo = y + balanco
    x = int(x)

    # DESENHO 
    # Cabeça
    x_head, y_head = x - 28, y_corpo - 8
    scanline_fill_circle(tela, x_head, y_head, 9, CINZA_ESCURO)
    bresenham_circulo(tela, x_head, y_head, 9, PRETO)
    
    # Bico
    bico = [(x_head - 8, y_head), (x_head - 16, y_head + 2), (x_head - 8, y_head + 4)]
    scanline(tela, bico, LARANJA)
    desenhar_poligono(tela, bico, PRETO)
    setPixel(tela, int(x_head - 3), int(y_head - 2), BRANCO)

    # Asa de Trás
    asa_base_1 = [(x, y_corpo - 5), (x + 30, y_corpo - 40), (x + 15, y_corpo - 5)]
    ombro_1 = (x, y_corpo - 5)
    asa_1_rot = rotacionar(asa_base_1, angulo_asa + 10, ombro_1)
    scanline(tela, asa_1_rot, CINZA_CHUMBO)
    desenhar_poligono(tela, asa_1_rot, PRETO)

    # Corpo e Cauda
    cauda = [(x + 20, y_corpo), (x + 45, y_corpo - 10), (x + 20, y_corpo + 10)]
    scanline(tela, cauda, CINZA_CHUMBO)
    desenhar_poligono(tela, cauda, PRETO)
    scanline_fill_ellipse(tela, x, y_corpo, 25, 12, CINZA_ESCURO)
    bresenham_elipse(tela, x, y_corpo, 25, 12, PRETO)

    # Asa da Frente 
    asa_base_2 = [(x - 10, y_corpo), (x - 20, y_corpo - 45), (x + 10, y_corpo)]
    ombro_2 = (x - 5, y_corpo)
    asa_2_rot = rotacionar(asa_base_2, -angulo_asa, ombro_2)
    scanline(tela, asa_2_rot, CINZA_CLARO)
    desenhar_poligono(tela, asa_2_rot, PRETO)

# HITBOX 
def calcular_hitbox_pombo(x, y, fase):
    balanco = int(abs(math.sin(fase * 0.2)) * 4)
    y_corpo = y + balanco
    
    # O pombo é "comprido" mas "fino"
    hb_w = 70 # Do bico até o final do corpo
    hb_h = 22 # Fina o suficiente para o player tentar passar por baixo/cima
    hb_x = x - 38 # Começa no bico/cabeça
    hb_y = y_corpo - 15 # Centralizado no corpo
    
    return (hb_x, hb_y, hb_w, hb_h)

def processar_pombos(tela, lista):
    for p in lista[:]:
        p["x"] -= p["vel"]
        p["fase"] += 1
        
        # Calculamos a hitbox e guardamos no dicionário
        p["hitbox"] = calcular_hitbox_pombo(p["x"], p["y"], p["fase"])
        
        desenhar_pombo(tela, p["x"], p["y"], p["fase"])
        
        if p["x"] < -100:
            lista.remove(p)