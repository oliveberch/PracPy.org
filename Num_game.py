import random
n = random.randint(1, 9)
e = input("Enter any character to continue: \n")
count = 0
while e != "exit":
    c = int(input("Guess the number between 0 and 9: \n"))
    count += 1
    if c==n:
       print("You guesssed it right.")
    elif c<n:
       print("You guessed it too low.")
    elif c>n:
       print("You guessed it too high.")
    e = input("Enter 'exit' to leave game, and any other word to continue: \n")
    if e == "exit" :
        print("You took",count,"attempts to guess the number.")