import math
from constantes import *


def setPixel(tela, x, y, cor):#Desenha um pixel
    if x < 0 or x > largura or y < 0 or y > altura:
        return
    else:
        tela.set_at((x, y), cor)


def dda(tela, x0, x1, y0, y1, cor):
    deltaX = x1 - x0
    deltaY = y1 - y0
    passos = int(max(abs(deltaX), abs(deltaY)))
    if passos == 0:
        setPixel(tela, x0, y0, cor)
        return
    xIncremento = deltaX / passos
    yIncremento = deltaY / passos
    x = x0
    y = y0
    for i in range(passos + 1):
        setPixel(tela, round(x), round(y), cor)
        x += xIncremento
        y += yIncremento


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


def get_simetria_circulo(xc, yc, x, y):
    return [
        (xc + x, yc + y), (xc - x, yc + y), (xc + x, yc - y),
        (xc - x, yc - y), (xc + y, yc + x), (xc - y, yc + x),
        (xc + y, yc - x), (xc - y, yc - x)]


def bresenham_circulo(tela, xc, yc, r, cor):
    x = 0
    y = r

    p = 1 - r   # parâmetro de decisão inicial

    pontos_circulo = []

    lista_pontos = get_simetria_circulo(xc, yc, x, y)

    for ponto in lista_pontos:
        pontos_circulo.append(ponto)

    while x < y:
        x += 1

        if p < 0:
            # escolhe E
            p = p + 2*x + 1
        else:
            # escolhe SE
            y -= 1
            p = p + 2*(x - y) + 1

        lista_pontos = get_simetria_circulo(xc, yc, x, y)
        for ponto in lista_pontos:
            pontos_circulo.append(ponto)
    
    return pontos_circulo


def get_simetria_elipse(xc, yc, x, y):
    return [(xc + x, yc + y), (xc - x, yc + y),
            (xc + x, yc - y), (xc - x, yc - y)]


def bresenham_elipse(tela, xc, yc, a, b, cor):
    pontos_elipse = []

    x = 0
    y = b

    a2 = a * a
    b2 = b * b

    # Região 1
    p = b2 - a2*b + a2//4

    lista_pontos = get_simetria_elipse(xc, yc, x, y)
    for ponto in lista_pontos:
        pontos_elipse.append(ponto)

    while 2*b2*x < 2*a2*y:
        x += 1

        if p < 0:
            p = p + 2*b2*x + b2
        else:
            y -= 1
            p = p + 2*b2*x - 2*a2*y + b2

        lista_pontos = get_simetria_elipse(xc, yc, x, y)
        for ponto in lista_pontos:
            pontos_elipse.append(ponto)

    # Região 2
    p = b2*(x + 0.5)*(x + 0.5) + a2*(y - 1)*(y - 1) - a2*b2

    while y > 0:
        y -= 1

        if p > 0:
            p = p - 2*a2*y + a2
        else:
            x += 1
            p = p + 2*b2*x - 2*a2*y + a2

        lista_pontos = get_simetria_elipse(xc, yc, x, y)
        for ponto in lista_pontos:
            pontos_elipse.append(ponto)
    
    return pontos_elipse


def boundary_fill(tela, x, y, boundary_color, fill_color):
    # iterativo com pilha; compara apenas RGB (ignora alpha)
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        if cx < 0 or cx >= largura or cy < 0 or cy >= altura:
            continue
        current_color = tela.get_at((cx, cy))[:3]
        if current_color != tuple(boundary_color) and current_color != tuple(fill_color):
            setPixel(tela, cx, cy, fill_color)
            stack.append((cx + 1, cy))
            stack.append((cx - 1, cy))
            stack.append((cx, cy + 1))
            stack.append((cx, cy - 1))


