a = int(input('Enter a numerator for frist fraction: '))
b = int(input('Enter a denominator for frist fraction: '))
print(f'First fraction {a}/{b}' )
c = int(input('Enter a numerator for second fraction: '))
d = int(input('Enter a denominator for second fraction: '))
print(f'second fraction {c}/{d}' )

if a*d > b*c:
    print(f'{a}/{b} > {c}/{d}  = {a}/{b} is Greater')
else:
    print(f'{a}/{b} > {c}/{d}  {c}/{d} is Greater')
