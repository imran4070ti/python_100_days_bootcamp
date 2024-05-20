import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_']

options = [letters, digits, symbols]

n_letters = int(input('How many letters do you want? '))
n_digits = int(input('How many digits do you want? '))
n_symbols = int(input('How many symbols do you want? '))


password = ''

for i in range(n_letters):
    password+=(letters[random.randint(0, len(letters)-1)])
for i in range(n_digits):
    password+=(digits[random.randint(0, len(digits)-1)])
for i in range(n_symbols):
    password+=(symbols[random.randint(0, len(symbols)-1)])
new_password = ''
length = len(password)
is_used = []
i = 1
while i<=length:
    rand_idx = random.randint(0, length-1)
    if rand_idx not in is_used:
        new_password += password[rand_idx]
        is_used.append(rand_idx)
        i+=1
print(password)
print(new_password)


# Insted we can store the ordered letters, digits and symbols in a list and then use random.shuffle(list_name)
# to randomly shuffle the order of the items and then create string with those items.
# But to make it more challenging I wanted to do hard coding.




