import random 
n = random.randint(0,9)
guess = int(input("Enter an integer from 0 to 9: "))

if guess < n:
    print "guess is low"
elif guess > n:
    print "guess is high"
else:
    print "you guessed it!"
