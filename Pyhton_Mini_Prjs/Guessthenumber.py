# This is a guess the number game.
import random #Random module

print('Hello, What is your name?')
name = input()

print('Well, ' + name + ' , I am thinking  of a number between 1 and 20, can you guess it?')
secretnumber = random.randint(1, 20)

for guessestaken in range(1, 7):
    print('Take a guess')
    guess = int(input())

    if guess < secretnumber:
       print('Nope, Thats too low.')
    elif guess > secretnumber:
        print('Nope, Thats too high.')
    else:
        break # This condition is for the correct guess.

if guess == secretnumber:
    print('Gj lil ' + name + '!, You guessed my number in ' + str(guessestaken) + ' guesses!')
else:
    print('6 guesses used, the number was ' + str(secretnumber) + ' Rookie.')
          
    
