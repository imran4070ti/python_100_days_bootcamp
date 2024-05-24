enimies = 1 # Global variable

def increase_enimies():
    enimies = 2 # Local variable
    print(f'Enimies inside the function is: {enimies}')


def num_of_enimies():
    print(f'Enimies inside another function is: {enimies}')

increase_enimies()
num_of_enimies()
print(f'Enimies outside the function is: {enimies}')

player_health = 10

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)
    drink_potion() # The drink_potion() is now Local Scope inside the function game(), that's why it can be called from inside the game() function.

# drink_potion() # But cannot be called directly outside from the game() function.

game()


