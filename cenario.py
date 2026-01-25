import pygame
import funcoes
from constantes import *

# ---------- ESTADO DO CENÁRIO ----------
scroll_x = 0.0
velocidade_movimento = 200
final_atingido = False
ultimo_tempo = pygame.time.get_ticks()

# RU
x_ru_inicial = 3000
largura_ru = 450
limite_scroll = (x_ru_inicial + largura_ru) - largura

# Limites de recorte
xmin, ymin, xmax, ymax = 0, 0, largura - 1, altura - 1


# ---------- FUNÇÕES AUXILIARES ----------
def desenhar_objeto_movel(tela, pontos, tx, cor, preencher=True):
    pontos_movidos = funcoes.transladar_pontos(pontos, tx, 0)

    xs = [p[0] for p in pontos_movidos]
    if min(xs) > largura or max(xs) < 0:
        return

    pontos_recortados = funcoes.sutherland_hodgman(
        pontos_movidos, xmin, ymin, xmax, ymax
    )

    if len(pontos_recortados) > 2:
        if preencher:
            funcoes.scanline(tela, pontos_recortados, cor)
        funcoes.desenhar_poligono(tela, pontos_recortados, PRETO)


# ---------- UPDATE ----------(Busca melhorar a animação)
def atualizar(dt):
    global scroll_x, final_atingido

    if not final_atingido:
        scroll_x += velocidade_movimento * dt
        
        if scroll_x >= limite_scroll:
            scroll_x = limite_scroll
            final_atingido = True
# A função de desenhar tem como função desenhar        
def desenhar(tela):
    altura_chao= altura-altura//4
    # --- DESENHO DO CHÃO ---
    chao_pts = [(0, altura_chao), (x_ru_inicial + largura_ru, altura_chao), (x_ru_inicial + largura_ru, altura), (0, altura)]
    desenhar_objeto_movel(tela, chao_pts, -scroll_x, CINZA)

    # --- DESENHO DAS COLUNAS---
    for i in range(1, 12):
        x_base = i * 250  # Mais próximas uma da outra
        coluna = [(x_base-20, 0), (x_base+20, 0), (x_base+20, altura_chao), (x_base-20, altura_chao)]
        base = [(x_base-30, altura_chao-17), (x_base+30, altura_chao-17), (x_base+30, altura_chao), (x_base-30, altura_chao)]
        
        desenhar_objeto_movel(tela, coluna, -scroll_x, CINZA)
        desenhar_objeto_movel(tela, base, -scroll_x, CINZA_ESCURO)

    # --- DESENHO DO RU (Cenário Final) ---
    # Corpo do RU (Bege)
    corpo_ru = [(x_ru_inicial, 0), (x_ru_inicial + largura_ru, 0), 
                (x_ru_inicial + largura_ru, altura_chao), (x_ru_inicial, altura_chao)]
    desenhar_objeto_movel(tela, corpo_ru, -scroll_x, BEGE)

    # Coluna de sustentação embaixo das telhas
    x_coluna_teto = x_ru_inicial - 80
    coluna_sustentacao = [(x_coluna_teto-10, 100), (x_coluna_teto+10, 100), 
                          (x_coluna_teto+10, altura_chao), (x_coluna_teto-10, altura_chao)]
    sustentacao_base = [(x_coluna_teto-15, altura_chao-10), (x_coluna_teto+15, altura_chao-10), 
                          (x_coluna_teto+15, altura_chao), (x_coluna_teto-15, altura_chao)]
    desenhar_objeto_movel(tela, coluna_sustentacao, -scroll_x, CINZA)
    desenhar_objeto_movel(tela, sustentacao_base, -scroll_x, CINZA_ESCURO)

    # Telhado 
    for i in range(3):
        y_t = 100 - (i * 20)
        x_inicio_telha = x_ru_inicial - 150 + (i * 30)
        teto_pts = [(x_inicio_telha, y_t), (x_ru_inicial, y_t), 
                    (x_ru_inicial, y_t-20), (x_inicio_telha, y_t-20)]
        desenhar_objeto_movel(tela, teto_pts, -scroll_x, TELHA)

    # --- TEXTO RU ---
    pos_x_texto = (x_ru_inicial + (largura_ru // 2)) - scroll_x
    if -50 < pos_x_texto < largura + 50:
        font = pygame.font.SysFont(None, 60, bold=True)
        text_surf = font.render("RU", True, PRETO)
        tela.blit(text_surf, (pos_x_texto - 30, 120))
        
def desenhar_start(tela):
    altura_chao= altura-altura//4
    # --- DESENHO DO CHÃO ---
    chao_pts = [(0, altura_chao), (x_ru_inicial + largura_ru, altura_chao), (x_ru_inicial + largura_ru, altura), (0, altura)]
    funcoes.desenhar_poligono(tela, chao_pts, CINZA)
    funcoes.scanline(tela, chao_pts, CINZA)

    # --- DESENHO DAS COLUNAS---
    espacamento= largura//4
    for i in range(1, 4):
        x_base = i * espacamento  # Mais próximas uma da outra
        coluna = [(x_base-20, 0), (x_base+20, 0), (x_base+20, altura_chao), (x_base-20, altura_chao)]
        base = [(x_base-30, altura_chao-17), (x_base+30, altura_chao-17), (x_base+30, altura_chao), (x_base-30, altura_chao)]
        
        desenhar_objeto_movel(tela, coluna, -scroll_x, CINZA)
        desenhar_objeto_movel(tela, base, -scroll_x, CINZA_ESCURO)