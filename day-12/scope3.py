# Modifying Global Scope
enemies = 1

# def increase_enemies():
#     global enemies # If we do so, then we can modify the enemies variable and it will not show the following error.
#     enemies += 1 # UnboundLocalError: cannot access local variable 'enemies' where it is not associated with a value.
#     print(f'Enemies inside the function is: {enemies}')

# increase_enemies()
print(f'Enemies outside the function is: {enemies}')


# We don't modify the global variable inside a function often.
# Insted we can use a return statement to update/modify the value of the global variable.

def increase_enemies():
    return enemies + 1

enemies = increase_enemies()
print(f'Enemies outside the function after increased is: {enemies}')