import pygame
import funcoes
from constantes import *
import cenario
import sys
import pygame
import funcoes

def tela_start(tela):
    menu_ativo = True
    clock = pygame.time.Clock()

    # Fundo preto (tela inteira) usando scanline
    fundo = [
        (0, 0),
        (largura, 0),
        (largura, altura),
        (0, altura)
    ]

    # Botão azul centralizado 
    botao_largura = 450
    botao_altura = 90
    bx = largura // 2 - botao_largura // 2
    by = altura // 2

    pontos_botao = [
        (bx, by),
        (bx + botao_largura, by),
        (bx + botao_largura, by + botao_altura),
        (bx, by + botao_altura)
    ]

    fonte_titulo = pygame.font.SysFont("Arial", 80, bold=True)
    fonte_instrucao = pygame.font.SysFont("Arial", 30)

    surf_titulo = fonte_titulo.render("DJONGA RUN", True, LARANJA)
    surf_instrucao = fonte_instrucao.render("Pressione ESPAÇO para Correr", True, BRANCO)

    while menu_ativo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    menu_ativo = False

        # Fundo preto com scanline
        funcoes.scanline(tela, fundo, AZUL)
        cenario.desenhar_start(tela)

        # Título acima do botão
        titulo_x = largura // 2 - surf_titulo.get_width() // 2
        titulo_y = by - surf_titulo.get_height() - 25
        surf_outline = fonte_titulo.render("DJONGA RUN", True, PRETO)

        offsets = [(-2,0), (2,0), (0,-2), (0,2), (-2,-2), (2,2), (-2,2), (2,-2)]

        for ox, oy in offsets:
            tela.blit(surf_outline, (titulo_x + ox, titulo_y + oy))

        tela.blit(surf_titulo, (titulo_x, titulo_y))
        funcoes.desenhar_poligono(tela, pontos_botao, BRANCO)
        funcoes.scanline(tela, pontos_botao, LARANJA)
        tela.blit(
            surf_instrucao,
            (
                largura // 2 - surf_instrucao.get_width() // 2,
                by + botao_altura // 2 - surf_instrucao.get_height() // 2
            )
        )

        pygame.display.flip()
        clock.tick(30)