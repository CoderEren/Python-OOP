import random

aceChoices = [1, 11]
names = ["Eren", "Michael", "John", "Rachael", "Michelle"]
cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
cardsToNumber = {"Ace":random.choice(aceChoices),
                 "2":2,
                 "3":3,
                 "4":4,
                 "5":5,
                 "6":6,
                 "7":7,
                 "8":8,
                 "9":9,
                 "10":10,
                 "Jack": 10,
                 "Queen":10,
                 "King":10}

class Player():
    def __init__(self):
        self.score = 0
        self.deck = [random.choice(cards), random.choice(cards)]
        self.values = []
        self.failed = False
        self.won = False
        self.twisted = False
        self.name = random.choice(names)
        
    def updateScore(self):
        for card in self.deck:
            value = cardsToNumber[card]
            self.values.append(value)
        self.score = 0
        for i in self.values:
            self.score += i
            
    def checkFail(self):
        if self.score > 21:
            self.failed = True
            #self.score = 0
            #self.deck = []
            #self.values = []
        elif self.score == 21:
            self.won = True
        elif len(self.deck) >= 5:
          self.won = True
    
    def askForTwist(self):
        if self.failed == False:
            print("Would you like to draw another card,", self.name, "(yes/no): ")
            twistInput = input().lower()
            if twistInput == "yes":
                self.twisted = True
            else:
                self.twisted = False
        

class Game():
  def __init__(self):
        self.players = []
        self.noOfPlayers = 0
        self.failedPlayers = []
        self.winners = []
      
  def startGame(self):
    self.noOfPlayers = int(input("How many people are playing: "))
    if self.noOfPlayers == 4:
        for i in range(0, self.noOfPlayers):
            player = Player()
            self.players.append(player)
        self.initialDeal()
        self.report()
        while True:
            continueInput = input("Would you like to continue (yes/no)? ").lower()
            if continueInput == "no":
                break
            else:
                self.report()
                self.deal()

              
  def deal(self):
      for i in range(0, self.noOfPlayers):
        self.players[i].askForTwist()
        if self.players[i].twisted == True:
          card = random.choice(cards)
          self.players[i].deck.append(card)
          self.players[i].values.append(cardsToNumber[card])
          self.players[i].score += cardsToNumber[card]
        #self.players[i].updateScore()
        self.players[i].checkFail()
        if self.players[i].failed == True:
          self.failedPlayers.append(self.players[i])
        elif self.players[i].won == True:
          self.winners.append(self.players[i])

  def initialDeal(self):
      for i in range(0, self.noOfPlayers):
        self.players[i].askForTwist()
        if self.players[i].twisted == True:
          card = random.choice(cards)
          self.players[i].deck.append(card)
          #self.players[i].values.append(cardsToNumber[card])
        self.players[i].updateScore()
        self.players[i].checkFail()
        if self.players[i].failed == True:
          self.failedPlayers.append(self.players[i])
        elif self.players[i].won == True:
          self.winners.append(self.players[i])
        
  def printScores(self):
      for player in self.players:
          print(player, "has scored", player.score)

  def report(self):
      for player in self.players:
          print(player)
          print("\t", player.score)
          print("\t", player.deck)
          print("\t Failed:", player.failed)
          print("\t Won:", player.won)
