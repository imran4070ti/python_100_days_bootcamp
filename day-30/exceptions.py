'''
try:
    Executing someting that might cause an exception.
except:
    Do this if there was an exception in try block.
else:
    Do this if there were no exceptions.
finally:
    Do this no matter what happens. This block is always
    gonna be executed.
raise:
    Allows us to raise our own exceptions.
'''
try:
    file = open('day-30/a_file.txt')
    a_dictionaory = {'key':'value'}
    print(a_dictionaory['key'])
except FileNotFoundError:
    file = open('day-30/a_file.txt', 'w')
    file.write('Hello there, how are you?')
    file.close()
except KeyError as error_message:
    # print('Probably you are trying to access using wrong key')
    print(f'The key {error_message} does not exists')
else:
    content = file.read()
    print(content)
finally:
    # file.close()
    # print('File is closed.')
    raise KeyError('This is an error I made up.')




