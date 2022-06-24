a =["mark",44,"samuel",34.6,'g',65,"kethey",2.1,'d']
b =["samuel",19,'w',2.3,34,'g',"nina",65]
c =[]
for A in a:
    for B in b:
        if A == B:
            c.append(A)
for C in c:
    print(C)
    
#2
# WRITE SAME IN ONE LINE....  :||
print([k for k in {*(int(i) for i in input().split())}.intersection({*(int(i) for i in input().split())})])