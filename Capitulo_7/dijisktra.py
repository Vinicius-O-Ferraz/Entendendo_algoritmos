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

#custos
infinito = float('inf')
custos = {}
custos['a'] = 6
custos['b'] = 2
custos['end'] = infinito

pais = {}
pais['a'] = 'beginning'
pais['b'] = 'beginning'
pais['end'] = None

processados = []

def ache_o_nodo_mais_barato(custos):
    custo_mais_baixo, nodo_custo_mais_baixo = float('inf'), None
    for nodo in custos:
        custo = custos[nodo]
        if custo< custo_mais_baixo and nodo not in processados:
            custo_mais_baixo = custo
            nodo_custo_mais_baixo = nodo
    return nodo_custo_mais_baixo

print(ache_o_nodo_mais_barato(custos))