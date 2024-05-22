import os
# os.system('clear')


# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def sub(n1, n2):
    return n1 - n2

# Multiplication
def mul(n1, n2):
    return n1 * n2

# Division
def div(n1, n2):
    return n1 / n2


operations = {
    '+' : add,
    '-' : sub,
    '*' : mul,
    '/' : div
}


num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
for symbol in operations:
    print(symbol)

operation = input('Which operation do you want? ')

calculation_function = operations[operation]
answer = calculation_function(num1, num2)
print(f'{num1} {operation} {num2} = {answer}')

while True:
    choice = input('Do you wnat another operation? "Y" or "N" ').upper()
    if choice == "Y":
        operation = input("What's the next operation? ")
        next = int(input('What is the next number? '))
        calculation_function = operations[operation]
        old_ans = answer
        answer = calculation_function(answer, next)
        print(f'{old_ans} {operation} {next} = {answer}')
    else:
        # os.system('clear')
        print(f'Final Result: {answer}')
        break