def scanline(tela, pontos, cor):
    ys = [p[1] for p in pontos]
    ymin = max(0, min(ys))
    ymax = min(altura - 1, max(ys))
    n = len(pontos)
    for y in range(ymin, ymax + 1):
        intersecoes = []
        for i in range(n):
            x0, y0 = pontos[i]
            x1, y1 = pontos[(i + 1) % n]
            if y0 == y1:
                continue
            if y0 > y1:
                x0, y0, x1, y1 = x1, y1, x0, y0
            if y < y0 or y >= y1:
                continue
            x_int = x0 + (y - y0) * (x1 - x0) / (y1 - y0)
            intersecoes.append(x_int)
        intersecoes.sort()
        for i in range(0, len(intersecoes), 2):
            if i + 1 < len(intersecoes):
                x_start = int(round(intersecoes[i]))
                x_end = int(round(intersecoes[i + 1]))
                x_start = max(0, x_start)
                x_end = min(largura - 1, x_end)
                for x in range(x_start, x_end + 1):
                    setPixel(tela, x, y, cor)
                    
def scanline_fill_circle(surface, xc, yc, r, cor):
    
    if r <= 0:
        return

    ymin = max(0, int(math.ceil(yc - r)))
    ymax = min(altura - 1, int(math.floor(yc + r)))

    r2 = r * r
    for y in range(ymin, ymax + 1):
        dy = y - yc
        inside = r2 - dy * dy
        if inside < 0:
            continue
        dx = int(math.floor(math.sqrt(inside)))
        x_start = max(0, xc - dx)
        x_end = min(largura - 1, xc + dx)
        for x in range(x_start, x_end + 1):
            setPixel(surface, x, y, cor)

def scanline_fill_ellipse(surface, xc, yc, a, b, cor):
    if a <= 0 or b <= 0:
        return

    ymin = max(0, int(math.ceil(yc - b)))
    ymax = min(altura - 1, int(math.floor(yc + b)))

    a2 = a * a
    b2 = b * b
    for y in range(ymin, ymax + 1):
        dy = y - yc
        val = 1.0 - (dy * dy) / b2
        if val <= 0:
            if val < 0:
                continue
            dx = 0
        else:
            dx = int(math.floor(a * math.sqrt(val)))
        x_start = max(0, xc - dx)
        x_end = min(largura - 1, xc + dx)
        for x in range(x_start, x_end + 1):
            setPixel(surface, x, y, cor)

def escala(pontos,sx,sy):
    xm=[]
    ym=[]
    for p in pontos:
        xm.append(p[0])
        ym.append(p[1])
    
    xc= sum(xm)/len(xm)
    yc= sum(ym)/len(ym)
    
    novos_pontos=[]
    
    for x,y in pontos:
        xn= xc+(x-xc)*sx
        yn= yc+(y-yc)*sy
        novos_pontos.append((int(xn),int(yn)))
    return novos_pontos


def multiplicar_matriz_ponto(M,p):
    x,y,w = p
    x_novo = M[0][0]*x + M[0][1]*y + M[0][2]*w
    y_novo = M[1][0]*x + M[1][1]*y + M[1][2]*w
    w_novo = M[2][0]*x + M[2][1]*y + M[2][2]*w
    return(x_novo,y_novo,w_novo)


def matriz_translacao(tx, ty):
    return [
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ]


def transladar_pontos(pontos,tx,ty):
    T = matriz_translacao(tx,ty)
    novos_pontos = []
    for x,y in pontos:
        x_novo,y_novo,_ = multiplicar_matriz_ponto(T,(x,y,1))
        novos_pontos.append((int(x_novo), int(y_novo)))
        
    return novos_pontos

def calcular_centro_media(vertices):
    soma_x = 0
    soma_y = 0
    qtd = len(vertices)

    for x, y in vertices:
        soma_x += x
        soma_y += y
    
    x = int(soma_x / qtd)
    y = int(soma_y / qtd)

    return (x, y)


def rotacionar(vertices, angulo_graus, pivoXY):
    xPivo, yPivo = pivoXY

    angulo_rad = math.radians(angulo_graus)

    cosseno_angulo = math.cos(angulo_rad)
    seno_angulo = math.sin(angulo_rad)

    vertices_rotacionados = []
    
    for inicialX, inicialY in vertices:
        x_relativo = inicialX - xPivo
        y_relativo = inicialY - yPivo

        x_rotacionado = int((x_relativo * cosseno_angulo) - (y_relativo * seno_angulo))
        y_rotacionado = int((x_relativo * seno_angulo) + (y_relativo * cosseno_angulo))

        x_final = x_rotacionado + xPivo
        y_final = y_rotacionado + yPivo

        vertices_rotacionados.append((x_final, y_final))

    
    
    return vertices_rotacionados

