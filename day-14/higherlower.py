# import necessary modules
import random
import os
from game_data import data
from logo import logo, vs

# display the logo
print(logo)

# declare necessary functions
def get_name(celeb):
    return celeb['name']
def get_description(celeb):
    return celeb['description']
def get_follower_count(celeb):
    return celeb['follower_count']
def get_country(celeb):
    return celeb['country']
def get_info(celeb):
    return get_name(celeb), get_description(celeb), get_follower_count(celeb), get_country(celeb)
def choose_and_compare(celeb1, celeb2):
    name1, des1, followers1, country1 = get_info(celeb1)
    name2, des2, followers2, country2 = get_info(celeb2)

    print(f'Compare A: {name1}, {des1}, from {country1}.')
    print(vs)
    print(f'Compare B: {name2}, {des2}, from {country2}.')

    choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    if choice == 'A':
        if followers1>followers2:
            return True
        return False
    elif choice == 'B':
        if followers2 > followers1:
            return True
        return False
    else:
        print('Invalid choice! Choose Again....')
        choose_and_compare(celeb1, celeb2)


def get_celebrity():
    length = len(data)
    idx_celeb = random.randint(1, length) - 1
    celeb = data[idx_celeb]
    return celeb

def play():
    celeb1 = get_celebrity()
    celeb2 = get_celebrity()
    while celeb1 == celeb2:
        celeb2 = get_celebrity()
    score = 0
    while True:
        result = choose_and_compare(celeb1, celeb2)
        if result == True:
            score+=1
            temp = celeb1
            celeb1 = celeb2
            celeb2 = get_celebrity()
            while celeb2 == temp:
                celeb2 = get_celebrity()
            print(f'You are right! Current score {score}')
        else:
            os.system('clear')
            print(logo)
            print(f'Sorry, that is wrong. Final score {score}')
            break

play()

