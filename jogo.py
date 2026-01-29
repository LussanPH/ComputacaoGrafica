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
            "x": 125,
            "y": Y_CHAO,
            "pulando": False,
            "distancia_chao": 0,
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
        if p["velocidade"] < 0:
            p["distancia_chao"] -= p["velocidade"] + 0.8
        else:
             p["distancia_chao"] -= p["velocidade"] - 0.8
        p["y"] += p["velocidade"]
        if p["y"] >= Y_CHAO:
            p["y"] = Y_CHAO
            p["pulando"] = False
            p["distancia_chao"] = 0
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
            p["inv_timer"] = 2 # 2 segundos de folga
            return True
    return False

def resetar_jogo():
    """Distribuição estratégica de obstáculos para uma corrida de 3000px"""
    
    # POMBOS: Desafios aéreos (fase e y variados para confundir o pulo)
    pombos = [
        {"x": 800,  "y": 140, "fase": 0,  "vel": 7},   # Primeiro susto
        {"x": 1600, "y": 120, "fase": 20, "vel": 8},   # Mais alto, exige pulo preciso
        {"x": 2300, "y": 220, "fase": 15, "vel": 8},   # Rápido e baixo (perigoso!)
        {"x": 2950, "y": 200, "fase": 40, "vel": 12}  # O "Pombo do Mal" na porta do RU
    ]

    # CACHORROS: Obstáculos terrestres (ritmo de pulo)
    cachorros = [
        {"x": 500,  "y": 280, "fase": 0, "vel": 6},   # Tutorial: Pulo simples
        {"x": 1100, "y": 280, "fase": 0, "vel": 7},   # Ritmo constante
        {"x": 1300, "y": 280, "fase": 0, "vel": 8},   # Combo: dois cachorros próximos!
        {"x": 2000, "y": 280, "fase": 0, "vel": 9},  # Velocidade alta
        {"x": 2850, "y": 280, "fase": 0, "vel": 11}   # Sprint final
    ]

    return pombos, cachorros
