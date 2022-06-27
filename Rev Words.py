def Reverse(lst):
    new_lst = lst[::-1]
    return new_lst

def revword():
    a = input("Enter a long string: ")
    sal = a.split()
    ral = Reverse(sal)
    ra = " ".join(ral)
    print(ra)

revword()