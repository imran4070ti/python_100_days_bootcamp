print('Welcome to the rollercoster!!!')
height = int(input('Enter your height in cm: '))
bill = 0
if height >=120:
    print("You can ride the rollercoster!")
    age = int(input('Enter your age: '))
    if age>=45 and age <=55:
        print('You can ride for free!')
    elif age>=18:
        print("Adult ticket $12.")
        bill += 12
    elif age<12:
        print("Child ticket $5.")
        bill += 5
    else:
        print("Youth ticket $7.")
        bill += 7

    photo_taken = input('Do you want to take a photo? Y or N ')
    if photo_taken == 'Y':
        bill += 3
    print(f'Your total bill is ${bill:.2f}')

else:
    print("Sorry....! You are unable to ride rollercoster.")