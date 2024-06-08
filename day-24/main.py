import os

# Read the starting letter
with open('day-24/input/letters/starting_letter.docx') as starting_letter_file:
    starting_letter = starting_letter_file.read()

# Read the invided names
with open('day-24/input/names/invited_names.txt') as names_file:
    names = names_file.readlines()

invited_letter_dir = 'day-24/output/ready_to_send'
if not os.path.exists(invited_letter_dir):
    os.makedirs(invited_letter_dir)

for name in names:
    name = name.strip()
    final_letter_file_name = f'letter_for_{name}.docx'
    final_letter_path = os.path.join(invited_letter_dir, final_letter_file_name)
    final_letter = starting_letter.replace('[name]', name)
    with open(final_letter_path, 'w') as final_letter_file:
        final_letter_file.write(final_letter)
        print(f'Letter for {name} is created.')




