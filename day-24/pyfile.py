
# No need to close the file if we open it using 'with'
with open('day-24/file.txt') as file: 
    text = file.readline()
    print(text)

# with open('day-24/file.txt', 'w') as file:
#     file.write('Hello there... New texts.')

with open('day-24/file.txt', 'a') as file:
    file.write('\nHello there... New texts 1.')
    file.write('\nHello there... New texts 2.')




# open('file.txt') -> Read only
# open('file.txt', 'r') -> Read only
# open('file.txt', 'w') -> write
# open('file.txt', 'a') -> Append
# file.read() -> whole text file as a single paragraph
# file.readline() -> only the first line
# file.readlines() -> all the lines in a list


