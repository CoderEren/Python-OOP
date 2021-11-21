#Create a class that writes a takeaway order to a file
import random

itemsList = ["Sushi", "Hamburger", "Pizza", "Kebab"]

class Takeaway:
  def __init__(self):
    self.items = []
    self.costs = []
    self.total = 0
    self.totalItems = 0

  def addItem(self):
    item = input("Enter the item name: ")
    cost = int(input("Enter the cost of the item: "))
    self.items.append(item)
    self.costs.append(cost)
    self.totalItems += 1

  def addMultiple(self):
    number = int(input("Enter how many items you would like to add: "))
    for i in range(number):
      self.items.append(random.choice(itemsList))
      self.costs.append(random.randint(5, 15))
      self.totalItems += 1

  def calculateTotal(self):
    self.total = 0
    for cost in self.costs:
      self.total += cost

  def printReceipt(self):
    self.calculateTotal()
    receipt = open("receipt.txt", "w")
    receipt.write("### Welcome to Takeaway ###\n\n")

    for i in range(self.totalItems):
      receipt.write(self.items[i] + ":\t\t" + "£" + str(self.costs[i]) + "\n")

    receipt.write("\n")
    receipt.write("Total Number of Items: \t\t" + str(self.totalItems)+ "\n")
    receipt.write("Total: \t\t£" + str(self.total) + "\n")

    receipt.close()
