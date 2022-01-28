#Create an OOP system for Netflix for each user, storing their data and watched films
#How to use:
#   netflix = Netflix()
#   netflix.mainMenu()

import os
import hashlib

class Netflix:
    def __init__(self):
        self.users = []
       
    def createUser(self):
        username = input("What is your username: ")
        password = input("What is your password: ")
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        usernames_found = 0
        for user in self.users:
            if username == user.username:
                print("Username already taken!")
                usernames_found += 1
                break
        if usernames_found == 0:
            user = User(username, hashed_password)
            self.users.append(user)


    def findHighestNumber(self, number_list):
        highest_num = 0
        for i in range(len(number_list)):
            if number_list[i] > highest_num:
                highest_num = number_list[i]
        return highest_num


    def createAccountToFilm(self):
        account_index = self.login()
        films_list = self.users[account_index].films
        account_to_film = {}
        for other_account_index in range(len(self.users)): #find common films in all users
            common_films = 0
            for film in self.users[other_account_index].films:
                for original_film in films_list:
                    if original_film == film:
                        common_films += 1
            account_to_film[other_account_index] = common_films
        account_to_film[account_index] = 0
        
        return account_to_film

    def recommendUser(self):
        account_to_film = self.createAccountToFilm()
        common_films_list = []
        for key in account_to_film: #find the user with the highest number of common films
            common_films_list.append(account_to_film[key])
        highest_common_films = self.findHighestNumber(common_films_list)

        compatible_users = []
        for i in range(len(common_films_list)):
            if common_films_list[i] == highest_common_films:
                compatible_users.append(i)

        #compatible_account_index = common_films_list.index(highest_common_films)
        for user in compatible_users:
            print("The user", self.users[user].username, "has watched", str(highest_common_films), "of the same movies as you!")

        return account_to_film

    
    def socialNetwork(self):
        account_to_film = self.createAccountToFilm()
        user_indices = []
        for key in account_to_film: #find users with more than or equal to 5 common films
            if account_to_film[key] >= 5:
                user_indices.append(key)
        for user in user_indices:
            print("The user", self.users[user].username, "has watched", account_to_film[user], "of the same movies as you!")


    def datingApp(self):
        account_to_film = self.createAccountToFilm()
        user_indices = []
        for key in account_to_film: #find users with more than or equal to 5 common films
            if account_to_film[key] >= 3:
                user_indices.append(key)
        for user in user_indices:
            print("Found a match! The user", self.users[user].username, "has watched", account_to_film[user], "of the same movies as you!")
    
       
    def login(self):
        username = input("Enter your username: ")
        #for user in self.users:
        for account_index in range(len(self.users)):
            if username == self.users[account_index].username:
                if self.users[account_index].loggedIn == True:
                    print("You are already logged in!")
                    return account_index
                else:
                    while True:
                        password = input("Enter your password: ")
                        hashed_password = hashlib.md5(password.encode()).hexdigest()
                        if hashed_password == self.users[account_index].password:
                            self.users[account_index].loggedIn = True
                            print("You are now logged in!")
                            return account_index

    def logout(self):
        username = input("Enter your username: ")
        for account_index in range(len(self.users)):
            if username == self.users[account_index].username:
                if self.users[account_index].loggedIn == True:
                    self.users[account_index].loggedIn = False
                    print("You are now logged out!")
                else:
                    print("You are already logged out!")
                    
                       
    def mainMenu(self):
        while True:
            print("~"*30)
            print("Menu Actions:")
            print("1. Create an account")
            print("2. Log in")
            print("3. Print account details")
            print("4. Add films")
            print("5. Create films file")
            print("6. Reset password")
            print("7. Delete existing films and create a new films list")
            print("8. Log out")
            print("9. Find users who has watched the most similar movies to you")
            print("10. Social Network - find users who have 5 or more movies similar to you")
            print("11. Dating App - find users who have 3 or more movies similar to you")
            print("12. Stop")
            print("~"*30)
            command_number = int(input())
            if command_number == 1:
                self.createUser()
            elif command_number == 2:
                self.login()
            elif command_number == 3:
                account_index = self.login()
                self.users[account_index].printAccountDetails()
            elif command_number == 4:
                account_index = self.login()
                self.users[account_index].addFilm()
            elif command_number == 5:
                account_index = self.login()
                self.users[account_index].createFilmsFile()
            elif command_number == 6:
                account_index = self.login()
                self.users[account_index].resetPassword()
            elif command_number == 7:
                account_index = self.login()
                self.users[account_index].overwriteFilms()
            elif command_number == 8:
                self.logout()
            elif command_number == 9:
                self.recommendUser()
            elif command_number == 10:
                self.socialNetwork()
            elif command_number == 11:
                self.datingApp()
            elif command_number == 12:
                break
       
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.films = []
        self.loggedIn = False
       
    def printAccountDetails(self):
        print("Username: ", self.username, "\n")
        print("Password: ", self.password, "\n")
        print("Films: ", self.films, "\n")
       
    def addFilm(self):
        number = int(input("How many films would you like to add: "))
        for i in range(number):
            film_name = input("Name of the film: ")
            self.films.append(film_name)

    def overwriteFilms(self):
        ask_confirmation = input("Are you sure you would like to delete the existing films and create a new list? (y/n) \n").lower()
        if ask_confirmation == "y" or ask_confirmation == "yes":
            self.films = []
            self.addFilm()
        else:
            print("The existing films list is not deleted.")
           
    def createFilmsFile(self):
        ask_personal_name = input("Would you like to call your list something other than your username (y/n): ").lower()
        if ask_personal_name == "y" or ask_personal_name == "yes":
            file_name = input("What would you like this films list to be called: ")
            files = os.listdir()
            if (file_name + ".txt") not in files:
                f = open(file_name + ".txt", "w")
                f.write("Films watched by " + self.username + ":\n")
                for film in self.films:
                    f.write(" - " + film + "\n")
                f.close()
            else:
                print("There is already a file with that name in the current directory!")
        else:
            files = os.listdir()
            if (file_name + ".txt") not in files:
                f = open(self.username + ".txt", "w")
                f.write("Films watched by " + self.username + ":\n")
                for film in self.films:
                    f.write(" - " + film + "\n")
                f.close()
            else:
                print("There is already a file with that name in the current directory!")

    def resetPassword(self):
        new_password = input("Enter your new password: ")
        hashed_password = hashlib.md5(new_password.encode()).hexdigest()
        self.password = hashed_password
        print("Password changed to", self.password)
       
