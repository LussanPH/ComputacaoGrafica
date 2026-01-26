import pygame
import sys
import funcoes
import telas
import jogador
import cachorro
import cenario
from constantes import largura, altura, AZUL
import pombo

# --- Inicialização da Lista de Obstáculos ---
lista_pombos = [
    {"x": 700, "y": 100, "fase": 0, "vel": 4},
    {"x": 900, "y": 150, "fase": 30, "vel": 2}
]

lista_cachorros = [
    {"x": 600, "y": 280, "fase": 0, "vel": 4}
]

pygame.init()
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Djonga Run")

telas.tela_start(tela)
clock = pygame.time.Clock()

rodando = True

while rodando:
    dt = clock.tick(60) / 1000.0 

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    
    tela.fill(AZUL)

    cenario.atualizar(dt) 
    cenario.desenhar(tela)

    cachorro.processar_cachorros(tela, lista_cachorros)
    pombo.processar_pombos(tela, lista_pombos)
    
    x_player, y_player = 175, 225
    jogador.desenhar_jogador(tela, x_player, y_player)
    jogador.desenhar_vida(tela,2)
    
    hb_p = (x_player - 30, y_player - 30, 60, 80) 

    pontos_p = [
        (hb_p[0], hb_p[1]),                      # Topo-Esquerdo
        (hb_p[0] + hb_p[2], hb_p[1]),             # Topo-Direito
        (hb_p[0] + hb_p[2], hb_p[1] + hb_p[3]),    # Baixo-Direito
        (hb_p[0], hb_p[1] + hb_p[3])              # Baixo-Esquerdo
    ]
    funcoes.desenhar_poligono(tela, pontos_p, (0, 255, 0))
    for cao in lista_cachorros:
        if "hitbox" in cao:
            if funcoes.intersecao(*hb_p, *cao["hitbox"]):
                print("HIT: Djonga vs Cachorro")
    pygame.display.flip()

pygame.quit()
sys.exit()