import random

diseases = ["coronavirus", "cancer", "stroke", "heart disease"]
foods = ["grass", "hay", "lettuce", "carrot"]
genders = ["male", "female"]

class Rabbit:

    def __init__(self, age, frailty, gender, causeOfDeath="Not Dead"):
        self.age = age
        self.frailty = frailty
        self.gender = gender
        self.causeOfDeath = causeOfDeath
        self.pregnancy = False
        self.kittens = []
        self.pregnancy_assigned = False
        self.starve_day_count = 0

    def find_food(self):
        print("Starve day count: " + str(self.starve_day_count) + " days.")
        random_int = random.randint(0, self.frailty + 3)
        print("Random number is " + str(random_int))

        if random_int % 6 == 0:
          food = foods[0]
          self.starve_day_count = 0
        elif random_int % 6 == 1:
          food = foods[1]
          self.starve_day_count = 0
        elif random_int % 6 == 2:
          food = foods[2]
          self.starve_day_count = 0
        elif random_int % 6 == 3 or random_int % 6 == 5:
          food = foods[3]
          self.starve_day_count = 0
        elif random_int % 6 == 4:
          food = "None"

        print("Food is " + food)
        
        if food == "None":
          self.frailty += 1
          self.starve_day_count += 1

        if self.starve_day_count == 3:
          self.die()

    def endOfDay(self):
        self.age += 1
        print("This rabbit is " + str(self.age) + " days old.")
        self.find_food()
        if self.age >= 10: #previously 365
            self.frailty += 1
        if self.frailty > 10: #previously 50
            if self.gender == "female" and self.pregnancy == False:
              self.breed()
            if self.frailty >= 730: #730 days = 2 years
                self.die()
            random_num = random.randint(0, 12)
            if random_num == 1:
                self.die()

    def breed(self):
      if self.pregnancy == False:
        if self.pregnancy_assigned == False:
          global pregnancy_start
          pregnancy_start = self.age
          self.pregnancy_assigned = True
        if self.age >= (pregnancy_start + 30): #previously if
          self.pregnancy = True
          random_num = random.randint(0, 12)
          if random_num == 0:
            self.pregnancy = False
          else:
            for i in range(random_num):
              rabbit = Rabbit(0, 0, genders[random.randint(0,1)])
              self.kittens.append(rabbit)
            
    def die(self):
      #del self.age
      #del self.frailty
      #del self.gender
      self.causeOfDeath = diseases[random.randint(0, 3)]


class Colony:
  def __init__(self):
    self.rabbits = []

  def addRabbit(self):
    age = int(input("Age of the rabbit: "))
    frailty = int(input("Frailty of the rabbit: "))
    gender = input("Gender of the rabbit: ")
    rabbit = Rabbit(age, frailty, gender)
    self.rabbits.append(rabbit)

  def addMultiple(self):
    number = int(input("How many new rabbits would you like to add: "))
    for i in range(number):
      rabbit = Rabbit(0, 0, genders[random.randint(0, 1)])
      self.rabbits.append(rabbit)

  def calculateDeads(self):
    deads = 0
    for i in self.rabbits:
      if i.causeOfDeath != "Not Dead":
        deads += 1
    return deads

  def calculatePregnantRabbits(self):
    pregnant_rabbits = 0
    for i in self.rabbits:
      if i.pregnancy == True:
        pregnant_rabbits += 1
    return pregnant_rabbits

  def calculateGenders(self):
    males = 0
    females = 0
    for i in self.rabbits:
      if i.gender == "male":
        males += 1
      else:
        females += 1
    print("There are " + str(males) + " male rabbits.")
    print("There are " + str(females) + " female rabbits.")

  def increaseAge(self):
    number = int(input("How many days would you like to pass: "))
    for rabbit in self.rabbits:
      for i in range(number):
        rabbit.endOfDay()

  def report(self):
    print("There are " + str(len(self.rabbits)) + " rabbits in this colony.")
    print(str(self.calculateDeads()) + " rabbits are dead.")
    print(str(self.calculatePregnantRabbits()) + " rabbits are pregnant.")
    self.calculateGenders()
