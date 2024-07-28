import pandas as pd

npa_df = pd.read_csv('day-30/nato_phonetic_alphabet/nato_phonetic_alphabet.csv')

npa_dict = {row.letter:row.code for idx,row in npa_df.iterrows()}
print(npa_dict)

# while True:
#     word = input('Enter a word: ').upper()
#     try:
#         code_words = [npa_dict[letter] for letter in word]
#     except KeyError:
#         print('Sorry, only letters in the alphabet please.')
#     else:
#         print(code_words)
#         break

def generate_phonetic():
    word = input('Enter a word: ').upper()
    try:
        code_words = [npa_dict[letter] for letter in word]
    except KeyError:
        print('Sorry, only letters in the alphabet please.')
        generate_phonetic()
    else:
        print(code_words)

generate_phonetic()