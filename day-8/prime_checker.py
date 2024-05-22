import math

def is_prime(num):
    if num<2:
        return False
    elif num == 2:
        return True
    else:
        for i in range (2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    


number = int(input('Enter any positive integer: '))

if is_prime(number):
    print(f'{number} is Prime.')
else:
    print(f'{number} is not Prime.')
