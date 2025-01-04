def rec_sum(l:list, s = 0):
    
    if(len(l)== 0):
        return s
    
    else:
        s = s + l[0]
        return(rec_sum(l[1:],s))

l = [i for i in range(1,5)]
print(rec_sum(l))