#This is a guess the number game
import random

print("Hello ; What is your name?")
name = input()

print('Well' + name + 'Im thinking of a number btw 1 - 20')

secretNumber = random.randint(1, 20)

#This is a for loop - Loop for 1-7 so 6 in total
for guesses_taken in range (1, 7):
    print('Take a guess:')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('your guess is too high')
    else:
        break #This condition is for the correct guess!

if guess == secretNumber:
    print('Good Job '+ name + 'You guessed my number in ' + str(guesses_taken))
else:
    print('Nope, the number i was thinking of was ' + str(secretNumber))

