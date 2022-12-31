print("Welcom to days in month")
# Create a program of leap y

def is_leap():
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
def days_in_month(year,month):
    if is_leap() and month == 2:
       month_days[1] = 29
       print(month_days[month -1])
        
    else:
        print(month_days[month -1])

run_program = True
while run_program:
    year = int(input('Enter a year: '))
    month = int(input('Enter a month: '))
    days_in_month(year,month)
    should_continue = input("Do you want to continue? type 'y' for yes and 'n' for no ").lower()
    if should_continue == 'n':
        print('Good Bye!')
        run_program = False




        



   
        
