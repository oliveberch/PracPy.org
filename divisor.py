#1

def divisor(n):
    for a in range(1,n):
        r = n%a
        if r == 0:
            print(a)
    return 0
n = int(input("Enter a no. to find all of its divisor: "))
divisor(n)

#2
# CAN BE DONE GENERATING LIST OF NUMBERS LESS THAN NUMBER ENTERED