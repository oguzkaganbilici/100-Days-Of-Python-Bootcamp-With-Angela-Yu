class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        
    def still_has_questions(self):
        if self.question_number == len(self.question_list):
            return False
        else:
            return True
        
    def check_answer(self,user_answer, correct_answer):
        if correct_answer.lower() == user_answer:
             self.score += 1
             print("You got it right")
        else:
             print("That's wrong")
             print(f"The correct answer was: {correct_answer}.")
             
        print(f"Your current score is {self.question_number}/{self.score}")
        print("\n")
        
        if not self.still_has_questions():
            print("You have completed quiz")
            print(f"Your final score is {self.question_number}/{self.score}")

            
        
             
        
             
             
    def next_question(self):
        answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text}. (True/False): ")
        correct_answer = self.question_list[self.question_number].answer
        self.question_number = self.question_number + 1
        self.check_answer(answer, correct_answer)
        
        
        
   
        