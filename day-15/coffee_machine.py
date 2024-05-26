'''
A coffee machine project.
'''

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    'money': 0
}


def print_report():
    '''
    function to print resource report
    '''
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    money = resources['money']

    print(f'Water: {water}ml')
    print(f'Milk: {milk}ml')
    print(f'Coffee: {coffee}g')
    print(f'Money: ${money}')


def process_coins(coins):
    '''
    function to process the coins
    '''
    quarters = coins['quarters']
    dimes = coins['dimes']
    nickles = coins['nickles']
    pennies = coins['pennies']
    total = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    return total


def get_available_resources():
    '''
    get available resources
    '''
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    return water, milk, coffee


def check_availability(water, milk, coffee):
    '''
    check resources availability
    '''
    avail_water, avail_milk, avail_coffee = get_available_resources()

    if avail_water >= water and avail_milk >= milk and avail_coffee >= coffee:
        return True
    return False


def update_resources(water, milk, coffee):
    '''
    update the resources after delivering a coffee
    '''
    resources['water'] -= water
    resources['milk'] -= milk
    resources['coffee'] -= coffee


def buy(coins, coffee_type):
    '''
    check if the coffee is buyalbe or not.
    '''
    total = process_coins(coins)
    to_buy = MENU[coffee_type]
    cost = to_buy['cost']
    if total < cost:
        print("Sorry, that's not enough money. Money refunded.")
    else:
        if coffee_type == 'espresso':
            water = to_buy['ingredients']['water']
            coffee = to_buy['ingredients']['coffee']
            milk = 0
        else:
            water = to_buy['ingredients']['water']
            coffee = to_buy['ingredients']['coffee']
            milk = to_buy['ingredients']['milk']

        availability = check_availability(water, milk, coffee)

        if availability is True:
            refundable = total - cost
            update_resources(water, milk, coffee)
            print(f'Here is ${refundable:.2f} in change.')
            print(f'Here is your {coffee_type} ☕ Enjoy!')
        else:
            missings = []
            avail_water, avail_milk, avail_coffee = get_available_resources()
            if avail_water < water:
                missings.append('water')
            if avail_coffee < coffee:
                missings.append('coffee')
            if avail_milk < milk:
                missings.append('milk')
            printable = ""
            for i in range(len(missings) - 1):
                printable += f'{missings[i]}, '
            printable += f'{missings[-1]}.'
            print(f'sorry, there is not enough {printable}')


while True:
    choice = input('What would you like? (espresso/latte/cappuccino): ')
    choice = choice.lower()
    if choice == 'report':
        print_report()
    elif choice == 'quit':
        break
    else:
        if choice == 'espresso':
            coffee_type = 'espresso'
        elif choice == 'latte':
            coffee_type = 'latte'
        elif choice == 'cappuccino':
            coffee_type = 'cappuccino'
        else:
            print('Incorrect choice')
            continue

        coins = {
            'quarters': 0,
            'dimes': 0,
            'nickles': 0,
            'pennies': 0
        }

        coins['quarters'] = int(input('How many quarters? '))
        coins['dimes'] = int(input('How many dimes? '))
        coins['nickles'] = int(input('How many nickles? '))
        coins['pennies'] = int(input('How many pennies? '))

        buy(coins, coffee_type)

