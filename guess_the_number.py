import random

print('Welcome to the number Guessing game')
print("I'm thinking of a number between 1 and 100")
# guessed number 5

number = random.randint(0, 100)

difficulty = input('Choose a difficulty. Type "easy" or "hard": ')
attempts = 10
if difficulty == 'hard':
    attempts = 5


def calculate():
    global attempts

    if make_a_guess > number:
        print('Too High\nGuess Again')

    elif make_a_guess < number:
        print('Too Low\nGuess Again')
    print(f' You have {attempts}  attempts to guess the number b')
    attempts += -1


run_program = True
while run_program:
    make_a_guess = int(input('Make a guess: '))
    if attempts == 0:
        print('your have no attempts left')
        run_program = False

    if make_a_guess == number:
        print('You Guessed the right number')
        run_program = False
    else:
        calculate()

