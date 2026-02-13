import random
choices = ["Rock", "Paper", "Scissors"]

playerChoice = input("give me a number 1-3")

playerChoice = int(playerChoice)

if playerChoice < 1 or playerChoice > 3:
	print("error not between 1 -3")
else: 
    computerChoice = random.randint(1, 3)

    if playerChoice == computerChoice:
        print("its a tie")
    elif playerChoice == 1 and computerChoice == 3:
        print("rock beats scissors -u win")
    elif playerChoice == 1 and computerChoice == 2:
        print("Paper beats Rock (you've lost)")
    elif playerChoice == 2 and computerChoice == 3:
        print("Scissors beats Paper you lose")
    elif playChoice == 2 and computerChoice == 1:
        print("Paper beats Rock you have WON!")
    elif playerChoice == 3 and computerChoice == 1:
        print("Rock beats Scissors you've lost")
    elif playerChoice == 3 and computerChoice == 2:
        print("Scissors beats Paper, you've Won!")
