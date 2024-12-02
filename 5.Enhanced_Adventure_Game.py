# Project-5(Game - Enhanced Adventure Game)
# Expanded Text-Based Adventure Game with Player Name

def start_game():
    print("Welcome to the Adventure Game!")
    player_name = input("Before we begin, what is your name, brave adventurer? ")
    print(f"Great to meet you, {player_name}! You find yourself standing at the edge of a dark, mysterious forest known as the Enchanted Forest.")
    print("Legends speak of magical creatures, hidden treasures, and daunting challenges within.")
    print("With a mix of excitement and trepidation, you decide to step forward and uncover the secrets that lie within.")
    print("You arrive at a fork in the path, where two distinct trails lie ahead:")
    print("1. The Left Path: Rumored to be home to a friendly wizard who grants magical powers.")
    print("2. The Right Path: Known for its lurking dangers, including a sleeping dragon said to guard a great treasure.")

    choice = input("What will you choose? (1 or 2): ")

    if choice == '1':
        left_path(player_name)
    elif choice == '2':
        right_path(player_name)
    else:
        print("Invalid choice. Please choose 1 or 2.")
        start_game()

def left_path(player_name):
    print(f"\nYou walk down the left path, {player_name}, and soon encounter a friendly wizard sitting by a bubbling brook.")
    print("The wizard smiles warmly and offers you a magic potion.")
    print("1. Drink the potion.")
    print("2. Refuse the potion.")

    choice = input("What will you do? (1 or 2): ")

    if choice == '1':
        print("\nYou feel a surge of energy and gain magical powers!")
        print("With these powers, you can explore further or return to the fork in the path.")
        print("1. Explore deeper into the forest.")
        print("2. Return to the fork.")

        choice = input("What will you do? (1 or 2): ")
        if choice == '1':
            explore_forest(player_name)
        elif choice == '2':
            start_game()
        else:
            print("Invalid choice. Please choose 1 or 2.")
            left_path(player_name)

    elif choice == '2':
        print("\nThe wizard becomes angry and casts a spell on you. You lose!")
    else:
        print("Invalid choice. Please choose 1 or 2.")
        left_path(player_name)

def explore_forest(player_name):
    print(f"\nAs you explore deeper, {player_name}, you stumble upon a magical fountain that sparkles in the sunlight.")
    print("You can drink from the fountain or continue exploring.")
    print("1. Drink from the fountain.")
    print("2. Continue exploring.")

    choice = input("What will you do? (1 or 2): ")

    if choice == '1':
        print("\nThe fountain grants you eternal youth! You win!")
    elif choice == '2':
        print("\nYou wander further into the forest and discover a hidden cave filled with treasure!")
        print("1. Take some treasure.")
        print("2. Leave the treasure alone.")

        choice = input("What will you do? (1 or 2): ")
        if choice == '1':
            print("\nAs you take the treasure, the cave collapses! You lose!")
        elif choice == '2':
            print("\nYou leave the treasure and return safely to the path. You win!")
        else:
            print("Invalid choice. Please choose 1 or 2.")
            explore_forest(player_name)
    else:
        print("Invalid choice. Please choose 1 or 2.")
        explore_forest(player_name)

def right_path(player_name):
    print(f"\nYou walk down the right path, {player_name}, and find a sleeping dragon curled up in a clearing.")
    print("You have two options:")
    print("1. Sneak past the dragon.")
    print("2. Wake up the dragon.")

    choice = input("What will you do? (1 or 2): ")

    if choice == '1':
        print("\nYou successfully sneak past the dragon and discover a hidden treasure chest nestled among the roots of an ancient tree.")
        print("1. Open the treasure chest.")
        print("2. Leave the treasure and continue walking.")

        choice = input("What will you do? (1 or 2): ")
        if choice == '1':
            treasure_chest(player_name)
        elif choice == '2':
            print("\nYou leave the treasure and continue through the forest.")
            print("Suddenly, you encounter a band of robbers! You lose!")
        else:
            print("Invalid choice. Please choose 1 or 2.")
            right_path(player_name)

    elif choice == '2':
        print("\nThe dragon wakes up and breathes fire! You lose!")
    else:
        print("Invalid choice. Please choose 1 or 2.")
        right_path(player_name)

def treasure_chest(player_name):
    print(f"\nInside the chest, {player_name}, you find gold coins and a magic map!")
    print("1. Use the map to find a hidden city.")
    print("2. Take the gold and leave.")

    choice = input("What will you do? (1 or 2): ")
    if choice == '1':
        hidden_city(player_name)
    elif choice == '2':
        print("\nYou take the gold and live a comfortable life! You win!")
    else:
        print("Invalid choice. Please choose 1 or 2.")
        treasure_chest(player_name)

def hidden_city(player_name):
    print(f"\nYou follow the map and discover a hidden city filled with wonders, {player_name}!")
    print("The city offers you two paths to explore:")
    print("1. Visit the marketplace.")
    print("2. Explore the enchanted garden.")

    choice = input("What will you do? (1 or 2): ")
    if choice == '1':
        print("\nIn the marketplace, you find a magical item that grants you three wishes! You win!")
    elif choice == '2':
        enchanted_garden(player_name)
    else:
        print("Invalid choice. Please choose 1 or 2.")
        hidden_city(player_name)

def enchanted_garden(player_name):
    print(f"\nIn the enchanted garden, you are greeted by fairies who grant you a choice, {player_name}.")
    print("1. Ask for wisdom.")
    print("2. Ask for power.")

    choice = input("What will you do? (1 or 2): ")
    if choice == '1':
        print("\nYou gain wisdom and become a great leader! You win!")
    elif choice == '2':
        print("\nYou gain power but become a tyrant! You lose!")
    else:
        print("Invalid choice. Please choose 1 or 2.")
        enchanted_garden(player_name)

# Start the game
start_game()
