# Definição do grafo como um dicionário de dicionários, representando as conexões e os custos.
graph = {}
graph['beginning'] = {}
graph['beginning']['a'] = 6
graph['beginning']['b'] = 2

graph['a'] = {}
graph['a']['end'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['end'] = 5
graph['end'] = {}

# Custos iniciais para cada nodo. A distância para 'end' é infinita no início.
infinito = float('inf')
custos = {}
custos['a'] = 6
custos['b'] = 2
custos['end'] = infinito

# Armazenamento dos pais de cada nodo para rastrear o caminho.
pais = {}
pais['a'] = 'beginning'
pais['b'] = 'beginning'
pais['end'] = None

# Lista de nodos que já foram processados.
processados = []

# Função que encontra o nodo com o menor custo que ainda não foi processado.
def ache_o_nodo_mais_barato(custos):
    custo_mais_baixo, nodo_custo_mais_baixo = float('inf'), None
    # Itera por todos os nodos e encontra o custo mais baixo.
    for nodo in custos:
        custo = custos[nodo]
        # Se o custo for o mais baixo e o nodo não foi processado ainda, atualiza.
        if custo < custo_mais_baixo and nodo not in processados:
            custo_mais_baixo = custo
            nodo_custo_mais_baixo = nodo
    return nodo_custo_mais_baixo

# Testando a função para encontrar o nodo com o custo mais baixo.
print(ache_o_nodo_mais_barato(custos))  # Output esperado: 'b' (custo 2)
