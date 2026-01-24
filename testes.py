# Teste DDA (reta)
#funcoes.dda(tela, 0, 599, 0, 399, BRANCO)

# Teste Bresenham (reta)
#funcoes.bresenham_reta(tela, 300, 500, 200, 350, BRANCO)

# Teste CÍRCULO
'''funcoes.bresenham_circulo(
    tela,
    xc=150,
    yc=200,
    r=80,
    cor=BRANCO
    )'''

# Teste ELIPSE
'''funcoes.bresenham_elipse(
    tela,
    xc=420,
    yc=200,
    a=120,   # raio horizontal
    b=60,    # raio vertical
    cor=BRANCO
    )'''
    
#Teste Desenhar e Pintar Polígono
'''poligono_boundary = [
    (100, 80),
    (200, 200),
    (60, 260)
]
    
funcoes.desenhar_poligono(
    tela,
    poligono_boundary,
    BRANCO
)

funcoes.scanline(
    tela,
    poligono_boundary,
    BRANCO
)'''
    
#Teste Translação
'''quadrado = [(350, 50),(450, 50),(450, 150),(350, 150)]

quadrado_t = funcoes.transladar_pontos(quadrado, 80, 40)

funcoes.desenhar_poligono(tela, quadrado, BRANCO)
funcoes.desenhar_poligono(tela, quadrado_t, BRANCO)'''

#Teste Rotação
'''if cont == 0:
    quadrado = [(350, 50),(450, 50),(450, 150),(350, 150)]
    cont += 1
    velocidade_e_sentido = 2
    angulo_graus = 0
    pivoXY = funcoes.calcular_centro_media(quadrado)
quadrado_rotacionado, angulo_graus = funcoes.rotacionar(quadrado, velocidade_e_sentido, angulo_graus, pivoXY)
if angulo_graus >= 360:
    angulo_graus = 0
funcoes.desenhar_poligono(tela, quadrado_rotacionado, BRANCO)'''