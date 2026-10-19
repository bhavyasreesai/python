import random
def get_choices():
    player_choice=input("enter your choice(rock,paper,scissors- )")#variable
#we can use single quote and double quote
    options=["rock","paper","scissors"]
    computer_choice=random.choice(options)#variable #we are making the computer to make its own choices
#function is set of code only runs when it is called
#in python indentation is very important
    choices={"player": player_choice, "computer" : computer_choice }
    return choices
def check_win(player,computer): #creating (ARGUMENT)function
    print(" player chose " + player + " computer chose " + computer)#concatenating strings
#  print(f"you chose{player} ,computer chose {computer}")
    if player==computer:
       return "its a tie!"
    elif player=="rock" and computer=="scissors":
        return "rock smashes scissors! player win"
    elif player=="rock" and computer=="paper":
        return "paper covers rock! computer win"
    elif player=="paper" and computer=="scissors":
        return "scissors cut paper! computer win"
    elif player=="paper" and computer=="rock":
        return "paper covers rock! player win"
    elif player=="scissors" and computer=="paper":
        return "scissors cut paper! player win"
    elif player=="scissors" and computer=="rock":
        return "rock smashes scissors! computer win"
    else:
        return "invalid choice"
        check_win("rock","paper")

#refactoring and nested if

    if player == computer:
        return "its a tie"
    elif player == "rock":
        if computer == "paper":
            return "computer win"
        else :
            return "player win"
    elif player == "paper":
        if computer == "rock":
            return "player win"
        else:
            return "computer win"
    elif player==scissors:
        if computer == "rock":
            return "computer win"
        else:
            return "player win"


choices=get_choices()
result=check_win(choices["player"],choices["computer"])
print(result)

#calling functions
#def greeting():
#   return"hi"
#response=greeting()
#print(greeting())
#print(response)

#DICTIONARIES

dict={"name":"beau","colour":choices}
       # key:value
       # in a dictionary can be a variable

# USER INPUT

#INPUT LIBRARIES,LITS,METHODS
 #Python LIBRARIES ARE USEFUL , WE DON'T HAVE TO WRITE CODE FROM SCRACH
#a list in python are used to store multiple item in a single variable

food=["pizza","carrots","eggs"]
dinner=random.choice(food)

#FUNCTION ARGUMENTS
#we create checkmate

#IF STATEMENT
a=3
b=5
if a>b:
    print("yes")

#concatenating strings
#we can concatenate with +
    #we can combine strings with other strings,strings with variables
    # we also have another method called "f-string"
    age=25
    print(f"jim is {age} years old")
#ELSE AND ELIF STATEMENTS
age = 10
if age>18:
    print("adult")
elif age >12:
    print("teenager")
elif age>1:
    print("child")
else:
    print("baby")

# REFACTORING AND NESTED IF
#process of restructuring code,while keeping the original functianllyty