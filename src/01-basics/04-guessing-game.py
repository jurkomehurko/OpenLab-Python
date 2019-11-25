import random

random_number = random.randint(1, 20)

guess = int(input('Guess a number 1 to 20: '))
while True:
    if random_number > guess:
        guess = int(input('Your guess is too low. Try again: '))
    elif random_number < guess:
        guess = int(input('Your guess is too high. Try again: '))
    else:
        print('You\'ve guessed the right number!')
        break
