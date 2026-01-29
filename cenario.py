import pygame
import funcoes
from constantes import *
from modelo_fila_ru import desenhar_modelo

# ---------- ESTADO DO CENÁRIO ----------
scroll_x = 0.0
velocidade_movimento = 150
final_atingido = False
ultimo_tempo = pygame.time.get_ticks()

textura_lucas = pygame.image.load("img/Lucas.png")
textura_luna = pygame.image.load("img/Luna.png")
textura_icaro = pygame.image.load("img/Icaro.png")

# RU
x_ru_inicial = 3300
largura_ru = 450
limite_scroll = (x_ru_inicial + largura_ru) - largura

# Limites de recorte
xmin, ymin, xmax, ymax = 0, 0, largura - 1, altura - 1


# Função para garantir o recorte e o movimento
def desenhar_objeto_movel(tela, pontos, tx, cor, preencher=True):
    # Aplicação do culling para verificar se os pontos estão dentro da tela antes de transladar
    xs_originais = [p[0] for p in pontos]
    x_min_na_tela = min(xs_originais) + tx
    x_max_na_tela = max(xs_originais) + tx

    if x_max_na_tela < 0 or x_min_na_tela > largura:
        return

    #Translada se visível
    pontos_movidos = funcoes.transladar_pontos(pontos, tx, 0)

    # Recorte
    pontos_recortados = funcoes.sutherland_hodgman(
        pontos_movidos, xmin, ymin, xmax, ymax
    )

    if len(pontos_recortados) > 2:
        if preencher:
            funcoes.scanline(tela, pontos_recortados, cor)
        funcoes.desenhar_poligono(tela, pontos_recortados, PRETO)


# Busca melhorar a animação
def atualizar(dt):
    global scroll_x, final_atingido

    if not final_atingido:
        scroll_x += velocidade_movimento * dt
        
        if scroll_x >= limite_scroll:
            scroll_x = limite_scroll
            final_atingido = True

# A função de desenhar tem como função desenhar        
def desenhar(tela):
    altura_chao = altura - altura // 4
    
    x_fim_mundo_tela = (x_ru_inicial + largura_ru) - scroll_x

    # Só desenhamos se o chão ainda não terminou de passar pela tela
    if x_fim_mundo_tela > 0:
        x_inicio_visivel = 0 
        x_fim_visivel = min(largura, x_fim_mundo_tela)
        
        chao_pts = [
            (x_inicio_visivel, altura_chao), 
            (x_fim_visivel, altura_chao), 
            (x_fim_visivel, altura), 
            (x_inicio_visivel, altura)
        ]
        desenhar_objeto_movel(tela, chao_pts, 0, CINZA)

    # --- DESENHO DAS COLUNAS ---
    # Margem serve para  suavizar o surgimento das colunas
    margem = 50 

    for i in range(1, 12):
        x_base_mundo = i * 250
        x_visual = x_base_mundo - scroll_x  

        # SÓ desenha se estiver dentro dos limites da tela (-margem até largura+margem)
        if -margem < x_visual < largura + margem:
            coluna = [(x_base_mundo-20, 0), (x_base_mundo+20, 0), 
                      (x_base_mundo+20, altura_chao), (x_base_mundo-20, altura_chao)]
            base = [(x_base_mundo-30, altura_chao-17), (x_base_mundo+30, altura_chao-17), 
                    (x_base_mundo+30, altura_chao), (x_base_mundo-30, altura_chao)]
            
            desenhar_objeto_movel(tela, coluna, -scroll_x, CINZA)
            desenhar_objeto_movel(tela, base, -scroll_x, CINZA_ESCURO)

    # --- DESENHO DO RU ---
    # Verifica se o bloco do RU está visível
    x_ru_visual_inicio = x_ru_inicial - scroll_x
    x_ru_visual_fim = (x_ru_inicial + largura_ru) - scroll_x

    # Verifica se o ru está dentro da largura da tela antes dele ser carregado
    if x_ru_visual_inicio < largura:
        
        # Corpo do RU
        corpo_ru = [(x_ru_inicial, 0), (x_ru_inicial + largura_ru, 0), 
                    (x_ru_inicial + largura_ru, altura_chao), (x_ru_inicial, altura_chao)]
        desenhar_objeto_movel(tela, corpo_ru, -scroll_x, BEGE)

        x_coluna_teto = x_ru_inicial - 80
        # Pequena verificação extra pois essa coluna está fora do corpo principal do RU
        if (x_coluna_teto - scroll_x) > -margem: 
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
            # Como as telhas são pequenas, confiar no check principal do RU é segur
            teto_pts = [(x_inicio_telha, y_t), (x_ru_inicial, y_t), 
                        (x_ru_inicial, y_t-20), (x_inicio_telha, y_t-20)]
            desenhar_objeto_movel(tela, teto_pts, -scroll_x, TELHA)
        pos_x_vitoria = x_ru_inicial - scroll_x -200
        if -200 < pos_x_vitoria < largura + 200:
            fonte_vitoria = pygame.font.SysFont(None, 80, bold=True)
            msg = "HOJE TEM LASANHA!"
            sombra = fonte_vitoria.render(msg, True, PRETO)
            texto = fonte_vitoria.render(msg, True, LARANJA)

            tela.blit(sombra, (pos_x_vitoria - 247, 43)) 
            tela.blit(texto, (pos_x_vitoria - 250, 40))
        y_modelos = altura_chao - 70
        distancia_entre_fila = 80
        
        x_icaro_mundo = x_ru_inicial - 120
        x_luna_mundo = x_icaro_mundo - distancia_entre_fila
        x_lucas_mundo = x_luna_mundo - distancia_entre_fila

        desenhar_modelo(tela, x_icaro_mundo - scroll_x, y_modelos, VERMELHO, textura_icaro)
    
        desenhar_modelo(tela, x_luna_mundo - scroll_x, y_modelos, VERDE, textura_luna)
        
        desenhar_modelo(tela, x_lucas_mundo - scroll_x, y_modelos, ROSA, textura_lucas)

        # Texto
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
        
        funcoes.scanline(tela, coluna, CINZA)
        funcoes.desenhar_poligono(tela, coluna, PRETO)
        funcoes.scanline(tela, base, CINZA_ESCURO)
        funcoes.desenhar_poligono(tela, base, PRETO)
        