def inside_left(p, xmin):
    return p[0] >= xmin

def inside_right(p, xmax):
    return p[0] <= xmax

def inside_top(p, ymin):      
    return p[1] >= ymin

def inside_bottom(p, ymax):
    return p[1] <= ymax

def intersect_left(p, q, xmin):
    x1, y1 = p
    x2, y2 = q
    y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
    return xmin, int(round(y))

def intersect_right(p, q, xmax):
    x1, y1 = p
    x2, y2 = q
    y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
    return xmax, int(round(y))

def intersect_top(p, q, ymin):
    x1, y1 = p
    x2, y2 = q
    x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
    return int(round(x)), ymin

def intersect_bottom(p, q, ymax):
    x1, y1 = p
    x2, y2 = q
    x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
    return int(round(x)), ymax


def sutherland_hodgman(polygon, xmin, ymin, xmax, ymax):
    output = polygon

    # LEFT
    input_list = output
    output = []
    for i in range(len(input_list)):
        p = input_list[i - 1]
        q = input_list[i]

        if inside_left(q, xmin):
            if not inside_left(p, xmin):
                output.append(intersect_left(p, q, xmin))
            output.append(q)
        elif inside_left(p, xmin):
            output.append(intersect_left(p, q, xmin))

    # RIGHT
    input_list = output
    output = []
    for i in range(len(input_list)):
        p = input_list[i - 1]
        q = input_list[i]

        if inside_right(q, xmax):
            if not inside_right(p, xmax):
                output.append(intersect_right(p, q, xmax))
            output.append(q)
        elif inside_right(p, xmax):
            output.append(intersect_right(p, q, xmax))

    # TOP
    input_list = output
    output = []
    for i in range(len(input_list)):
        p = input_list[i - 1]
        q = input_list[i]

        if inside_top(q, ymin):
            if not inside_top(p, ymin):
                output.append(intersect_top(p, q, ymin))
            output.append(q)
        elif inside_top(p, ymin):
            output.append(intersect_top(p, q, ymin))

    # BOTTOM
    input_list = output
    output = []
    for i in range(len(input_list)):
        p = input_list[i - 1]
        q = input_list[i]

        if inside_bottom(q, ymax):
            if not inside_bottom(p, ymax):
                output.append(intersect_bottom(p, q, ymax))
            output.append(q)
        elif inside_bottom(p, ymax):
            output.append(intersect_bottom(p, q, ymax))

    return output


def intersecao(x1,y1,w1,h1,x2,y2,w2,h2):
    has_collision = False
    if (x1 < x2 + w2 and x1 + w1 > x2 and y1 < y2 + h2 and y1 +h1 > y2 ):
        has_collision = True

    return has_collision    

def setTexturaCabeca(tela, textura, x_centro, y_centro, raio):
    largura_textura, altura_textura = textura.get_size()
    diametro = raio*2

    for y in range(y_centro - raio, y_centro + raio):
        for x in range(x_centro - raio, x_centro + raio):
            distancia_ao_quadrado = (x - x_centro)**2 + (y - y_centro)**2
            
            if distancia_ao_quadrado <= raio**2:
                x_minimo = x_centro - raio
                y_minimo = y_centro - raio

                u = (x - x_minimo)/diametro
                v = (y - y_minimo)/diametro

                tx = int(u * (largura_textura - 1))
                ty = int(v * (altura_textura - 1))
            
                cor = textura.get_at((tx, ty))
                tela.set_at((x, y), cor)

def viewport(tela):
    quadrado = [(5, (altura - altura//6)), (5, altura - 10), (largura//6, altura - 10), (largura//6, (altura - altura//6))]

    desenhar_poligono(tela, quadrado, PRETO)
