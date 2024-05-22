letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def encrypt(plain_text, shift_number):
    cipher_text = ''
    for letter in plain_text:
        if letter in letters:
            idx = letters.index(letter)
            shifted_idx = idx + shift_number
            if shifted_idx > 25:
                shifted_idx = shifted_idx % 26
            cipher_text += letters[shifted_idx]
    return cipher_text

def decrypt(cipher_text, shift_number):
    plain_text = ''
    for letter in cipher_text:
        if letter in letters:
            idx = letters.index(letter)
            shifted_idx = idx - shift_number
            if shifted_idx < 0:
                shifted_idx = shifted_idx % 26
            plain_text += letters[shifted_idx]
    return plain_text


# def encode(plain_text, shift_number):
#     cipher_text = ''
#     while len(cipher_text) < len(plain_text):
#         for char in plain_text:
#             for i, letter in enumerate(letters):
#                 if char == letter:
#                     shifted_idx = i + shift_number
#                     if shifted_idx >25:
#                         shifted_idx = shifted_idx%26
#                     cipher_text += letters[shifted_idx]
#                     break 
#     return cipher_text  

# def decode(cipher_text, shift_number):
#     plain_text = ''
#     while len(plain_text) < len(cipher_text):
#         for char in cipher_text:
#             for i, letter in enumerate(letters):
#                 if char == letter:
#                     shifted_idx = i - shift_number
#                     if shifted_idx < 0:
#                         shifted_idx = shifted_idx % 26
#                     plain_text += letters[shifted_idx]
#                     break
#     return plain_text

while True:
    choice = input('Do you want to check again? Y or N ').upper()

    if choice == 'Y':
        plain_text = input('Enter your code in BLOCK letter: ').upper()
        print(f'Plain text code: {plain_text}')
        shift_number = int(input('Enter your shift number: '))

        encoded_text = encrypt(plain_text, shift_number)

        print(f'Encoded text: {encoded_text}')
        decoded_text = decrypt(encoded_text, shift_number)
        print(f'Decoded text: {decoded_text}')
    elif choice == 'N':
        print('Terminatting the program...!')
        break
    else:
        print('Invalid choice....!')