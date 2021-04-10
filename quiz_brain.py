class QuizBrain:

  def __init__(self , question_list):
    self.question_number = 0
    self.question_list = question_list
    self.score = 0
    

  def check_answer(self, user_ans , ans):
    if user_ans.lower() == ans.lower():
      print("You Got it Right\n")
      self.score +=1 
      
    else:
      print("That's Wrong\n")
    print(f"The correct answer was : {ans}\n")
    print(f"Your Score is {self.score} / {self.question_number}\n")
  def still_has_questions(self):
    if self.question_number == len(self.question_list):
      return False
    else:
      return True



  def next_question(self):
    current_question = self.question_list[self.question_number]
    self.question_number += 1
    user_answer = input(f"Q {self.question_number}:{current_question.text} (True / False)")
    self.check_answer(user_answer , current_question.answer)
