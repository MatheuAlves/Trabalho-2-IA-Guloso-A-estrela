from collections import deque
from time import perf_counter
import tracemalloc

matriz = [
    ['A', 'B', 'C', 'D', 'E'],
    ['F', 'G', 'H', 'I', 'J'],
    ['K', 'L', 'M', 'N', 'O'],
    ['P', 'Q', 'R', 'S', 'T'],
    ['U', 'V', 'X', 'Y', 'Z']
]

barreiras = [
    ((0, 1), (0, 2)), # B - C
    ((0, 2), (0, 1)), # C - B
    ((0, 1), (1, 1)), # B - G
    ((1, 1), (0, 1)), # G - B
    ((0, 3), (1, 3)), # D - I
    ((1, 3), (0, 3)), # I - D
    ((1, 3), (1, 4)), # I - J
    ((1, 4), (1, 3)), # J - I
    ((1, 0), (2, 0)), # F - K
    ((2, 0), (1, 0)), # K - F
    
    ((1, 1), (2, 1)), # G - L
    ((2, 1), (1, 1)), # L - G
    ((1, 2), (2, 2)), # H - M
    ((2, 2), (1, 2)), # M - H
    ((1, 4), (2, 4)), # J - O
    ((2, 4), (1, 4)), # O - J
    ((2, 0), (2, 1)), # K - L
    ((2, 1), (2, 0)), # L - K
    ((2, 3), (3, 3)), # N - S
    ((3, 3), (2, 3)), # S - N
    
    ((2, 4), (3, 4)), # O - T
    ((3, 4), (2, 4)), # T - O
    ((3, 0), (3, 1)), # P - Q
    ((3, 1), (3, 0)), # Q - P
    ((3, 1), (3, 2)), # Q - E
    ((3, 2), (3, 1)), # E - Q
    ((3, 2), (4, 2)), # E - X
    ((4, 2), (3, 2)), # X - E
    ((3, 3), (4, 3)), # S - Y
    ((4, 3), (3, 3)), # Y - S
]


inicio = (4, 0) 
fim = (0, 4) 
movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def heuristica_manhattan(pos_atual, fim):
    x = abs(pos_atual[0] - fim[0])
    y = abs(pos_atual[1] - fim[1])
    distancia = x + y
    return distancia

def tem_barreira(matriz, pos_atual, prox_pos):
    coordenadas = (pos_atual, prox_pos)
    for i in barreiras:
        if coordenadas == i:
            return True
    return False

def testa_posicoes_futuras(caminho, pos_atual, matriz, g_atual, fim, lista_de_posicoes_futuras):
    for movimento in movimentos:
            prox_pos = (pos_atual[0] + movimento[0], pos_atual[1] + movimento[1])
            
            # Verifica se a posição está dentro dos limites da matriz e não tem barreira
            if 0 <= prox_pos[0] < len(matriz) and 0 <= prox_pos[1] < len(matriz[0]):
                if not tem_barreira(matriz, pos_atual, prox_pos):
                    g = g_atual[pos_atual] + 1
                    h = heuristica_manhattan(prox_pos, fim)
                    f = g + h
            
            # Adiciona à lista aberta se for mais eficiente
            if prox_pos not in g or g_atual < g[prox_pos]:
                g_atual[prox_pos] = g
                lista_de_posicoes_futuras.append((prox_pos, f))

def imprime_A_estrela(caminho, caminho_valores, tempo_bfs, memoria, pico_memoria):
    print(f'Caminho A*: {caminho}')
    print(f'Caminho A*: {caminho_valores}')
    print(f'Tempo total A*: {tempo_bfs:.10f}')
    print(f'Consumo de Memória A*: {memoria / 1024:.2f} KB; Pico: {pico_memoria / 1024:.2f} KB')

