def rec_sort(l):
    # Caso base: Se a lista tiver menos de dois elementos, ela já está ordenada.
    if len(l) < 2:
        return l
    else:
        # Escolhemos o primeiro elemento como pivô.
        pivo = l[0]

        # Criamos uma lista com os elementos menores ou iguais ao pivô.
        menores = [i for i in l[1:] if i <= pivo]

        # Criamos uma lista com os elementos maiores que o pivô.
        maiores = [i for i in l[1:] if i > pivo]

        # Ordenamos recursivamente as sublistas e as concatenamos com o pivô.
        return rec_sort(menores) + [pivo] + rec_sort(maiores)

# Lista de exemplo
l = [3, 4, 1, 7, 9, 10, 1, 100]
print(rec_sort(l))  # Saída: [1, 1, 3, 4, 7, 9, 10, 100]
