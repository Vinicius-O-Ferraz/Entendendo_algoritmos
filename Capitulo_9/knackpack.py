# número de itens e tamanho da mochila
quantidade, capacidade = input().split()
quantidade, capacidade = int(quantidade), int(capacidade)

mochila = []
pesos, valores = [0 for i in range((quantidade))],[0 for i in range((quantidade))]

for _ in range(quantidade):
    temp = []
    temp = input().split()
    pesos[_] = int(temp[0])
    valores[_] = int(temp[1])

def knapsack(pesos, valores, quantidade, capacidade):
    m = [[0] * (capacidade + 1) for _ in range(quantidade + 1)]

    for i in range(1, quantidade + 1):
        for j in range(1, capacidade + 1):
            a = m[i - 1][j]
            b = 0
            if pesos[i - 1] <= j:
                b = valores[i - 1] + m[i - 1][j - pesos[i - 1]]
            m[i][j] = max(a, b)

    return m[quantidade][capacidade]

resultado = knapsack(pesos, valores, quantidade, capacidade)
print(f"Valor máximo que pode ser colocado na mochila: {resultado}")
       
    

