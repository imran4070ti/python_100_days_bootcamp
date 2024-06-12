import pandas as pd

npa_df = pd.read_csv('day-26/nato_phonetic_alphabet.csv')

npa_dict = {row.letter:row.code for idx,row in npa_df.iterrows()}
print(npa_dict)


word = input('Enter a word: ').upper()

code_words = [npa_dict[letter] for letter in word]
print(code_words)