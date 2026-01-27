import pygame
import funcoes
from constantes import *
import jogador

GRAVIDADE = 1
FORCA_PULO = -17
Y_CHAO = 225


def iniciar_pulo(estado):
    if not estado["pulando"]:
        estado["pulando"] = True
        estado["velocidade"] = FORCA_PULO


def atualizar_pulo(estado):
    if estado["pulando"]:
        estado["velocidade"] += GRAVIDADE
        estado["y"] += estado["velocidade"]

    if estado["y"] >= Y_CHAO:
        estado["y"] = Y_CHAO
        estado["pulando"] = False
        estado["velocidade"] = 0

def resetar_jogo():
    """Função para resetar as posições dos elementos ao reiniciar o jogo"""
    #Não testei sem, mas pelo que eu pesquisei parece ser recomendada
    pombos = [
        {"x": 700, "y": 100, "fase": 0, "vel": 4},
        {"x": 900, "y": 150, "fase": 30, "vel": 2}
    ]
    cachorros = [
        {"x": 600, "y": 280, "fase": 0, "vel": 3}
    ]
    return pombos, cachorros