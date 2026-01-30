# Djonga Run

**Autores:** Lucas Levi, Antônio Ícaro e Pedro Luna.

## Proposta do Jogo
O cotidiano de um estudante da **Universidade Estadual do Ceará (UECE)** é uma verdadeira corrida de obstáculos. Entre uma aula e outra, a missão é clara: atravessar o campus, desviar dos pombos estratégicos e dos cachorros territoriais para alcançar o prêmio máximo — o **Restaurante Universitário (RU)** — antes que a fome vença.

## 🛠️ O Desafio Técnico: Motor Gráfico Próprio de CG
Este projeto foi construído sob a premissa da **Computação Gráfica de baixo nível**. O motor gráfico foi desenvolvido do zero, partindo da primitiva fundamental `setPixel`. Diferente de motores comerciais, toda a renderização é fruto da implementação dos algoritmos clássicos:

* **Traçado de Linhas:** Implementação dos algoritmos de **DDA** e **Bresenham**.
* **Preenchimento de Áreas:** Algoritmo de **Scanline** para polígonos complexos, e os algoritmos recursivos **Boundary Fill** e **Flood Fill** para preenchimento de regiões delimitadas.
* **Curvas e Primitivas:** Desenho de poligonos, círculos e elipses via algoritmos.
* **Transformações Geométricas:** Funções de **Rotação**, **Translação** e **Escala**. Todos via cálculo de matrizes.
* **Recorte (Clipping):** Implementação de **Sutherland-Hodgman** para delimitação de tela.

---

## Estrutura de Arquivos

### 1. `funcoes.py` (O Motor de CG)
O núcleo matemático do projeto. Contém as implementações de rasterização, manipulação de matrizes para transformações e o gerenciamento da viewport.

### 2. `cachorro.py` (Inimigo Terrestre)
Gerencia a renderização dos cachorros do campus. Utiliza **elipses preenchidas** para o corpo e rotação dinâmica de polígonos para as pernas. A hitbox é estrategicamente posicionada no dorso para permitir o pulo do jogador.

### 3. `pombo.py` (Inimigo Aéreo)
Controla os pombos da UECE. Implementa a batida de asas através de transformações de rotação em tempo real. Sua hitbox estreita exige que o jogador calcule precisamente o tempo de permanência no ar.

### 4. `modelos_ru.py` (A Fila do RU)
Responsável por criar os personagens que compõem a fila final do restaurante. Utiliza uma abordagem de **renderização por camadas (Back-to-Front)** e aplica pesadamente as transformações de **Escala** (para contornos e mochilas), **Rotação** (para postura de cansaço) e **Translação**.

### 5. `jogo.py` (Gerenciador de Estado e Lógica)
Centraliza o **Dicionário de Estado**. Controla a física do pulo, a progressão da dificuldade e garante que o reset de jogo limpe corretamente a memória de frames anteriores.

### 6. `colisoes.py` (Sistema de Detecção)
Implementa a lógica de **AABB (Axis-Aligned Bounding Box)** com múltiplas hitboxes simultâneas, permitindo que a cabeça e o corpo do jogador tenham detecções independentes.

### 7. `jogador.py`, `cenario.py`, `telas.py` e `main.py`
Gerenciam o herói (Djonga), o scroll do campus, as interfaces de usuário e a orquestração do loop principal com sincronia de Delta Time.

---

## Lógica e Matemática Aplicada

### Animação Procedural e Trigonométrica
Para dar vida aos personagens sem o uso de imagens externas, o motor utiliza funções trigonométricas para calcular ângulos de rotação em tempo real:

1. **Oscilação de Membros:**
   Calculamos o ângulo ($\theta$) para pernas e asas usando:
   $$\theta = A \cdot \sin(\phi \cdot v + \text{offset})$$
   Isso permite que cachorros e pombos tenham ritmos de animação orgânicos.

2. **Modelagem via Camadas:**
   Nos modelos da fila do RU, as partes do corpo são tratadas como objetos geométricos independentes que sofrem transformações relativas a um ponto pivô $(x, y)$, permitindo a criação de diversas posturas de alunos apenas alterando matrizes.



### Sincronização de Tempo (Delta Time)
Para evitar "teletransportes" após pausas ou lags, o motor implementa um reset de clock:
$$posicao = posicao + (velocidade \times dt)$$
Onde $dt$ é limitado para garantir estabilidade física mesmo em quedas de performance.

---

## Link do Repositório: 
https://github.com/LussanPH/ComputacaoGrafica.git

## Como Executar
1. Certifique-se de ter o **Python 3** e a biblioteca **Pygame** instalados.
2. Execute o comando:
   ```bash
   python main.py