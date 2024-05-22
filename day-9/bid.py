import os
from logo import logo

print(logo)

bids = []

def take_bid():
    name = input('What is your name? ')
    amount = int(input('What is your bid? $ '))
    bid = {
        'name' : name,
        'amount' : amount
    }
    bids.append(bid)

def announce_winner():
    top_bidder = ""
    top_amount = 0
    for bid in bids:
        name = bid['name']
        amount = bid['amount']
        if amount > top_amount:
            top_bidder = name
            top_amount = amount
    print(f'The winner is {top_bidder} with a bid of ${top_amount}.')


take_bid()

while True:
    again = input('Is there any other bidders? Type "Y" or "N" ').upper()
    if again == "Y":
        os. system('clear')
        print(logo)
        take_bid()
    else:
        os. system('clear')
        print(logo)
        break


announce_winner()
