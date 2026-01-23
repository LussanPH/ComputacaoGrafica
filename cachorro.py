import math
import funcoes
import constantes

def desenhar_cachorro(tela, x, y, fase):
    # 1. PARÂMETROS DE ANIMAÇÃO
    velocidade_marcha = 0.2

    angulo_base = math.sin(fase * velocidade_marcha)
    amplitude_graus = 25 
    
    angulo_A = angulo_base * amplitude_graus
    angulo_B = math.sin(fase * velocidade_marcha + math.pi) * amplitude_graus
    
    # Balanço do corpo (Bobbing)
    balanco = int(abs(angulo_base) * 5)
    y_corpo = y - balanco
    x = int(x)

    # 2. PERNAS 
    def desenhar_perna_transformada(pivot_x, pivot_y, angulo):
        # Forma da perna em posição neutra
        largura_topo = 8
        largura_pata = 6
        h = 20
        ponto_pivo = (pivot_x, pivot_y)
        
        perna_base = [
            (pivot_x - largura_topo//2, pivot_y),
            (pivot_x + largura_topo//2, pivot_y),
            (pivot_x + largura_pata//2, pivot_y + h),
            (pivot_x - largura_pata//2, pivot_y + h)
        ]
        
        # Chamada da sua função de transformação
        perna_rot = funcoes.rotacionar(perna_base, angulo, ponto_pivo)
        
        funcoes.scanline(tela, perna_rot, constantes.CARAMELO)
        funcoes.desenhar_poligono(tela, perna_rot, constantes.PRETO)

    # Pernas de Trás (Camada de fundo)
    desenhar_perna_transformada(x - 10, y_corpo, angulo_A)
    desenhar_perna_transformada(x - 35, y_corpo, angulo_B)

    # RABO 
    pivo_rabo = (x + 10, y_corpo - 10)
    rabo_base = [pivo_rabo, (x + 10, y_corpo - 35), (x + 20, y_corpo - 5)]
    # ABANAR rabo 
    angulo_rabo = math.sin(fase * 0.3) * 30 
    
    rabo_rot = funcoes.rotacionar(rabo_base, angulo_rabo, pivo_rabo)
    funcoes.scanline(tela, rabo_rot, constantes.CARAMELO)
    funcoes.desenhar_poligono(tela, rabo_rot, constantes.PRETO)

    # CORPO
    funcoes.scanline_fill_ellipse(tela, x - 25, y_corpo - 12, 35, 15, constantes.CARAMELO)
    funcoes.bresenham_elipse(tela, x - 25, y_corpo - 12, 35, 15, constantes.PRETO)

    # CABEÇA E PESCOÇO
    y_head = y_corpo - 20
    pescoco = [(x - 55, y_head + 10), (x - 40, y_head + 15), (x - 50, y_head - 5), (x - 60, y_head - 5)]
    funcoes.scanline(tela, pescoco, constantes.CARAMELO)
    
    funcoes.scanline_fill_circle(tela, x - 60, y_head - 10, 14, constantes.CARAMELO)
    funcoes.bresenham_circulo(tela, x - 60, y_head - 10, 14, constantes.PRETO)
    funcoes.scanline_fill_ellipse(tela, x - 72, y_head - 8, 10, 6, constantes.CARAMELO)
    funcoes.bresenham_elipse(tela, x - 72, y_head - 8, 10, 6, constantes.PRETO)

    # PERNAS DA FRENTE
    desenhar_perna_transformada(x - 15, y_corpo, angulo_B)
    desenhar_perna_pendulo = desenhar_perna_transformada(x - 40, y_corpo, angulo_A)

    # DETALHES FACE
    funcoes.scanline_fill_circle(tela, x - 65, y_head - 13, 2, constantes.BRANCO)
    funcoes.scanline_fill_circle(tela, x - 80, y_head - 8, 3, constantes.PRETO)
    funcoes.bresenham_reta(tela, x - 78, x - 70, y_head - 3, y_head - 3, constantes.VERMELHO_ESCURO)

def processar_cachorros(tela, lista):
    for cao in lista[:]:
        cao["x"] -= cao["vel"]
        cao["fase"] += 1
        desenhar_cachorro(tela, int(cao["x"]), int(cao["y"]), cao["fase"])
        if cao["x"] < -100:
            lista.remove(cao)