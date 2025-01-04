def rec_sum(l:list, s = 0):
    
    if(len(l)== 0):
        return s
    
    else:
        s = s + 1
        return(rec_sum(l[1:],s))

l = [1,2,3,4,5,6]
print(rec_sum(l))