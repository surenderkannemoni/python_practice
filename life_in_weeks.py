# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

max_age = 90
run_program = True
def life_in_weeks():
    remaining_years = max_age - age
    days = remaining_years * 365
    weeks = remaining_years * 52
    months = remaining_years * 12
    print(f'You have {days} days, {weeks} weeks, and {months} months left.')
while run_program:
    age = int(input('What is your current age? '))
    life_in_weeks()
    ask = input("Do you want continue? type 'y' for yes and 'n' for no ").lower()
    if ask == 'n':
        print('Good Bye!')
        run_program = False



