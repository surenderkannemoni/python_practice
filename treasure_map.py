print('welcome to Treasure Map')
row_1 = ['⬜️', '⬜️', '⬜️']
row_2 = ['⬜️', '⬜️', '⬜️']
row_3 = ['⬜️', '⬜️', '⬜️']
print(f'{row_1}\n{row_2}\n{row_3}')
rows = [row_1,row_2,row_3]
# print(rows[2][2]).
number = input('Enter the column ')
first_digit = int(number[0])
second_digit = int(number[1])
if number:
    rows[second_digit-1][first_digit-1] = 'X'

# print(f'{row_1}\n{row_2}\n{row_3}')
print(f'{row_1}\n{row_2}\n{row_3}')



