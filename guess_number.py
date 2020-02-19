import random


number = random.randint(1, 20)

for number_of_time in range(1, 10):
    number_guessed = input('Guess a number?')
    number_guessed = int(number_guessed)
    
    if number_guessed < number:
        print('you are too low')
    elif number_guessed > number:
        print('you are too high!')
    else:
        break

if number_guessed == number:
    print('Found it!')
