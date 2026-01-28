import pygame
import sys
import jogo
import jogador
import modelo_fila_ru
import telas
import cenario
import funcoes
from constantes import *

pygame.init()
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Djonga Run")
clock = pygame.time.Clock()

#Textura dos rostos
textura_cientista = pygame.image.load("img/Cientista.png")
textura_lucas = pygame.image.load("img/Lucas.png")
textura_luna = pygame.image.load("img/Luna.png")
textura_icaro = pygame.image.load("img/Icaro.png")

estado_inicial = "MENU"
estado_dados = None 
velocidade_x_minimapa = 0.9


rodando = True
# --- MANTENHA OS IMPORTS ---

while rodando:
    # 1. EVENTOS GLOBAIS
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # --- 2. MÁQUINA DE ESTADOS ---
    if estado_inicial == "MENU":
        telas.tela_start(tela)
        # Resets
        cenario.resetar()              
        estado_dados = jogo.inicializar_estado() 
        clock.tick()                   
        estado_inicial = "JOGANDO"
        continue 

    elif estado_inicial == "GAME OVER":
        acao = telas.tela_game_over(tela)
        
        if acao == "play":
            cenario.resetar()         
            estado_dados = jogo.inicializar_estado()
            clock.tick()               
            estado_inicial = "JOGANDO"
            continue 
        elif acao == "menu":
            estado_inicial = "MENU"
            continue

    elif estado_inicial == "JOGANDO":
        # Agora o dt será sempre pequeno e correto
        dt = clock.tick(60) / 1000.0
        teclas = pygame.key.get_pressed()

        # PROCESSAMENTO
        tela.fill(AZUL)
        
        cenario.atualizar(dt)
        cenario.desenhar(tela)

        jogo.processar_logica(tela, estado_dados, dt, teclas)
        
        p = estado_dados["player"]
        if p["vidas"] < 0:
            estado_inicial = "GAME OVER"

        # --- DESENHOS ---
        jogador.desenhar_vida(tela, p["vidas"])
        protegido = p["inv_timer"] > 0

        if p["pulando"]:
            jogador.desenhar_pulo(tela, p["x"], p["y"], textura_cientista, p["velocidade"], protegido)
        else:
            jogador.desenhar_jogador(tela, p["x"], p["y"], textura_cientista, protegido)

        modelo_fila_ru.desenhar_modelo(tela, 250, 150, CINZA_CLARO, textura_icaro)# Função para desenhar personagem na fila do RU

        # 5. Desenho do minimapa com o jogador
        mover_minimapa = funcoes.viewport(tela, p["posicao_viewport_x"], p["posicao_viewport_y"])

        if mover_minimapa:
            p["posicao_viewport_x"] += velocidade_x_minimapa
        
        print(dt)

    pygame.display.flip()

pygame.quit()
sys.exit()