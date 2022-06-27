
#METHOD 1: LOOP and LIST
def fibN(n):
    n1,n2 = 0,1
    fib=[n1,n2]
    for a in range(1,n-1):
        n3= n2+n1
        fib.append(n3)
        n1,n2=n2,n3
    return(fib)
print(fibN(int(input("ENTER THE NUMBER OF TERMS TO PRINT FIBNOCCI SERIES."))))

#METHOD 2: RECURSIVE FUNCTION
def fibN2(n):
    n1,n2 = 0,1
    fib=[n1,n2]
    
    return


# METHOD 3: 
total = int(input("ENTER THE NUMBER OF TERMS TO PRINT FIBNOCCI SERIES."))
fib = [0, 1]
for i in range(1, total):
    fib.append(fib[i] + fib[i-1])
print(fib[1:total+1])

