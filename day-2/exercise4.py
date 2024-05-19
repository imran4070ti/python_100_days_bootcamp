print('Welcome to tip calculator')
bill = input('What was the bill? ($) ')
tip = input('What percentage tip would you like to give? 10, 12 or 15? ')
person = input('How many people to split the bill? ')

total_bill = float(bill) + float(tip)/100*float(bill)
each_person_bill = total_bill/float(person)

print(f'Each person should pay: ${each_person_bill:.2f}')