
def energy_rating(lumens,power_consumption):
    efficient_ratio = lumens / (power_consumption /1000)
    if efficient_ratio > 210:
        print('Energy Rating  is "A"')
    elif efficient_ratio > 210:
        print('Energy Rating  is "A"')
    elif efficient_ratio > 185:
        print('Energy Rating  is "B"')
    elif efficient_ratio > 160:
        print('Energy Rating  is "C"')
    elif efficient_ratio > 135:
        print('Energy Rating  is "D"')
    elif efficient_ratio > 110:
        print('Energy Rating  is "E"')
    elif efficient_ratio > 85:
        print('Energy Rating  is "F"')
    elif efficient_ratio < 85:
        print('Energy Rating  is "G"')
    else:
        print('Invalid Input')
    


run_program = True
while run_program:
    lumens = int(input('Enter your bulb output in lumens: '))
    power_consumption = int(input('Enter your power consumption in kw: '))
    energy_rating(lumens,power_consumption)
    
    



