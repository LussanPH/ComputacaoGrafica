import pygame
import sys
import funcoes
import telas
import jogador
import cachorro
import cenario
import pombo
from constantes import largura, altura, BRANCO, PRETO, AZUL, LARANJA

# --- INICIALIZAÇÃO ---
pygame.init()
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Djonga Run")
clock = pygame.time.Clock()

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


estado_atual = "MENU"
lista_pombos, lista_cachorros = resetar_jogo()
rodando = True

# --- LOOP PRINCIPAL ---
while rodando:
    
    if estado_atual == "GAME_OVER":
        
        # Chama a função de acordo com o estado, basicamente um nfa. Ela bloqueia o loop até retornar uma ação.
        acao = telas.tela_game_over(tela)
        
        if acao == "play":
            lista_pombos, lista_cachorros = resetar_jogo()
            estado_atual = "JOGANDO"
        elif acao == "menu":
            estado_atual = "MENU"

    elif estado_atual == "MENU":
        # Chama a tela de início
        telas.tela_start(tela)
        # Após sair da tela_start, vai para o jogo
        lista_pombos, lista_cachorros = resetar_jogo()
        estado_atual = "JOGANDO"

    elif estado_atual == "JOGANDO":
        dt = clock.tick(60) / 1000.0 

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_g:
                    estado_atual = "GAME_OVER"

        # --- LÓGICA DE DESENHO (O Jogo rodando normalmente) ---
        tela.fill(AZUL)

        cenario.atualizar(dt) 
        cenario.desenhar(tela)

        cachorro.processar_cachorros(tela, lista_cachorros)
        pombo.processar_pombos(tela, lista_pombos)
        
        jogador.desenhar_jogador(tela, 175, 225)

        pygame.display.flip()

# Finalização
pygame.quit()
sys.exit()