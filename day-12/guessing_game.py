import random

print('Welcome to the Number Guessing Game!')
print('I am thinking of a number between 1 to 100.')
random_number = random.randint(1, 100)

def make_guess():
    guess = int(input('\tMake a guess: '))
    return guess


def play(difficulty):
    if difficulty == "hard":
        attempts = 5
    elif difficulty == "easy":
        attempts = 10

    while attempts > 0:
        guess = make_guess()
        if guess == random_number:
            return True
        elif guess > random_number:
            print('\tToo high!')
        else:
            print('\tToo low!')

        attempts -= 1
        print('\tGuess again.')
        print(f'\tYou have {attempts} attemps remaining to guess the number.')
    return False


difficulty = input('Choose difficulty. "easy" or "hard": ').lower()
success = play(difficulty)

if success:
    print('\t\tCongratulations!! You guessed the correct number!')
else:
    print('\t\tSorry! You failed to guess the correct number!')
    print(f'\t\tThe number was {random_number}')

