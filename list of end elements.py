# Take a list input and print new list with only first and last elements.
a = [int(i) for i in input("ENTER THE ELEMENTS OF FIRST LIST: ").split()]
b =[a[0],a[len(a)-1]]
print("NEW LIST: ", b)