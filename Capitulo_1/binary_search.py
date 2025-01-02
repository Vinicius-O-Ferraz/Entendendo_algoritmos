import time 
from math import floor

def b_search(list:list,element:any, etapas = 0):
    up, down = len(list) -1, 0

    while down <= up:
        middle = (down + up)//2 
        guess =  list[middle]

        if guess == element:
            print(f"Achamos {element} em {etapas} etapas")
            return middle
        
        if guess > element:
            etapas+=1
            up = middle - 1
        else:
            etapas+=1
            down = middle +1
    return None

lista = range(1,100000000) 

start = time.time_ns()
print(b_search(lista,128))
end = time.time_ns()

print(f"O tempo decorrido é de {(end - start)}s")