import random

logo = '''
 {}    {}    {}{}     {}    {}    {}}}}}    {}      {}    {}{}     {}    {}
 {}    {}   {}  {}    {}}}  {}   {}    {}   {}}}  {{{}   {}  {}    {}}}  {}
 {}{{}}{}  {}{{}}{}   {} {} {}   {}         {} {{}} {}  {}{{}}{}   {} {} {}
 {}    {}  {}    {}   {}  {{{}   {}  {{{{   {}  {}  {}  {}    {}   {}  {{{}
 {}    {}  {}    {}   {}    {}    {}}}}}    {}      {}  {}    {}   {}    {}
'''

print(logo)

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']



def replace_character(word, char, idx):
    word_left = word[:idx]
    word_right = word[idx+1:]
    return word_left + char + word_right


words = ['mango', 'banana', 'guava', 'jackfruit', 'apple', 'orange', 'watermelon']

word = random.choice(words)
word_cpy = word
length = len(word)
guess = '*'*length


i = 0
flag = False
while i<7:
    print(f'Guessed word: {guess}')
    if guess == word:
        flag = True
        break
    letter = input('Guess a letter: ').lower()
    if letter in word_cpy:
        while letter in word_cpy:
            idx = word_cpy.index(letter)
            guess = replace_character(guess, letter, idx)
            word_cpy = replace_character(word_cpy, '*', idx)
    else:
        print(stages[i])
        i+=1
        # print(f'You have {7 - i} attempts left.')


if flag:
    print('Well done! You guessed the word.')
else:
    print('You failed.')
    
