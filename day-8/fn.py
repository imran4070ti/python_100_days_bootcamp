def greet(name):
    print(f'Hello, {name}')
    print('How do you do?')
    print('How is the weather?')

def greet_with(name, location):
    print(f'Hello, {name}')
    print(f'How is the weather in {location}')

# greet(name='Imran') # parameter -> name, argument -> 'Imran'

greet_with('Imran', 'Rangpur') # Positional arguments
print()
greet_with('Rangpur', 'Imran') # Positional arguments
print()
greet_with(location='Rangpur', name='Imran') # Keyword arguments

