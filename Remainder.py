import math
n1 = int(input("Enter two numbers :"))
n2 = int(input(""))
r1 = math.remainder(n2,n1)
print(r1)
r2 = n2%n1
print(r2)
if n2%n1 == 0:
    print("Second number is perfectly divided by first number")
else:
    print("Second number leaves a remainder",r1,"or",r2,"when divided by first number")