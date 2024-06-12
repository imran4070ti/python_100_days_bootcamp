sentence = 'The quick bround fox has jumped over the lazy dog'

char_freq = {word:len(word) for word in sentence.split(' ')}

print(char_freq)