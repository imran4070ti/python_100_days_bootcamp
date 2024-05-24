##################### Debugging ######################

# # 1. Describe Problem
# def my_function():
#     for i in range(1, 20):
#         if i == 20: # i never reaches to 20 (1 to 19)
#             print('You got it')
# my_function()


# # 2. Reproduce the bug
# import random

# dice_numbers = [1, 2, 3, 4, 5, 6]
# dice_num = random.randint(1, 6) # Can produce random number in range [1, 6], but index in dice_numbers are [0, 6]
# print(dice_numbers[dice_num])


# # 3. Play Computer
# # Here if the year is 1994, none of the condition will be true.
# year = int(input("What's your year of birth? "))
# if year > 1980 and year<1994:
#     print('You are a millenial.')
# elif year>1994:
#     print('You are a Gen Z.')


# # 4. Fix an error
# age = input('Inpur your age? ')
# if age >= 18: #Comparison between string and integer
# print('Your age is: {age}.') # Indentation problem and formatting problem. But for the formatting problem you won't get any error in running the code.


# # 5. Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input('Number of pages: '))
# word_per_page == int(input('Number of words per page: ')) # Assignment operator error

# total_words = pages * word_per_page
# print(total_words)


# # 6. Use a Debugger
# def mutate (a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item*2
#     b_list.append(new_item) # only the last new_item value will append.
#     print(b_list)

# mutate([1, 2, 3, 5, 8, 13])


# 7. Take a break, Relax your brain and back later.
# 8. Ask a friend.
# 9. Run Often (small block)
# 10. Ask StackOverflow



