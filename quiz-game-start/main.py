from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for q in question_data:
    question_bank.append(Question(q["question"], q["correct_answer"]))

brain = QuizBrain(question_bank)

while brain.still_has_question():
    brain.next_question()

print("You've completed the quiz.")
print(f"Your final score is {brain.score}/{brain.question_number}!")