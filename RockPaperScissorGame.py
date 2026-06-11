"""
WORKFLOW OF PROJECT:
1. Input from user: rock, paper, or scissors
2. Computer will choose (Computer will choose randomly not conditionally)
3. Result point

Cases: 
A - Rock
Rock - Rock = Tie
Rock - Paper = Computer wins
Rock - Scissors = User wins

B - Paper
Paper - Paper = Tie
Paper - Rock = Computer wins
Paper - Scissors = Computer wins

C - Scissors
Scissors - Scissors = Tie
Scissors - Rock = Computer wins
Scissors - Paper = User wins

"""

import random

item_list = ["Rock", "Paper", "Scissors"]
user_choice = input("Enter your choice (Rock, Paper, Scissors): ")
computer_choice = random.choice(item_list)

print("User's choice:", user_choice)
print("Computer's choice:", computer_choice)

if user_choice == computer_choice:
    print("Both chooses same: Match tie")

# elif (user_choice == "Rock" and computer_choice == "Scissors") or (user_choice == "Paper" and computer_choice == "Rock") or (user_choice == "Scissors" and computer_choice == "Paper"):
#     print("User wins")
# else:
#     print("Computer wins")


## Another way to write the same code is:

elif user_choice == "Rock":
    if computer_choice == "Scissors":
        print("Rock break the scissors : User wins")
    else:
        print("Paper covers rock : Computer wins")

elif user_choice == 'Paper':
    if computer_choice == "Rock":
        print("Paper covers rock : User wins")
    else:
        print("Scissors cut paper : Computer wins")

elif user_choice == "Scissors":
    if computer_choice == "Paper":
        print("Scissors cut paper : User wins")
    else:
        print("Rock break the scissors : Computer wins")