def desenhar_game_over(tela):
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

        linha_sombra = [
            (x_centro + largura_coluna // 4, 0),
            (x_centro + largura_coluna // 4, y_topo - altura_base_capital)
        ]
        base = [
            (x_centro - (largura_coluna // 2 + 10), y_topo - altura_base_capital),
            (x_centro + (largura_coluna // 2 + 10), y_topo - altura_base_capital),
            (x_centro + (largura_coluna // 2 + 10), y_topo),
            (x_centro - (largura_coluna // 2 + 10), y_topo)
        ]
        funcoes.desenhar_poligono(tela, linha_sombra, CINZA_ESCURO)
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
    largura_coluna = 20

    coluna_teto = [
        (espacamento - largura_coluna // 2, y_topo_teto),
        (espacamento + largura_coluna // 2, y_topo_teto),
        (espacamento + largura_coluna // 2, y_topo),
        (espacamento - largura_coluna // 2, y_topo)
    ]
    funcoes.desenhar_poligono(tela, coluna_teto, CINZA)
    funcoes.scanline(tela, coluna_teto, CINZA)

    base_teto = [
        (espacamento - (largura_coluna // 2 + 10), y_topo - altura_base_capital),
        (espacamento + (largura_coluna // 2 + 10), y_topo - altura_base_capital),
        (espacamento + (largura_coluna // 2 + 10), y_topo),
        (espacamento - (largura_coluna // 2 + 10), y_topo)
    ]
    funcoes.desenhar_poligono(tela, base_teto, CINZA_ESCURO)
    funcoes.scanline(tela, base_teto, CINZA_ESCURO)

    y_modelo = y_topo - 80
    
    x_inicial = largura_ru - 60 
    distancia_entre_eles = 100

    desenhar_modelo(tela, x_inicial, y_modelo, VERMELHO, textura_icaro)

    desenhar_modelo(tela, x_inicial - distancia_entre_eles, y_modelo, VERDE, textura_luna)
    
    desenhar_modelo(tela, x_inicial - (distancia_entre_eles * 2), y_modelo, ROSA, textura_lucas)

    #Texto RU
    font_size = max(12, int((y_topo) * 0.25))  
    font = pygame.font.SysFont(None, font_size, bold=True)
    text_surf = font.render("RU", True, PRETO)
    center_x = (largura_ru + (largura - 1)) // 2
    center_y = y_topo // 2
    text_rect = text_surf.get_rect(center=(center_x, center_y))
    tela.blit(text_surf, text_rect)

def resetar():
    global scroll_x, final_atingido
    scroll_x = 0.0
    final_atingido = False