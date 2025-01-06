def biggest_rec(l: list, s=0):
    # Caso base: Se a lista tiver apenas um elemento, retornamos o maior número encontrado até agora.
    if len(l) == 1:
        return s
    
    else:
        # Comparação do segundo elemento da lista com o maior valor atual (s).
        if l[1] > s:
            s = l[1]  # Atualizamos s com o novo maior valor encontrado.

        # Chamamos a função recursivamente, excluindo o primeiro elemento da lista.
        return biggest_rec(l[1:], s)

# Lista de exemplo 1
l = [1, 2, 3, 4, 5, 6]
print(biggest_rec(l))  # Saída: 6

# Lista de exemplo 2
e = [3, 4, 1, 7, 9, 10, 1, 100]
print(biggest_rec(e))  # Saída: 100
