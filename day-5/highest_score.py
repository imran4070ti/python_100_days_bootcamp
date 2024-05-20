scores = input('Enter the student scores: ').split()

for i in range(len(scores)):
    scores[i] = int(scores[i].strip())

highest_score = 0
for score in scores:
    if score>highest_score:
        highest_score = score
print(f'The highest score is: {highest_score}')