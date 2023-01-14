import random
upper_case_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower_case_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-']

password = []
password_actual = []

def random_generator(password_length):
    for i in range(password_length):
        password.append(random.choice(upper_case_letters))
        password.append(random.choice(lower_case_letters))
        password.append(random.randrange(0, 10))
        password.append(random.choice(symbols))
    for p in range(password_length):
        password_actual.append(random.choice(password))
        print(password_actual[p], end='')


run_program = True
while run_program:
    password_length = int(input('Password Length '))
    random_generator(password_length)
    should_continue = input('\nDo you want to generate again? type "y" or "n" ')
    if should_continue == 'n':
        run_program = False
        








