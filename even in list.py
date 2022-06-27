# 1 list out even elements of a given list and make new one from those elements:
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = []
for A in a:
    if A%2 == 0:
        b.append(A)
print(b)

# 2 Write same code in a line ;-)

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [n for n in a if n%2 == 0]
print(b)