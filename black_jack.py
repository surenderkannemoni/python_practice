import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []

for c in range(2):
    user_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))

user = sum(user_cards)
computer = sum(computer_cards)
print(f' computer card = [{computer_cards[0]}, ?] and score {computer_cards[0]}')
print(f' user cards = {user_cards} and score {user} ')
program = True
while program:
    hit_stand = input('Do you want to hit (h) or stand (s)? ').lower()
    if hit_stand == 'h':
        user_cards.append(random.choice(cards))
        user = sum(user_cards)
        print(f' user cards = {user_cards} and score {user} ')
        if user > 21:
            print('Bust!\n Computer wins')
            program = False
        if user == 21:
            print(f'{computer_cards}\n {computer}')

    elif hit_stand == 's':
        if computer < 17:
            computer_cards.append(random.choice(cards))
            computer = sum(computer_cards)
            
        if (computer >= 17) and (computer <= 21):
            if computer > user:
                
                print(f' Computer wins')
            else:
                
                print(f' User wins {user}')
        if computer > 21:
            
            print(f'{computer}')
            print('Bust\n user wins')
        program = False
print(f'computer cards = {computer_cards}\n {computer}')
print(f' user cards = {user_cards} and score {user} ')



