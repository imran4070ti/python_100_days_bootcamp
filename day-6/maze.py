# Solution 1

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# loop_count = 0
# while not at_goal():
#     if loop_count >=4:
#         turn_left()
#     if right_is_clear():
#         turn_right()
#         move()
#         loop_count+=1
        
#     elif front_is_clear():
#         move()
#         loop_count=0
#     else:
#         turn_left()
#         loop_count=0



# Solution 2

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# while front_is_clear():
#     move()
# turn_left()
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()
