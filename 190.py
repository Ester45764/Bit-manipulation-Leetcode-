def reversebits(n):
    l=0
    for  bit in range(31):
        if n&(1<<bit)!=0:
             l=l|(1<<(31-bit))
    return l
 
