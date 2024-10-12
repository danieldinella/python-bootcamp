class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
    
    def next_question(self):
        item = self.question_list[self.question_number]
        self.question_number += 1
        user = input(f"Q.{self.question_number}: {item.text} (True/False): ")
        if self.check_answer(item.answer,user):
            self.score += 1
            print("You got it right!")
        else:
            print("Your answer is wrong!")
        print(f"Your actual score is {self.score}/{self.question_number}.\n\n")

    def still_has_question(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self, correct, user):
        return correct.lower() == user.lower()
