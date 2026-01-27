import pygame
import sys
import funcoes
import jogo
import telas
import jogador
import cachorro
import cenario
from constantes import largura, altura, AZUL
import pombo

# --- Inicialização da Lista de Obstáculos ---

lista_pombos,lista_cachorros= jogo.resetar_jogo()

pygame.init()
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Djonga Run")

textura = pygame.image.load("Cientista.png")

clock = pygame.time.Clock()

rodando = True

gravidade = 1
forca_pulo = -17
estado_player = {
"x": 175,
"y": 225,
"pulando": False,
"velocidade": 0
}
estado_inicial = "MENU"

while rodando:
    if estado_inicial == "MENU":
        telas.tela_start(tela)
        lista_pombos,lista_cachorros= jogo.resetar_jogo()
        estado_inicial="JOGANDO"
    
    elif estado_inicial == "GAME OVER":
        acao= telas.tela_game_over(tela)
        
        if acao == "play":
            lista_pombos,lista_cachorros= jogo.resetar_jogo()
            estado_inicial="JOGANDO"
        elif acao == "menu":
             estado_inicial= "MENU"
    elif estado_inicial == "JOGANDO":    
        teclas = pygame.key.get_pressed()

        dt = clock.tick(60) / 1000.0 

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
        
        tela.fill(AZUL)

        cenario.atualizar(dt) 
        cenario.desenhar(tela)

        funcoes.viewport(tela)

        cachorro.processar_cachorros(tela, lista_cachorros)
        pombo.processar_pombos(tela, lista_pombos)


        if teclas[pygame.K_w]:
           jogo.iniciar_pulo(estado_player)

        jogo.atualizar_pulo(estado_player)
        
        if estado_player["pulando"]:
            jogador.desenhar_pulo(
                tela,
                estado_player["x"],
                estado_player["y"],
                textura,
                estado_player["velocidade"]
            )
        else:
            jogador.desenhar_jogador(
                tela,
                estado_player["x"],
                estado_player["y"],
                textura
            )

        jogador.desenhar_vida(tela,2)
        
        hb_p = (
        estado_player["x"] - 30,
        estado_player["y"] - 30,
        60,
        80
        )
        pontos_p = [
            (hb_p[0], hb_p[1]),                      # Topo-Esquerdo
            (hb_p[0] + hb_p[2], hb_p[1]),             # Topo-Direito
            (hb_p[0] + hb_p[2], hb_p[1] + hb_p[3]),    # Baixo-Direito
            (hb_p[0], hb_p[1] + hb_p[3])              # Baixo-Esquerdo
        ]
        funcoes.desenhar_poligono(tela, pontos_p, (0, 255, 0))
        pygame.display.flip()

pygame.quit()
sys.exit()