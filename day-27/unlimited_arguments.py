# limited arguments
def add (n1, n2):
    return n1 + n2

# unlimited arguments / unlimited positional arguments
# *args is basically a tuple
def add(*args):
    print(args[-1]) # access by position
    sum = 0
    for n in args:
        sum+=n
    return sum

print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))