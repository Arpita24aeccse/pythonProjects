# Project-4(Game - Adventure Game)
# Simple Text-Based Adventure Game

# Purpose: To create an interactive text-based adventure game where players navigate through different scenarios, make choices, and face consequences based on their decisions. This game aims to engage users in storytelling and enhance their problem-solving skills through an immersive experience.

def start_game():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark forest. There are two paths ahead.")
    print("1. Take the left path.")
    print("2. Take the right path.")

    choice = input("What will you do? (1 or 2): ")

    if choice == '1':
        left_path()
    elif choice == '2':
        right_path()
    else:
        print("Invalid choice. Please choose 1 or 2.")
        start_game()

def left_path():
    print("\nYou walk down the left path and encounter a friendly wizard.")
    print("The wizard offers you a magic potion.")
    print("1. Drink the potion.")
    print("2. Refuse the potion.")

    choice = input("What will you do? (1 or 2): ")

    if choice == '1':
        print("\nYou feel a surge of energy and gain magical powers! You win!")
    elif choice == '2':
        print("\nThe wizard becomes angry and casts a spell on you. You lose!")
    else:
        print("Invalid choice. Please choose 1 or 2.")
        left_path()

def right_path():
    print("\nYou walk down the right path and find a sleeping dragon.")
    print("You can either sneak past it or wake it up.")
    print("1. Sneak past the dragon.")
    print("2. Wake up the dragon.")

    choice = input("What will you do? (1 or 2): ")

    if choice == '1':
        print("\nYou successfully sneak past the dragon and escape the forest! You win!")
    elif choice == '2':
        print("\nThe dragon wakes up and breathes fire! You lose!")
    else:
        print("Invalid choice. Please choose 1 or 2.")
        right_path()

# Start the game
start_game()
