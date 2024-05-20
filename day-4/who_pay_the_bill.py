import random

names = input('Enter the name of everyone seperated by comma: ')
names = names.split(',')
idx = random.randint(0, len(names)-1)

will_pay = names[idx]
print(f'Bill will be paid by {will_pay.strip()}')

will_pay = random.choice(names)
print(f'Bill will be paid by {will_pay.strip()}')
