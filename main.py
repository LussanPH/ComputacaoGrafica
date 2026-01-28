import pygame
import sys
import jogo
import jogador
import telas
import cenario
import funcoes
from constantes import largura, altura, AZUL

pygame.init()
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Djonga Run")
clock = pygame.time.Clock()

textura = pygame.image.load("Cientista.png")
estado_inicial = "MENU"
estado_dados = None 
velocidade_x_minimapa = 0.8


rodando = True
# --- MANTENHA OS IMPORTS ---

while rodando:
    # 1. EVENTOS GLOBAIS
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    pixel_array = pygame.PixelArray(tela)

    # --- 2. MÁQUINA DE ESTADOS ---
    if estado_inicial == "MENU":
        telas.tela_start(tela,pixel_array)
        # Resets
        cenario.resetar()              
        estado_dados = jogo.inicializar_estado() 
        clock.tick()                   
        estado_inicial = "JOGANDO"
        continue 

    elif estado_inicial == "GAME OVER":
        acao = telas.tela_game_over(tela,pixel_array)
        
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
        dt = clock.tick(60) / 1000.0
        teclas = pygame.key.get_pressed()

        tela.fill(AZUL)


        cenario.atualizar(dt)
        cenario.desenhar(tela,pixel_array)

        jogo.processar_logica(pixel_array, estado_dados, dt, teclas)

        p = estado_dados["player"]
        if p["vidas"] < 0:
            estado_inicial = "GAME OVER"

        jogador.desenhar_vida(tela,pixel_array, p["vidas"])

        protegido = p["inv_timer"] > 0
        if p["pulando"]:
            jogador.desenhar_pulo(pixel_array, p["x"], p["y"], textura, p["velocidade"], protegido)
        else:
            jogador.desenhar_jogador(pixel_array, p["x"], p["y"], textura, protegido)

        mover_minimapa = funcoes.viewport(
            pixel_array, p["posicao_viewport_x"], p["posicao_viewport_y"]
        )
        if mover_minimapa:
            p["posicao_viewport_x"] += velocidade_x_minimapa
        del pixel_array

        pygame.display.flip()

pygame.quit()
sys.exit()