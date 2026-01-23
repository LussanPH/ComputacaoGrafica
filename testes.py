import pygame
import sys
import funcoes
from constantes import *

# Configurações iniciais
pygame.init()
tela = pygame.display.set_mode((largura, altura))
clock = pygame.time.Clock()

scroll_x = 0.0
# Velocidade em pixels por segundo (independente do FPS)
velocidade_movimento = 200
final_atingido = False

# Limites para o recorte
xmin, ymin, xmax, ymax = 0, 0, largura - 1, altura - 1

def desenhar_objeto_movel(tela, pontos, tx, cor, preencher=True):
    # 1. Transladar
    pontos_movidos = funcoes.transladar_pontos(pontos, tx, 0)
    
    # 2. Culling (Ignora se estiver fora da tela)
    xs = [p[0] for p in pontos_movidos]
    if min(xs) > largura or max(xs) < 0:
        return

    pontos_recortados = funcoes.sutherland_hodgman(pontos_movidos, xmin, ymin, xmax, ymax)
    
    if len(pontos_recortados) > 2:
        if preencher:
            funcoes.scanline(tela, pontos_recortados, cor)
        funcoes.desenhar_poligono(tela, pontos_recortados, PRETO)

ultimo_tempo = pygame.time.get_ticks()

# --- CONFIGURAÇÃO DO MAPA ---
# RU posicionado mais longe para dar espaço às colunas
x_ru_inicial = 3000 
largura_ru = 450
# O mapa para quando a borda direita do RU estiver visível no lado esquerdo da tela
limite_scroll = (x_ru_inicial + largura_ru) - largura

while True:
    # 1. Delta Time para fluidez
    agora = pygame.time.get_ticks()
    dt = (agora - ultimo_tempo) / 1000.0
    ultimo_tempo = agora

    # 2. Lógica de Parada
    if not final_atingido:
        scroll_x += velocidade_movimento * dt
        if scroll_x >= limite_scroll:
            scroll_x = limite_scroll
            final_atingido = True

    tela.fill(AZUL)
    altura_chao= altura-altura/3
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

    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(60)