def A_estrela(matriz, inicio, fim, movimentos):
    inicio_tempo_A_estrela = perf_counter()
    tracemalloc.start()
    
    pos_atual = inicio
    caminho  = []
    caminho_valores = []
    g_atual = {inicio: 0}
    pais = {inicio: None}
    lista_de_posicoes_futuras = []
    h = heuristica_manhattan(inicio, fim)
    lista_de_posicoes_futuras.append((inicio, h))
    
    while lista_de_posicoes_futuras:
        # Ordena a lista pela segunda posição (o f), pegando o elemento de menor f
        lista_de_posicoes_futuras.sort(key=lambda x: x[1])
        pos_atual, _ = lista_de_posicoes_futuras.pop(0)  # Remove o primeiro elemento, o de menor f
        
        if pos_atual == fim:
            # Reconstrua o caminho a partir dos pais
            while pos_atual is not None:
                caminho.append(pos_atual)
                caminho_valores.append(matriz[pos_atual[0]][pos_atual[1]])
                pos_atual = pais.get(pos_atual, None)
            fim_tempo_A_estrela = perf_counter()
            tempo_total_A_estrela = fim_tempo_A_estrela - inicio_tempo_A_estrela
            caminho.reverse()
            caminho_valores.reverse()
            memoria, pico_memoria = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            imprime_A_estrela(caminho, caminho_valores, tempo_total_A_estrela, memoria, pico_memoria)
            return caminho
    
        # Testa as posições futuras a partir da posição atual
        for movimento in movimentos:
            prox_pos = (pos_atual[0] + movimento[0], pos_atual[1] + movimento[1])

            # Verifica se a posição está dentro dos limites da matriz e não tem barreira
            if 0 <= prox_pos[0] < len(matriz) and 0 <= prox_pos[1] < len(matriz[0]):
                if prox_pos not in g_atual or g_atual[pos_atual] + 1 < g_atual[prox_pos]:
                    g_atual[prox_pos] = g_atual[pos_atual] + 1
                    h = heuristica_manhattan(prox_pos, fim)
                    f = g_atual[prox_pos] + h
                    lista_de_posicoes_futuras.append((prox_pos, f))
                    pais[prox_pos] = pos_atual

    print('Matriz não tem solução!')
    tracemalloc.stop()
    return None

def guloso(matriz, inicio, fim, movimentos):
    inicio_tempo_guloso = perf_counter()
    tracemalloc.start()
    
    pos_atual = inicio
    caminho  = []
    caminho_valores = []
    pais = {inicio: None}
    lista_de_posicoes_futuras = []
    h = heuristica_manhattan(inicio, fim)
    lista_de_posicoes_futuras.append((inicio, h))
    
    while lista_de_posicoes_futuras:
        # Ordena a lista pela heurística (h), pegando o elemento com a menor heurística
        lista_de_posicoes_futuras.sort(key=lambda x: x[1])
        pos_atual, _ = lista_de_posicoes_futuras.pop(0)  # Remove o primeiro elemento, o de menor h
        
        if pos_atual == fim:
            # Reconstrua o caminho a partir dos pais
            while pos_atual is not None:
                caminho.append(pos_atual)
                caminho_valores.append(matriz[pos_atual[0]][pos_atual[1]])
                pos_atual = pais.get(pos_atual, None)
            fim_tempo_guloso = perf_counter()
            tempo_total_guloso = fim_tempo_guloso - inicio_tempo_guloso
            caminho.reverse()
            caminho_valores.reverse()
            memoria, pico_memoria = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            imprime_A_estrela(caminho, caminho_valores, tempo_total_guloso, memoria, pico_memoria)
            return caminho
    
        # Testa as posições futuras a partir da posição atual
        for movimento in movimentos:
            prox_pos = (pos_atual[0] + movimento[0], pos_atual[1] + movimento[1])

            # Verifica se a posição está dentro dos limites da matriz e não tem barreira
            if 0 <= prox_pos[0] < len(matriz) and 0 <= prox_pos[1] < len(matriz[0]):
                if not tem_barreira(matriz, pos_atual, prox_pos) and prox_pos not in pais:
                    h = heuristica_manhattan(prox_pos, fim)
                    lista_de_posicoes_futuras.append((prox_pos, h))
                    pais[prox_pos] = pos_atual

    print('Matriz não tem solução!')
    tracemalloc.stop()
    return None
    
print(f'Início: {matriz[inicio[0]][inicio[1]]}')
print(f'Fim: {matriz[fim[0]][fim[1]]}')

print('-----------A *-----------')
pos_atual = inicio
A_estrela(matriz, inicio, fim, movimentos)

print('--------GULOSO---------')
pos_atual = inicio
guloso(matriz, inicio, fim, movimentos)