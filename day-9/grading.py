students_scores = {
    'Harry' : 90,
    'Ron' : 78,
    'Hermione' : 99,
    'Draco' : 74,
    'Neville' : 62
}


def score2grades(scores):
    for item in scores.items():
        key = item[0]
        value = item[1]

        if value > 90:
            scores[key] = 'Outstanding'
        elif value > 80:
            scores[key] = 'Exceeds Expectations'
        elif value > 70:
            scores[key] = 'Acceptable'
        else:
            scores[key] = 'Fail'
    return scores

student_grades = score2grades(students_scores)
print(student_grades)