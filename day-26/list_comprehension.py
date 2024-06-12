import random

students = ['A', 'B', 'C', 'D']

students_score = {student:random.randint(1, 100) for student in students}
print(students_score)

passed_students = {student:score for student, score in students_score.items() if score>50}
print(passed_students)