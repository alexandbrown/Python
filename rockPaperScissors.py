import random

def rockPaperScissors(user_input, computer_input):
    if (user_input == "rock") & (computer_input == "rock"):
        print("The computer threw rock. Rock and rock ends in a draw.")
    elif (user_input == "scissors") & (computer_input == "scissors"):
        print("The computer threw scissors, Scissors and scissors ends in a draw")
    elif (user_input == "paper") & (computer_input == "paper"):
        print("The computer threw paper, Paper and paper ends in a draw")

    elif (user_input == "scissors") & (computer_input == "rock"):
        print("The computer threw rock, Rock versus scissors, computer win!") 
    elif (user_input == "rock") & (computer_input == "paper"):
        print("The computer threw paper, Paper versus rock, computer win!")
    elif (user_input == "scissors") & (computer_input == "rock"):
        print("The computer threw rock, Rock versus scissors, computer win!")

    elif (user_input == "rock") & (computer_input == "scissors"):
        print("The computer drew scissors, Scissors versus rock, you win!")
    elif (user_input == "paper") & (computer_input == "rock"):
        print("the computer drew rock, Rock versus paper, you win!")
    elif (user_input == "scissors") & (computer_input == "paper"):
        print("The computer drew paper, Paper versus scissors, you win!")

rock = "rock"
paper = "paper"
scissors = "scissors"

list = [rock, paper, scissors]
computer = random.choice(list)

response = input("Do you want to play rockPaperScissors? 'Y' for yes, anything else for no: ").upper()
while response == "Y":
    user = input("Rock. Paper. Scissors. Shoot!: ").lower()
    computer = random.choice(list)
    rockPaperScissors(user,computer)
    response = input("Do you want to play again? 'Y' for yes, anything else for no: ").upper()
