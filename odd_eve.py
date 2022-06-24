n = int(input("Enter a number :"))
if (n%2) == 0:
    if (n%4) == 0:
        print("No. entered is Even and multiple of 4")
    else:
        print("No. entered is Even")
else:
    print("No. entered is Odd")