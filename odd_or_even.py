print('Welcoe to odd or even progranm')
number = int(input('Which number do you want to check? '))

if number % 2 == 0:
    print(f' This {number} is an even number.')
elif number % 2 != 0:
    print(f' This {number} is an odd number.')
else:
    print('Invalid Input')

