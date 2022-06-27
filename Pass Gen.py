#m1
import random
def main():
    pc = string.ascii_letters + string.digits + string.punctuation
    passlen = 4* int(input("ENTER 1,2,3 for Weak Regular Strong strength of password: "))
    password = ''.join(random.sample(pc,passlen))
    print ("Your Pass:",password)
    
# m2
import string
#import random
def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
    #print (chars)
    return ''.join(random.choice(chars) for _ in range(size))

print(pw_gen())