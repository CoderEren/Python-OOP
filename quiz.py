class Quiz:
  def __init__(self, username, password):
    self.username = username
    self.password = password
    self.questions = []
    self.answers = []
    self.score = 0

  def addQuestion(self):
    question = input("What is the question: ")
    answer = input("What is the answer: ")
    self.questions.append(question.lower())
    self.answers.append(answer.lower())

  def startQuiz(self):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == self.username and password == self.password:
      for question in range(len(self.questions)):
        print("Question", question)
        print("%"*30)
        print(self.questions[question])
        answer = input("")
        if answer.lower() == self.answers[question]:
          print("Well done!")
          self.score += 1
        else:
          print("That's wrong!")
      print("Your score is", self.score)
      self.score = 0
    else:
      print("Wrong login details! Try again.")
