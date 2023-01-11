import random

player1 = input("Select Rock, Paper, or Scissor :").lower()
computer = random.choice(["Rock", "Paper", "Scissor"]).lower()
print("Computer selected: ", computer)

if player1 == "rock" and computer == "paper":
    print("Computer Won")
elif player1 == "paper" and computer == "scissor":
    print("Computer Won")
elif player1 == "scissor" and computer == "rock":
    print("Computer Won")
elif player1 == computer:
    print("It was a draw!")
else:
    print("Player 1 Won")
