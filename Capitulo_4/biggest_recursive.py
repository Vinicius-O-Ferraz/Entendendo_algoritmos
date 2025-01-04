def biggest_rec(l:list, s = 0):
    
    if(len(l)== 1):
        return s
    
    else:
        if l[1] > s:
            s =  l[1]

        return(biggest_rec(l[1:],s))

l = [1,2,3,4,5,6]
print(biggest_rec(l))

e = [3,4,1,7,9,10,1,100]
print(biggest_rec(e))