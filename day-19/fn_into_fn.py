def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1//n2

def calculator(n1, n2, func):  # Higher order function
    return func(n1, n2)


print(calculator(10, 5, subtract))