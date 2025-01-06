def sum_elements(l: list, s=0):
    # Caso base: Se a lista estiver vazia, retornamos a soma acumulada.
    if len(l) == 0:
        return s
    
    else:
        # Adicionamos o primeiro elemento da lista ao acumulador (s).
        s = s + l[0]

        # Chamamos a função recursivamente, excluindo o primeiro elemento da lista.
        return sum_elements(l[1:], s)

# Lista de exemplo
l = [1, 2, 3, 4, 5, 6]
print(sum_elements(l))  # Saída: 21
