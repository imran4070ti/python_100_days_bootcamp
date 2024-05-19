age = input('Enter your age: ')
remaining_age = 90 - int(age)
weeks = remaining_age * 52
days = remaining_age * 365
months = remaining_age * 12

print(f'You have {days} days, {weeks} weeks and {months} left.')
