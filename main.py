from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain

question_bank = []

for question in question_data:
    question_text = question['question']
    question_ans = question['correct_answer']
    new_question = Question(question_text, question_ans)
    question_bank.append(new_question)

quiz = QuizzBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()


print("You've completed the quiz successfully!!!")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
