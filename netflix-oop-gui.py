from easygui import *
from netflix-oop import *
import sys

netflix = Netflix()

while True:
    msg = "Select a command"
    title = "Notflix - Main Menu"
    choices = ["Create an account", "Log In", "Log Out", "Print account details", "Add Films", "Stop"]
    choice = choicebox(msg, title, choices)

    if choice == "Create an account":
        msg = "Enter your information"
        title = "Notflix - Create an account"
        fieldNames = ["Username", "Password"]
        fieldValues = multpasswordbox(msg, title, fieldNames)
        if fieldValues is None:
            sys.exit(0)
        else:
            user = User(fieldValues[0], fieldValues[1])
            netflix.users.append(user)
    elif choice == "Log In":
        msg = "Enter your login information"
        title = "Notflix - Log In"
        fieldNames = ["Username", "Password"]
        fieldValues = multpasswordbox(msg, title, fieldNames)
        if fieldValues is None:
            sys.exit(0)
        else:
            username = fieldValues[0]
            password = fieldValues[1]
            for account_index in range(len(netflix.users)):
                if username == netflix.users[account_index].username:
                    if netflix.users[account_index].loggedIn == True:
                        print("You are already logged in!")
                    else:
                        if password == netflix.users[account_index].password:
                                netflix.users[account_index].loggedIn = True
                                print("You are now logged in!")
    elif choice == "Log Out":
        msg = "Enter your login information"
        title = "Notflix - Log Out"
        fieldNames = ["Username", "Password"]
        fieldValues = multpasswordbox(msg, title, fieldNames)
        if fieldValues is None:
            sys.exit(0)
        else:
            username = fieldValues[0]
            password = fieldValues[1]
            for account_index in range(len(netflix.users)):
                if username == netflix.users[account_index].username:
                    if netflix.users[account_index].loggedIn == True:
                        netflix.users[account_index].loggedIn = False
                        print("You are now logged out!")
                    else:
                        print("You are already logged out!")
                        
    elif choice == "Print account details":
        msg = "Enter your login information"
        title = "Notflix - Log In To Print Account Details"
        fieldNames = ["Username", "Password"]
        fieldValues = multpasswordbox(msg, title, fieldNames)
        if fieldValues is None:
            sys.exit(0)
        else:
            username = fieldValues[0]
            password = fieldValues[1]
            for account_index in range(len(netflix.users)):
                if username == netflix.users[account_index].username:
                    if netflix.users[account_index].loggedIn == True:
                        print("You are already logged in!")
                        message = "Username: " + netflix.users[account_index].username + "\nPassword: " + netflix.users[account_index].password + "\nFilms: " + str(netflix.users[account_index].films)
                        title2 = "Your Account Details"
                        msgbox(message, title=title2, ok_button="Okay!")
                    else:
                        if password == netflix.users[account_index].password:
                                netflix.users[account_index].loggedIn = True
                                print("You are now logged in!")
                                message = "Username: " + netflix.users[account_index].username + "\nPassword: " + netflix.users[account_index].password + "\nFilms: " + str(netflix.users[account_index].films)
                                title2 = "Your Account Details"
                                msgbox(message, title=title2, ok_button="Okay!")

    elif choice == "Add Films":
        msg = "Enter your login information"
        title = "Notflix - Log In To Add Films"
        fieldNames = ["Username", "Password"]
        fieldValues = multpasswordbox(msg, title, fieldNames)
        if fieldValues is None:
            sys.exit(0)
        else:
            username = fieldValues[0]
            password = fieldValues[1]
            for account_index in range(len(netflix.users)):
                if username == netflix.users[account_index].username:
                    if netflix.users[account_index].loggedIn == True:
                        print("You are already logged in!")
                        message = "Add a film"
                        title2 = "Notflix - Add a film"
                        film = enterbox(message, title=title2)
                        netflix.users[account_index].films.append(film)
                    else:
                        if password == netflix.users[account_index].password:
                                netflix.users[account_index].loggedIn = True
                                print("You are now logged in!")
                                message = "Add a film"
                                title2 = "Notflix - Add a film"
                                film = enterbox(message, title=title2)
                                netflix.users[account_index].films.append(film)
                                
    elif choice == "Stop":
        break
