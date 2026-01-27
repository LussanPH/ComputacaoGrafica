import pygame
import colisoes
import cachorro
import pombo
import jogador
from constantes import *

# Constantes de Física
GRAVIDADE = 1
FORCA_PULO = -17
Y_CHAO = 225

def inicializar_estado():
    """Cria o dicionário inicial com toda a 'alma' do jogo."""
    pombos, cachorros = resetar_jogo()
    return {
        "player": {
            "x": 175,
            "y": Y_CHAO,
            "pulando": False,
            "velocidade": 0,
            "vidas": 2, # Coração 0, 1 e 2
            "inv_timer": 0,
            "posicao_viewport_x": 10,
            "posicao_viewport_y": 357
        },
        "obstaculos": {
            "pombos": pombos,
            "cachorros": cachorros
        },
        "status": "JOGANDO"
    }

def processar_logica(tela, estado, dt, teclas):
    """Executa a matemática e as colisões. Retorna True se houve um hit."""
    p = estado["player"]
    obs = estado["obstaculos"]

    # 1. Pulo (Entrada e Física)
    if teclas[pygame.K_w] and not p["pulando"]:
        p["pulando"] = True
        p["velocidade"] = FORCA_PULO
    
    if p["pulando"]:
        p["velocidade"] += GRAVIDADE
        p["y"] += p["velocidade"]
        if p["y"] >= Y_CHAO:
            p["y"] = Y_CHAO
            p["pulando"] = False
            p["velocidade"] = 0

    # 2. Timers (Invencibilidade)
    if p["inv_timer"] > 0:
        p["inv_timer"] -= dt

    # 3. Movimentação dos Inimigos
    cachorro.processar_cachorros(tela, obs["cachorros"])
    pombo.processar_pombos(tela, obs["pombos"])

    # 4. Colisões
    if p["inv_timer"] <= 0:
        hb_djonga = jogador.calcular_hitbox_jogador(p["x"], p["y"])
        if colisoes.verificar_colisoes_gerais(hb_djonga, obs["cachorros"], obs["pombos"]):
            p["vidas"] -= 1
            p["inv_timer"] = 0.8 # 0.8 segundos de folga
            return True
    return False

def resetar_jogo():
    pombos = [
        {"x": 700, "y": 100, "fase": 0, "vel": 10},
        {"x": 900, "y": 150, "fase": 30, "vel": 10}
    ]
    cachorros = [
        {"x": 600, "y": 280, "fase": 0, "vel": 10},
        {"x": 800, "y": 280, "fase": 0, "vel": 10},
        {"x": 860, "y": 280, "fase": 0, "vel": 10}
    ]
    return pombos, cachorros