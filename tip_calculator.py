# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
# Write your code below this line 👇
print('Welcome to the tip calculator')
bill = float(input('what was the total bill? $ '))
tip_percentage = int(input('What percentage tip yuu would like to give? 10, 12, 0r 15 '))
total_people = int(input('How many people to split the bill? '))
tip = bill * (tip_percentage / 100)
total_bill = bill + tip
split = total_bill / total_people
print(f'Each person should pay ${split:.2f}')
