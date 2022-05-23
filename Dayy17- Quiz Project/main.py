from question_model import Question
from data import question_data as qt
from quiz_brain import QuizBrain 


question_bank = []

for i in qt:
    questions = i["text"]
    answers = i["answer"]
    newQuestion = Question(questions, answers)
    question_bank.append(newQuestion)



quiz = QuizBrain(question_bank)
while(quiz.still_has_questions()):
    quiz.next_question()

    
