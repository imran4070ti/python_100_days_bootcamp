'''
Here we are creating the QuizBrain class.
'''

from question_model import Question
from data import question_data


class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def next_question(self):
        question_idx =  self.question_number
        question = self.questions_list[question_idx]
        question_text = question.text
        question_answer = question.answer
        user_answer = input(f'Q.{question_idx + 1}: {question_text} (True/False)? ')
        self.check_answer(question_answer, user_answer)
        self.question_number += 1

    def check_answer(self, question_answer, user_answer):
        if question_answer.lower() == user_answer.lower():
            print('You got it right!')
            self.score+= 1
        else:
            print('You got it wrong!')
        print(f'The correct answer is {question_answer}')
        print(f'Your current score is: {self.score}/{self.question_number+1}')
    
    def get_score(self):
        return self.score
    
    def get_question_number(self):
        return self.question_number

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)
        