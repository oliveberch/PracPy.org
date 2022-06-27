def divisor(n):
    div = []
    for a in range(1,n):
        r = n%a
        if r == 0:
            div.append(a)
    return div

def prime(n):
    div = divisor(n)
    if len(div) <= 1:
        print("NUMBER ENTERED IS PRIME.")
    else:
        print("NUMBER ENTERED IS NOT PRIME.")

n = int(input("ENTYTER A NUMBER TO CHECK IT'S PRIME OR NOT: \n"))
prime(n)
