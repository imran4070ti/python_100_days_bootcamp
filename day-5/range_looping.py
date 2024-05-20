a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
sum = 0
for i in range(a, b+1):
    sum += i

print(f'Sum of the all numbers is {sum}')