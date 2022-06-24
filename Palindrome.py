def palindrome(s):
    ns = s[::-1]
    if ns==s:
        print("String entered is palindrome")
    else:
        print("String entered is not palindrome")
a = input("Enter a word to check weather it is palindroome or not: ")
palindrome(a)