fruits = ['Apple', 'Pear', 'Orange']


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError as error_message:
        print('Fruit pie')
    else:
        print(fruit + " pie")
    finally:
        print('Your pie is made.')

make_pie(4)