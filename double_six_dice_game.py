import random
import art
print(art.logo)



player_one = input('Enter player one name: ')
player_two = input('Enter player two name: ')
number = 6
counter1 = 0
counter2 = 0
run_program1 = True

while run_program1:
    dice_1 = random.randint(0,6)    
    if dice_1 != number:
        counter1 += 1
        
    elif dice_1 == number:
        
        run_program1 = False
run_program2 = True
while run_program2:
    dice_2 = random.randint(0,6)      
    if dice_2 != number:
        counter2 += 1        
    elif dice_2 == number:       
        run_program2 = False
print(f'{player_one} diced {counter1}')
print(f'{player_two} diced {counter2}')
if counter1 > counter2:
    print(f'{player_two} wins')
elif player_one < player_two:
    print(f'{player_one} wins')
else:
    print('Draw')
    

    
