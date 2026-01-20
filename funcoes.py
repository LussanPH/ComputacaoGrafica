import math
from constantes import largura, altura

def setPixel(tela, x, y, cor):#Desenha um pixel
    if x < 0 or x > largura or y < 0 or y > altura:
        return
    else:
        tela.set_at((x, y), cor)

def dda(tela, x0, x1, y0, y1, cor):#Desenha uma reta por dda
    deltaX = x1 - x0
    deltaY = y1 - y0

    passos = max(abs(deltaX), abs(deltaY))

    xIncremento = deltaX/passos
    yIncremento = deltaY/passos

    xNovo = x0
    yNovo = y0
    while yNovo != y1 and xNovo != x1:
        if tela.get_at((round(xNovo), round(yNovo))) == (255, 255, 255, 255):
            continue
        setPixel(tela, round(xNovo), round(yNovo), cor)
        xNovo += xIncremento
        yNovo += yIncremento

def bresenham_reta(tela, x0, x1, y0, y1, cor):
    deltaX = abs(x1 - x0)
    deltaY = abs(y1 - y0)

    direcaoX = 1
    direcaoY = 1
    if x0 > x1:
        direcaoX = -1
    if y0 > y1:
        direcaoY = -1

    p = deltaX - deltaY

    while True:
        setPixel(tela, x0, y0, cor)

        if x0 == x1 and y0 == y1:
            break

        p2 = 2 * p

        if p2 > -deltaY:
            p -= deltaY
            x0 += direcaoX

        if p2 < deltaX:
            p += deltaX
            y0 += direcaoY

def desenhar_poligono(tela, pontos, cor):
    n = len(pontos)
    if n < 3:
        return  
    for i in range(n):
        x0, y0 = pontos[i]
        x1, y1 = pontos[(i + 1) % n] 
        bresenham_reta(tela, x0, x1, y0, y1, cor)

def setPixel_simetria_circulo(tela, xc, yc, x, y, cor):
    setPixel(tela, xc + x, yc + y, cor)
    setPixel(tela, xc - x, yc + y, cor)
    setPixel(tela, xc + x, yc - y, cor)
    setPixel(tela, xc - x, yc - y, cor)
    setPixel(tela, xc + y, yc + x, cor)
    setPixel(tela, xc - y, yc + x, cor)
    setPixel(tela, xc + y, yc - x, cor)
    setPixel(tela, xc - y, yc - x, cor)

def bresenham_circulo(tela, xc, yc, r, cor):
     x = 0
     y = r

     p = 1 - r   # parâmetro de decisão inicial

     setPixel_simetria_circulo(tela, xc, yc, x, y, cor)

     while x < y:
        x += 1

        if p < 0:
            # escolhe E
            p = p + 2*x + 1
        else:
            # escolhe SE
            y -= 1
            p = p + 2*(x - y) + 1

        setPixel_simetria_circulo(tela, xc, yc, x, y, cor)

def setPixel_simetria_elipse(tela, xc, yc, x, y, cor):
    setPixel(tela, xc + x, yc + y, cor)
    setPixel(tela, xc - x, yc + y, cor)
    setPixel(tela, xc + x, yc - y, cor)
    setPixel(tela, xc - x, yc - y, cor)

def bresenham_elipse(tela, xc, yc, a, b, cor):
    x = 0
    y = b

    a2 = a * a
    b2 = b * b

    # Região 1
    p = b2 - a2*b + a2//4

    setPixel_simetria_elipse(tela, xc, yc, x, y, cor)

    while 2*b2*x < 2*a2*y:
        x += 1

        if p < 0:
            p = p + 2*b2*x + b2
        else:
            y -= 1
            p = p + 2*b2*x - 2*a2*y + b2

        setPixel_simetria_elipse(tela, xc, yc, x, y, cor)

    # Região 2
    p = b2*(x + 0.5)*(x + 0.5) + a2*(y - 1)*(y - 1) - a2*b2

    while y > 0:
        y -= 1

        if p > 0:
            p = p - 2*a2*y + a2
        else:
            x += 1
            p = p + 2*b2*x - 2*a2*y + a2

        setPixel_simetria_elipse(tela, xc, yc, x, y, cor)

def boundary_fill(surface,x,y,boundary_color,fill_color):
    stack=[]
    
    stack.append((x,y))
    while stack:
        x,y=stack.pop()
        if x < 0 or x >= largura or y < 0 or y >= altura:
           continue
        
        current_color=surface.get_at((x,y))
        
        if( current_color!= boundary_color and current_color != fill_color):
            setPixel(surface, x, y, fill_color)
            stack.append((x+1,y))
            stack.append((x-1,y))
            stack.append((x,y+1))
            stack.append((x,y-1))
             
def scanline(surface, pontos, cor):
    ys = [p[1] for p in pontos]
    ymin = min(ys)
    ymax = max(ys)

    n = len(pontos)

    for y in range(ymin, ymax):
        intersecoes = []

        for i in range(n):
            x0, y0 = pontos[i]
            x1, y1 = pontos[(i + 1) % n]

            # Ignorar arestas horizontais
            if y0 == y1:
                continue

            # Garantir y0 < y1
            if y0 > y1:
                x0, y0, x1, y1 = x1, y1, x0, y0

            # Scanline fora da aresta
            if y < y0 or y >= y1:
                continue

            # Cálculo da interseção
            x = x0 + (y - y0) * (x1 - x0) / (y1 - y0)
            intersecoes.append(x)

        intersecoes.sort()

        # Preenchimento entre pares
        for i in range(0, len(intersecoes), 2):
            if i + 1 < len(intersecoes):
                x_inicio = int(round(intersecoes[i]))
                x_fim = int(round(intersecoes[i + 1]))

                for x in range(x_inicio, x_fim + 1):
                    setPixel(surface, x, y, cor)
