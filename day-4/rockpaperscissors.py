import random


rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''

choices = [rock, paper, scissors]

your_choice = int(input('What do you want to choose? Type 0 for Rock, 1 for Paper, 2 for Scissors. '))
computer_choice = random.randint(0, 2)

print(f'You choose: {choices[your_choice]}')
print(f'Computer choose: {choices[computer_choice]}')
if your_choice >=3:
    print('Invalid choice')
elif your_choice ==  computer_choice:
    print('DRAW')
elif your_choice == 0 and computer_choice == 1:
    print('Computer WON')
elif your_choice == 0 and computer_choice == 2:
    print('You WON')
elif your_choice == 1 and computer_choice == 0:
    print('You WON')
elif your_choice == 1 and computer_choice == 2:
    print('Computer WON')
elif your_choice == 2 and computer_choice == 0:
    print('Computer WON')
elif your_choice == 2 and computer_choice == 1:
    print('You WON')



