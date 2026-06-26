# random is a library in python which is used to select options randomly 
import random;
# def is used to define a function in python
def get_choices():
    #Using a variable named Player_Choice to take user input for game 
    Player_choice = input("ENTER YOUR CHOICE(ROCK,PAPER,SCISSOR):")
    # Using list named Options
    # A List is a collections of elments which is mutlable means can be changed later on. 
    Options = ["ROCK", "PAPER","SCISSORS"]
    # now using computer choice variable to implement computer choice by using choice method from random library
    Computer_choice = random.choice(Options)
    # now to return player and computer choice insted of writing return Player_choice , Computer_choice like this we use dictioncary
    # A Python dictionary is a built-in, mutable data structure used to store collection items in key-value pairs
    # we have assigned the key as Player and Computer and value as variables Player_choice and Computer_choice
    Choices = {"Player": Player_choice, "Computer": Computer_choice}
    return Choices
#now we will define a function to check the winner of the game. We have passed two parameters player and computer to the function check_win
def check_win(player, computer):
    # instead of using print("You chose: " + player + "and Computer chose" + computer) to print the choices of player and computer we will use f string to make it more readable and easy to understand
    # using f string we can directly insert the variables player and computer in the string without using + operator to concatenate the strings.
    print(f"Your choice is {player} and Computer choice is {computer}")
    #now we will use if else statements to check the winner of the game
    if player == computer:
        return "Its a tie!"
    # instead of writting lengthy code again and again like elif player == "ROCK" and computer == "SCISSORS": we use Nested if else ladders
    elif player == "ROCK":
        if computer == "SCISSORS":
            return "ROCK smashes SCISSORS! You win!"
        else:
            return "PAPER covers ROCK! You lose."
    elif player == "PAPER":
        if computer == "ROCK":
            return "PAPER covers ROCK! you win!"
        else:
            return "SCISSORS cuts PAPER! You lose."
    elif player == "SCISSORS":
        if computer == "ROCK":
            return "ROCK smashes SCISSORS! You lose."
        else:
            return "SCISSORS cuts PAPER! You win!"
#   NOW we will call the get_choices function to get the choices of player and computer and store it in a variable named choices   
choices = get_choices()
# now using the check_win function we will pass the player and computer choices to check who is the winner of the game and store the result in a variable named result
# using choices["Player"] we can access the value of the key Player in the dictionary choices and using choices["Computer"] we can access the value of the key Computer in the dictionary choices
result = check_win(choices["Player"], choices["Computer"])
print(result)
