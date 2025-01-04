def rec_sort(l):
    if len(l) < 2:
        return l
    else:
        pivo = l[0]
        menores = [ i for i in l[1:] if i <= pivo]
        maiores = [ i for i in l[1:]  if i > pivo]
        return rec_sort(menores) + [pivo] + rec_sort(maiores)
    
l = [3,4,1,7,9,10,1,100]
print(rec_sort(l))