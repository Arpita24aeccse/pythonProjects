# Project-6 (Game - Number Guesser)

# Purpose: This program is a simple number-guessing game where the user tries to guess a randomly generated number within a specified range.


# Import the random module to generate a random number
import random

# Ask the user to type a number for the upper limit of the guessing range
top_of_range = input("Type a number for the upper limit: ")

# Check if the input is a digit (a positive whole number)
# The isdigit() method returns True if all characters in the string are digits
if top_of_range.isdigit():
    # Convert the input string to an integer
    top_of_range = int(top_of_range)

    # Check if the number is greater than 0
    if top_of_range <= 0:
        print('Please type a number larger than 0 next time.')
        quit()  # Exit the program if the number is not valid
else:
    print('Please type a valid number next time.')
    quit()  # Exit the program if the input is not a number

# Generate a random number between 0 and the upper limit (top_of_range)
random_number = random.randint(0, top_of_range)

# Initialize the number of guesses made by the user
guesses = 0

# Start an infinite loop for the guessing game
while True:
    # Increment the guess count using a more basic line
    guesses = guesses + 1  # Increase the guess count by 1

    # Ask the user to make a guess
    user_guess = input("Make a guess: ")

    # Check if the input is a digit
    if user_guess.isdigit():
        # Convert the input string to an integer
        user_guess = int(user_guess)
    else:
        print('Please type a valid number next time.')  # Prompt for a valid number if input is invalid
        continue  # Go back to the start of the loop if input is invalid

    # Check if the user's guess is correct
    if user_guess == random_number:
        print("You got it!")  # Congratulate the user if they guessed correctly
        break  # Exit the loop if the guess is correct
    elif user_guess > random_number:
        print("You were above the number!")  # Hint if the guess is too high
    else:
        print("You were below the number!")  # Hint if the guess is too low

# Print the total number of guesses the user made
print("You got it in", guesses, "guesses!")
