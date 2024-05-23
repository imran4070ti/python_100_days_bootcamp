import random
import os
from logo import logo


cards_dict = {
    'A':11, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10
}

cards = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

def is_blackjack(cards, score):
    if len(cards) == 2 and score == 21:
        return True
    return False

def add_score(user, score, choice):
    if choice is 'A' and score + 11 > 21:
        if user == 'player':
            to_add = input('Type "1" to add 1 or type "11" to add 11: ')
            if to_add is '1':
                score+=1
            elif to_add is '11':
                score += 11
        elif user == 'computer':
            if score + 11 > 21:
                score += 1
            else:
                score += 11
    else:
        score+=cards_dict[choice]
    return score

def print_score(your_cards, your_score, computer_cards):
    print(f'Your cards: {your_cards}, current score: {your_score}')
    if len(computer_cards) == 1:
        print(f"Computer's first card: {computer_cards[0]}")
    else:
        print(f"Computer's cards: {computer_cards}")

def print_final_hand(your_cards, your_score, computer_cards, computers_score):
    print(f'Your final hand: {your_cards}, final score: {your_score}')
    print(f"Computer's final hand: {computer_cards}, final score: {computers_score}")

def print_result(your_score, computers_score):
    if computers_score > 21:
        print('You won!')
    elif your_score > 21:
        print('Computer won!')
    elif computers_score < your_score:
        print('You won!')
    elif computers_score == your_score:
        print('Draw')
    else:
        print('Computer won!')


restart = True

while restart:
    print(logo)
    your_cards = [random.choice(cards), random.choice(cards)]
    your_score = 0

    for card in your_cards:
        your_score+=cards_dict[card]

    print(f'Your cards: {your_cards}, current score: {your_score}')

    computer_cards = [random.choice(cards)]
    print(f"Computer's first card: {computer_cards[0]}")
    computers_score = 0
    for card in computer_cards:
        computers_score+=cards_dict[card]

    while True:
        if is_blackjack(your_cards, your_score):
            print('Your Blackjack!!') 
        choice = input('Type "y" to get another card, type "n" to pass: ').lower()
        if choice == 'n':
            print_score(your_cards, your_score, computer_cards)
            while computers_score<17:
                if is_blackjack(computer_cards, computers_score):
                    print("Computer's Blackjack!!") 
                next_card = random.choice(cards)
                computer_cards.append(next_card)
                computers_score = add_score('computer', computers_score, next_card)
            print_final_hand(your_cards, your_score, computer_cards, computers_score)
            print_result(your_score, computers_score)
            break
            
        elif choice == 'y':
            your_next = random.choice(cards)
            your_cards.append(your_next)
            your_score = add_score('player', your_score, your_next)
            print_score(your_cards, your_score, computer_cards)
            computer_next = random.choice(cards)
            computer_cards.append(computer_next)
            computers_score = add_score('computer', computers_score, computer_next)
            if your_score > 21:
                print_result(your_score, computers_score)
                print_final_hand(your_cards, your_score, computer_cards, computers_score)
                break
        else:
            print('Invalid choice')
    
    play_again = input('Do you want to start over? "yes" or "no": ')
    if play_again == 'yes':
        os.system('clear')
        restart = True
    elif play_again == "no":
        restart = False
    else:
        print('Invalid Choice!')
        os.system('claer')
        restart = True
    
        


        
