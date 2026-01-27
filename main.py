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
<<<<<<< HEAD
estado_dados = None 
=======
estado_dados = None # O dicionário do jogo.py
velocidade_x_minimapa = 3
>>>>>>> 3067dc3 (Added viewport)

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
            jogador.desenhar_pulo(tela, p["x"], p["y"], textura, p["velocidade"], protegido)
        else:
            jogador.desenhar_jogador(tela, p["x"], p["y"], textura, protegido)

        # 5. Desenho do minimapa com o jogador
        mover_minimapa = funcoes.viewport(tela, p["posicao_viewport_x"], p["posicao_viewport_y"])

        if mover_minimapa:
            p["posicao_viewport_x"] += velocidade_x_minimapa

    pygame.display.flip()

pygame.quit()
sys.exit()