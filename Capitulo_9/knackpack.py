# Número de itens e tamanho da mochila
quantidade, capacidade = input().split()
quantidade, capacidade = int(quantidade), int(capacidade)

# Inicializa as listas de pesos e valores
mochila = []
pesos, valores = [0 for i in range(quantidade)], [0 for i in range(quantidade)]

# Preenche os pesos e valores dos itens
for _ in range(quantidade):
    temp = input().split()
    pesos[_] = int(temp[0])  # Peso do item
    valores[_] = int(temp[1])  # Valor do item

# Função para resolver o problema da mochila com programação dinâmica
def knapsack(pesos, valores, quantidade, capacidade):
    # Matriz m onde m[i][j] armazenará o valor máximo que pode ser alcançado com
    # os primeiros i itens e capacidade j
    m = [[0] * (capacidade + 1) for _ in range(quantidade + 1)]

    # Preenche a matriz com os valores ótimos de acordo com a capacidade e os itens
    for i in range(1, quantidade + 1):
        for j in range(1, capacidade + 1):
            # Caso o peso do item seja maior que a capacidade atual da mochila
            a = m[i - 1][j]
            b = 0
            if pesos[i - 1] <= j:  # Se o item cabe na mochila
                # Considera incluir o item ou não
                b = valores[i - 1] + m[i - 1][j - pesos[i - 1]]
            m[i][j] = max(a, b)

    # O valor máximo é encontrado na última célula da matriz
    return m[quantidade][capacidade]

# Chama a função para calcular o valor máximo que pode ser colocado na mochila
resultado = knapsack(pesos, valores, quantidade, capacidade)

# Exibe o resultado
print(f"Valor máximo que pode ser colocado na mochila: {resultado}")

       
    

