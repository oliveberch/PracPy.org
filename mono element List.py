def monoList(l):
    for i in l:
        j= i+1
        for j in l:
            a,b =l(i),l(j)
            if a == b:
                l.remove(b)
    return(l)
a=[1,2,4,5,2,5,1,6,4,7]
print(monoList(a))