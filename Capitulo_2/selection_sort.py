def smallest_search(lista):
    smallest, smallest_index = lista[0],0

    for i in range(1,len(lista)):
        if lista[i] < smallest:
            smallest, smallest_index = lista[i], i
    
    return smallest_index


def s_sort(lista):
    l = []
    for i in range(len(lista)):
        smallest = smallest_search(lista)
        l.append(lista.pop(smallest))
    return l

l = [i for i in range(100,0,-1)]
print(l)
print(s_sort(l))