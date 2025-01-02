import time  # Biblioteca para medir o tempo de execução
from math import floor  # Opcional: 'floor' não está sendo usado neste código

def b_search(list: list, element: any, etapas=0):
    """
    Implementa o algoritmo de busca binária.
    
    Args:
        list (list): Lista ordenada onde a busca será realizada.
        element (any): Elemento que se deseja encontrar.
        etapas (int, opcional): Contador de etapas para acompanhar o número de iterações.

    Returns:
        int | None: Retorna o índice do elemento encontrado ou None se o elemento não estiver na lista.
    """
    # Definindo os limites superior (up) e inferior (down) da lista
    up, down = len(list) - 1, 0

    # Loop até que o intervalo de busca se esgote
    while down <= up:
        # Calcula o índice do meio do intervalo
        middle = (down + up) // 2
        guess = list[middle]  # Obtém o elemento no índice 'middle'

        # Verifica se o elemento foi encontrado
        if guess == element:
            print(f"Achamos {element} em {etapas} etapas")  # Informa o número de etapas
            return middle  # Retorna o índice do elemento encontrado
        
        # Ajusta o intervalo de busca dependendo da comparação
        if guess > element:
            etapas += 1  # Incrementa o contador de etapas
            up = middle - 1  # Atualiza o limite superior
        else:
            etapas += 1  # Incrementa o contador de etapas
            down = middle + 1  # Atualiza o limite inferior
    
    # Retorna None se o elemento não for encontrado
    return None

# Define uma lista ordenada de números de 1 até 99.999.999
lista = range(1, 100000000)

# Mede o tempo de execução da busca
start = time.time_ns()  # Tempo inicial em nanosegundos
print(b_search(lista, 128))  # Busca o elemento 128 na lista
end = time.time_ns()  # Tempo final em nanosegundos

# Calcula e exibe o tempo total decorrido em nanosegundos
print(f"O tempo decorrido é de {(end - start)}ns")
