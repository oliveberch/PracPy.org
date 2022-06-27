import random

def cnb(a,b):
        ans = [0,0]
        for i in range(0,3):
            if a[i] == b[i]:
              ans[1]+=1
            else:
              ans[0]+=1    
        return ans


if __name__=="__main__":
    n = random.randint(1000,9999)
    playing = True
    guesses = 0
    
    while playing:
        #getting user guess
        g = input("GUESS THE FOUR DIGIT NUMBER: ")
        #getting number of cows and bulls
        cowbullcount = cnb(str(n),str(g))
        guesses+=1

        print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

        if cowbullcount[1]==4:
            playing = False
            print("You win the game after " + str(guesses) + "! The number was "+str(n))
            break #redundant exit
        else:
            print("Your guess isn't quite right, try again.")
            
        to_exit = input("Enter exit to leave game.")
        #exiting when user wants
        if to_exit == "exit":
            print("O|<! The number was "+str(n))
            break
    
    
    
