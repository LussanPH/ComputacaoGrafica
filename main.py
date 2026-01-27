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

# Ativos
textura = pygame.image.load("Cientista.png")
estado_inicial = "MENU"
estado_dados = None # O dicionário do jogo.py

rodando = True
while rodando:
    # --- MÁQUINA DE ESTADOS ---
    if estado_inicial == "MENU":
        telas.tela_start(tela)
        estado_dados = jogo.inicializar_estado() # Começa tudo do zero
        estado_inicial = "JOGANDO"
    
    elif estado_inicial == "GAME OVER":
        acao = telas.tela_game_over(tela)
        if acao == "play":
            estado_dados = jogo.inicializar_estado()
            estado_inicial = "JOGANDO"
        elif acao == "menu":
            estado_inicial = "MENU"

    elif estado_inicial == "JOGANDO":
        dt = clock.tick(60) / 1000.0
        teclas = pygame.key.get_pressed()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: rodando = False

        # 1. Desenho de Fundo
        tela.fill(AZUL)
        cenario.atualizar(dt)
        cenario.desenhar(tela)
        funcoes.viewport(tela)

        # 2. Lógica delegada ao jogo.py
        houve_hit = jogo.processar_logica(tela, estado_dados, dt, teclas)
        
        # 3. Verificação de Derrota
        p = estado_dados["player"]
        if p["vidas"] < 0:
            estado_inicial = "GAME OVER"

        # 4. Desenho da Interface e Jogador
        jogador.desenhar_vida(tela, p["vidas"])
        protegido = p["inv_timer"] > 0

        if p["pulando"]:
            jogador.desenhar_pulo(tela, p["x"], p["y"], textura, p["velocidade"], protegido)
        else:
            jogador.desenhar_jogador(tela, p["x"], p["y"], textura, protegido)

    pygame.display.flip()

pygame.quit()
sys.exit()