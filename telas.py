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

    fundo = [
        (0, 0),
        (largura, 0),
        (largura, altura),
        (0, altura)
    ]
    cores_poligono = [
       AZUL,
       AZUL,
       LARANJA,
       LARANJA
    ]

    # Botão centralizado 
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

    surf_titulo = fonte_titulo.render("DJONGA R.UN", True, LARANJA)
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
        funcoes.scanline_fill_gradiente(tela, fundo, cores_poligono)
        cenario.desenhar_start(tela)

        # Título acima do botão
        titulo_x = largura // 2 - surf_titulo.get_width() // 2
        titulo_y = by - surf_titulo.get_height() - 25
        surf_outline = fonte_titulo.render("DJONGA R.UN", True, PRETO)

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
        
def tela_game_over(tela):
    menu_ativo = True
    clock = pygame.time.Clock()

    # Fundo usando scanline
    fundo = [
        (0, 0),
        (largura - 1, 0),
        (largura - 1, altura - 1),
        (0, altura - 1)
    ]

    # Botões
    botao_largura = 200
    botao_altura = 90
    espacamento = largura // 3
    by = (altura // 2)-50
    botao_by=altura-altura//3

    pontos_botoes = []
    for i in range(1, 3):
        x_base = i * espacamento
        pontos = [
            (x_base - botao_largura // 2, botao_by),
            (x_base + botao_largura // 2, botao_by),
            (x_base + botao_largura // 2, botao_by + botao_altura),
            (x_base - botao_largura // 2, botao_by + botao_altura)
        ]
        pontos_botoes.append((x_base, pontos))

    fonte_titulo = pygame.font.SysFont("Arial", 65, bold=True)
    fonte_instrucao = pygame.font.SysFont("Arial", 15, bold=True)

    surf_titulo = fonte_titulo.render("VAI PASSAR FOME!", True, LARANJA)
    surf_outline = fonte_titulo.render("VAI PASSAR FOME!", True, PRETO)

    # Textos dos dois botões (respectiva ordem: botão esquerdo, botão direito)
    textos_botoes = [
        "ESC para voltar ao menu",
        "ESPAÇO para jogar de novo"
    ]

    acao = None
    while menu_ativo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    acao = "play"
                    menu_ativo = False
                elif evento.key == pygame.K_ESCAPE:
                    acao = "menu"
                    menu_ativo = False

        # Desenhar fundo preto com scanline
        funcoes.desenhar_poligono(tela, fundo, AZUL)
        funcoes.boundary_fill(tela,200,150,AZUL, AZUL)
        cenario.desenhar_game_over(tela)
       

        # Título com contorno
        titulo_x = largura // 2 - surf_titulo.get_width() // 2
        titulo_y = by - surf_titulo.get_height() - 25
        offsets = [(-2,0), (2,0), (0,-2), (0,2), (-2,-2), (2,2), (-2,2), (2,-2)]
        for ox, oy in offsets:
            tela.blit(surf_outline, (titulo_x + ox, titulo_y + oy))
        tela.blit(surf_titulo, (titulo_x, titulo_y))

        # Desenhar os dois botões e seus texto
        for idx, (x_base, pontos_botao) in enumerate(pontos_botoes):
            funcoes.desenhar_poligono(tela, pontos_botao, BRANCO)
            funcoes.scanline(tela, pontos_botao, LARANJA)

            label = fontes = fonte_instrucao.render(textos_botoes[idx], True, PRETO)
            label_x = x_base - label.get_width() // 2
            label_y = botao_by + botao_altura // 2 - label.get_height() // 2
            tela.blit(label, (label_x, label_y))

        pygame.display.flip()
        clock.tick(30)

    return acao 