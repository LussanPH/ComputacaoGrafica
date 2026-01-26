import math
import funcoes
import constantes

def desenhar_cachorro(tela, x, y, fase, mostrar_hitbox=False):
    # LÓGICA DE ANIMAÇÃO
    velocidade_marcha = 0.2
    angulo_base = math.sin(fase * velocidade_marcha)
    amplitude_graus = 25 
    angulo_A = angulo_base * amplitude_graus
    angulo_B = math.sin(fase * velocidade_marcha + math.pi) * amplitude_graus
    
    balanco = int(abs(angulo_base) * 5)
    y_corpo = y - balanco
    x = int(x)

    # DESENHO DAS PARTES 
    # Pernas de Trás
    desenhar_perna_helper(tela, x - 10, y_corpo, angulo_A)
    desenhar_perna_helper(tela, x - 35, y_corpo, angulo_B)

    # Rabo
    pivo_rabo = (x + 10, y_corpo - 10)
    rabo_base = [pivo_rabo, (x + 10, y_corpo - 35), (x + 20, y_corpo - 5)]
    rabo_rot = funcoes.rotacionar(rabo_base, math.sin(fase * 0.3) * 30, pivo_rabo)
    funcoes.scanline(tela, rabo_rot, constantes.CARAMELO)
    funcoes.desenhar_poligono(tela, rabo_rot, constantes.PRETO)

    # Corpo
    funcoes.scanline_fill_ellipse(tela, x - 25, y_corpo - 12, 35, 15, constantes.CARAMELO)
    funcoes.bresenham_elipse(tela, x - 25, y_corpo - 12, 35, 15, constantes.PRETO)

    # Cabeça e Pescoço
    y_head = y_corpo - 20
    pescoco = [(x - 55, y_head + 10), (x - 40, y_head + 15), (x - 50, y_head - 5), (x - 60, y_head - 5)]
    funcoes.scanline(tela, pescoco, constantes.CARAMELO)
    funcoes.scanline_fill_circle(tela, x - 60, y_head - 10, 14, constantes.CARAMELO)
    funcoes.bresenham_circulo(tela, x - 60, y_head - 10, 14, constantes.PRETO)
    funcoes.scanline_fill_ellipse(tela, x - 72, y_head - 8, 10, 6, constantes.CARAMELO)
    funcoes.bresenham_elipse(tela, x - 72, y_head - 8, 10, 6, constantes.PRETO)

    # Pernas da Frente
    desenhar_perna_helper(tela, x - 15, y_corpo, angulo_B)
    desenhar_perna_helper(tela, x - 40, y_corpo, angulo_A)

    # Detalhes Face
    funcoes.scanline_fill_circle(tela, x - 65, y_head - 13, 2, constantes.BRANCO)
    funcoes.scanline_fill_circle(tela, x - 80, y_head - 8, 3, constantes.PRETO)
    funcoes.bresenham_reta(tela, x - 78, x - 70, y_head - 3, y_head - 3, constantes.VERMELHO_ESCURO)

    # DEBUG: HITBOX 
    if mostrar_hitbox:
        hb = calcular_hitbox_cachorro(x, y, fase)
        funcoes.desenhar_poligono(tela, [
            (hb[0], hb[1]), (hb[0]+hb[2], hb[1]), 
            (hb[0]+hb[2], hb[1]+hb[3]), (hb[0], hb[1]+hb[3])
        ], (255, 0, 0)) # Caixa Vermelha

def desenhar_perna_helper(tela, px, py, ang):
    pivo = (px, py)
    base = [(px-4, py), (px+4, py), (px+3, py+20), (px-3, py+20)]
    rot = funcoes.rotacionar(base, ang, pivo)
    funcoes.scanline(tela, rot, constantes.CARAMELO)
    funcoes.desenhar_poligono(tela, rot, constantes.PRETO)

# HitBox
def calcular_hitbox_cachorro(x, y, fase):
    balanco = int(abs(math.sin(fase * 0.2)) * 5)
    y_corpo = y - balanco

    # A hitbox será um pouco menor para ser justa:
    hb_w = 78
    hb_h = 28 # Menor que a altura total para o player poder pular por cima
    hb_x = x - 70 # Começa perto do focinho
    hb_y = y_corpo - 35 # Focado na parte de cima (dorso e cabeça)
    
    return (hb_x, hb_y, hb_w, hb_h)

def processar_cachorros(tela, lista):
    for cao in lista[:]:
        cao["x"] -= cao["vel"]
        cao["fase"] += 1
        # Otimização: Guardamos a hitbox no dicionário para a Main ler sem recalcular
        cao["hitbox"] = calcular_hitbox_cachorro(cao["x"], cao["y"], cao["fase"])
        
        desenhar_cachorro(tela, int(cao["x"]), int(cao["y"]), cao["fase"])
        
        if cao["x"] < -150:
            lista.remove(cao)