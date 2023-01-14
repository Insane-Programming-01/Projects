# IMporting Requirements

import random

# Initialize variables

count = 1
over = False

number = random.randint(1,21)

def check(guess):

    global count

    if guess == number:
        print(f'\nYou Won in {count} chances!')
        global over
        over = True
    
    else:

        if guess < number:
            print('\nYour guess is low')
        elif guess > number:
            print('\nYour guess is high!')
        
        print(f'You have {5 - count} chances left')
        count += 1
    
    if count > 5:
        print(f'\nYou Lose!, Number was {number}')

        over = True


while not over:

    guess = int(input(f'\nGuess {count} - '))

    if guess < 1 or guess > 20:
        print('Your guess is invalid')
    else:
        check(guess)