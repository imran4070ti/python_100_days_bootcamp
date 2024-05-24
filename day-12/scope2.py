# If a variable is created inside a condition or loop block,
# it can be accessed directly from outside of the block.
# But if created inside a function, it cannot be accessed form outside of that function.



enemies = ['Skeleton', 'Zombie', 'Alien']

game_level = 3

# if game_level < 5:
#     new_enemies = enemies[0]
# print(new_enemies) # Can be accessed even if new_enemies declared inside an if block

def create_enemy():
    if game_level < 5:
        new_enemies = enemies[0] # Cannot be accessed form outside of the function. Because it is inside a local scope.

# print(new_enemies) # Cannot be accessed