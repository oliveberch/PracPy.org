#return a list that has common elements of both lists in it,
#without duplicates.

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#c = []
#for A in a:
#    for B in b:
#        if A == B:
#            n=0
#            for C in c:
#                if A == C:
#                    n+=1
#            if n ==0:
#                c.append(A)
#for C in c:
#    print(C)

#generate random list to test your code.
#
import random
a=[]
b=[]
c=[]
for n in range(0, random.randint(10,20)):
    A = random.randint(1, 99)
    a.append(A)
for n in range(0, random.randint(10,20)):
    B = random.randint(1, 99)
    b.append(B)
for A in a:
    for B in b:
        if A == B:
            n=0
            for C in c:
                if A == C:
                    n+=1
            if n ==0:
                c.append(A)
for C in c:
    print(C)