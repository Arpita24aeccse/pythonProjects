# Project-7 (Game - Flashcard Quiz Application)
# Flashcard Quiz Application

# Purpose: Create an interactive quiz that tests users on various questions, providing immediate feedback and scoring.


# Function to run the flashcard quiz
def flashcard_quiz(questions):
    score = 0  # Initialize the score to 0
    total_questions = len(questions)  # Get the total number of questions
    
    # Iterate through each question-answer pair in the questions dictionary,
    # The .items() method is used to retrieve both keys and values as tuples,
    # allowing us to access questions and their corresponding answers simultaneously.
    for question, answer in questions.items():
        # Display the question to the user
        user_answer = input(f"Question: {question} \nYour answer: ")

        # Check if the user's answer is correct
        if user_answer.lower() == answer.lower():
            print("Correct!")  # Provide feedback for a correct answer
            # Increment the score by 1 using basic code
            score = score + 1  # Explicitly increment the score
        else:
            print(f"Incorrect! The correct answer is: {answer}")  # Inform user of the correct answer

    # Display the final score at the end of the quiz
    print(f"\nYou scored {score} out of {total_questions}.")  # Show the user's score

def main():
    # Dictionary of questions and their corresponding answers
    questions = {
        "What is the capital of France?": "Paris",
        "What is 2 + 2?": "4",
        "What is the largest planet in our solar system?": "Jupiter",
        "Who wrote 'Romeo and Juliet'?": "Shakespeare",
        "What is the chemical symbol for water?": "H2O",
        # Additional questions - Just Uncomment them to use
        # "What is the capital of Japan?": "Tokyo",
        # "What is 5 * 6?": "30",
        # "Who painted the Mona Lisa?": "Leonardo da Vinci",
        # "What is the boiling point of water in degrees Celsius?": "100",
        # "What gas do plants absorb from the atmosphere?": "Carbon dioxide",
        # "What is the smallest continent?": "Australia",
        # "Who discovered gravity?": "Isaac Newton",
        # "What is the currency of the United States?": "Dollar",
        # "What is the hardest natural substance on Earth?": "Diamond",
        # "What is the main ingredient in guacamole?": "Avocado",
        # "What is the square root of 16?": "4",
        # "What is the capital of Italy?": "Rome",
        # "What is 10 - 4?": "6",
        # "Who was the first President of the United States?": "George Washington",
        # "What planet is known as the Red Planet?": "Mars",
        # "What is the longest river in the world?": "Nile",
        # "What element does 'O' represent on the periodic table?": "Oxygen",
        # "Who is known as the Father of Geometry?": "Euclid",
        # "What is the largest mammal in the world?": "Blue whale",
        # "What is the freezing point of water in degrees Celsius?": "0",
        # "Which organ is responsible for pumping blood in the body?": "Heart",
        # "What is the capital of Canada?": "Ottawa",
        # "What is the main language spoken in Brazil?": "Portuguese",
        # "What is 3 * 3?": "9",
        # "What is the primary color of bananas?": "Yellow",
        # "What is the chemical formula for salt?": "NaCl",
        # "Who invented the telephone?": "Alexander Graham Bell",
        # "What is the capital of Australia?": "Canberra",
        # "What is the sum of angles in a triangle?": "180",
        # "What is the largest ocean on Earth?": "Pacific Ocean",
        # "Who wrote the 'Iliad' and the 'Odyssey'?": "Homer",
        # "What is the main ingredient in bread?": "Flour",
        # "What is 15 + 6?": "21",
        # "What is the capital of Spain?": "Madrid",
        # "What type of animal is a dolphin?": "Mammal",
        # "What is the hardest bone in the human body?": "Femur",
        # "What do bees produce?": "Honey",
        # "What is the capital of Germany?": "Berlin",
        # "What is 12 / 4?": "3",
        # "What instrument is used to measure temperature?": "Thermometer",
        # "Who was the first man to walk on the moon?": "Neil Armstrong",
        # "What is the main ingredient in sushi?": "Rice",
        # "What is the capital of India?": "New Delhi",
        # "What is 8 - 3?": "5",
        # "What do you call a baby kangaroo?": "Joey",
        # "What is the primary gas found in the air we breathe?": "Nitrogen",
        # "What is the capital of China?": "Beijing",
        # "What is the name of the fairy in Peter Pan?": "Tinkerbell",
        # "What is the process by which plants make their food?": "Photosynthesis",
        # "What is the capital of Egypt?": "Cairo",
        # "What is the largest desert in the world?": "Sahara",
        # "What is the first letter of the Greek alphabet?": "Alpha",
        # "What is the capital of Russia?": "Moscow",
        # "What is 7 * 7?": "49",
        # "What is the primary ingredient in chocolate?": "Cocoa",
        # "Who painted the ceiling of the Sistine Chapel?": "Michelangelo",
        # "What is the capital of Mexico?": "Mexico City",
        # "What is 100 - 40?": "60",
        "What is the only planet that rotates on its side?": "Uranus",
        "What is the main organ of the human circulatory system?": "Heart",
        "What is the chemical symbol for gold?": "Au",
        "What is the capital of South Africa?": "Pretoria",  # One of the capitals
        "What is 9 + 10?": "19",
        "What is the primary source of energy for the Earth?": "Sun"
    }

    print("Welcome to the Flashcard Quiz!")  # Welcome message
    flashcard_quiz(questions)  # Start the quiz

# Start the application
main()  # Call the main function to run the program
