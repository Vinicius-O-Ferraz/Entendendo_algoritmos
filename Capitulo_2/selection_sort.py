def smallest_search(lista):
    """
    Encontra o menor elemento de uma lista e retorna seu índice.

    Args:
        lista (list): Lista de elementos.

    Returns:
        int: Índice do menor elemento na lista.
    """
    # Inicializa o menor elemento como o primeiro e seu índice como 0
    smallest, smallest_index = lista[0], 0

    # Itera pela lista a partir do segundo elemento
    for i in range(1, len(lista)):
        # Atualiza o menor elemento e seu índice se encontrar um menor
        if lista[i] < smallest:
            smallest, smallest_index = lista[i], i

    return smallest_index  # Retorna o índice do menor elemento


def s_sort(lista):
    """
    Implementa o algoritmo de ordenação por seleção usando a função smallest_search.

    Args:
        lista (list): Lista de elementos a serem ordenados.

    Returns:
        list: Nova lista com os elementos ordenados em ordem crescente.
    """
    l = []  # Lista para armazenar os elementos ordenados

    # Itera até que todos os elementos sejam removidos da lista original
    for i in range(len(lista)):
        smallest = smallest_search(lista)  # Encontra o menor elemento
        l.append(lista.pop(smallest))  # Remove o menor da lista original e o adiciona na nova lista

    return l  # Retorna a lista ordenada


# Cria uma lista de 100 elementos em ordem decrescente
l = [i for i in range(100, 0, -1)]

# Exibe a lista original
print("Lista original:", l)

# Ordena a lista usando o algoritmo de ordenação por seleção
print("Lista ordenada:", s_sort(l))
