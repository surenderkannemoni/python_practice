import random
print('Welcome to Knight Name generator')

def knight_name_generator():
      firstnames = input('Enter your name: ')
      nicknames = ["Brave", "Horrific", "Courageous", "Terrific", "Fair", "Conqueror", "Victorious", "Glorious",
                   "Invicible"]

      nickname = random.choice(nicknames)
      return firstnames + ' ' + "the" ' ' + nickname

run_program = True
while run_program:
    print(knight_name_generator())
    continue_program = input('Do you want to continue "y" or "n": ').lower()
    if continue_program == "n":
        run_program = False
        print('Good Bye!')
