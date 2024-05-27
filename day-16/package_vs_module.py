'''
In this section we are going to learn about
the differences between modules and packages
'''

# Module -> Modules are codes that are written in our own project.
# Package -> A package is a whole bunch of code that other people have written
# on a specific purpose.

# pypi -> python package index is the source of lots of packages.


from prettytable import PrettyTable


fruits = PrettyTable()

# fruits.border = False
# fruits.header = False
print(fruits.align)
fruits.align = "l"
print(fruits.align)

fruits.add_column('Id', [1, 2, 3, 4, 5])
fruits.add_column('Name', ['Apple', 'Banana', 'Orange', 'Watermelon', 'Guava'])
fruits.add_column('Price', [20, 10, 25, 50, 15])

print(fruits)
