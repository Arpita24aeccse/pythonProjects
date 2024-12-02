# Project-1 (Game - Rock, Paper, Scissors)
# Rock-Paper-Scissors Game

# The game will randomly assign the computer's choice, and based on the user’s input, it will determine the winner.
# Rock beats Scissors, Scissors beat Paper, and Paper beats Rock.


# Import the random module to generate a random number
import random

def GameWin(comp, you):
    # Function to determine the winner
    # Returns True if you win, False if you lose, None if it's a tie

    # If the computer and player choose the same option, it's a tie
    if comp == you:
        return None

    # Checking all conditions if the computer chose 'rock' (r)
    elif comp == 'r':
        if you == 's':  # Scissors lose to Rock
            return False
        elif you == 'p':  # Paper beats Rock
            return True

    # Checking all conditions if the computer chose 'paper' (p)
    elif comp == 'p':
        if you == 'r':  # Rock loses to Paper
            return False
        elif you == 's':  # Scissors beat Paper
            return True

    # Checking all conditions if the computer chose 'scissors' (s)
    elif comp == 's':
        if you == 'p':  # Paper loses to Scissors
            return False
        elif you == 'r':  # Rock beats Scissors
            return True

# Computer's turn to select Rock, Paper, or Scissors randomly
print("Comp Turn: Rock(r), Paper(p), or Scissors(s)?")
RandNo = random.randint(1, 3)  # Generate a random number between 1 and 3
if RandNo == 1:
    comp = 'r'
elif RandNo == 2:
    comp = 'p'
elif RandNo == 3:
    comp = 's'

# Player's turn to input choice
you = input("Your Turn: Rock(r), Paper(p), or Scissors(s)? ")

# Displaying choices of both computer and player
print(f"Computer Chose: {comp}")
print(f"You Chose: {you}")

# Determine the game result
a = GameWin(comp, you)

# Displaying the result based on the outcome from the GameWin function
if a == None:
    print("The game is a Tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")
    