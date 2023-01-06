
import random
number_to_guess = random.randint(0,10)
user_guess = 1
while number_to_guess != user_guess:
    user_guess = int(input("Guess a number: "))
    if number_to_guess > user_guess:
        print('Higher')
    elif number_to_guess < user_guess:
        print('Lower')
    else:        
        print('You Win!')


