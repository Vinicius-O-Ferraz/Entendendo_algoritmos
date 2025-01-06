def rec_sum(l: list, s=0):
    # Caso base: Se a lista estiver vazia, retornamos a soma acumulada.
    if len(l) == 0:
        return s
    else:
        # Adicionamos o primeiro elemento da lista ao acumulador (s).
        s = s + l[0]
        # Chamamos a função recursivamente, excluindo o primeiro elemento da lista.
        return rec_sum(l[1:], s)

# Lista de exemplo gerada com números de 1 a 4.
l = [i for i in range(1, 5)]  # Resultado: [1, 2, 3, 4]
print(rec_sum(l))  # Saída: 10
