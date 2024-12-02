# Project-2 (Basic Calculator)

# This project implements a simple calculator that can perform basic arithmetic operations:
# addition, subtraction, multiplication, and division. The calculator will continue to run
# until the user chooses to exit. Division by zero is handled to prevent errors.

# Function for addition of two numbers
def add(x, y):
    return x + y

# Function for subtraction of the second number from the first
def subtract(x, y):
    return x - y

# Function for multiplication of two numbers
def multiply(x, y):
    return x * y

# Function for division of the first number by the second
def divide(x, y):
    # Check for division by zero, which is undefined
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Main function to display the menu and handle user input for calculations
def calculator():
    print("Welcome to the Simple Calculator!")
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    # Loop to continue calculations until the user chooses to exit
    while True:
        # Prompt user to select an operation
        choice = input("Enter choice (1/2/3/4/5): ")

        # Exit the calculator if the user chooses option 5
        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        # Check if the user's choice corresponds to a valid operation
        if choice in ['1', '2', '3', '4']:
            # Get input from the user for the numbers to calculate
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            # Perform the chosen operation and display the result
            if choice == '1':
                print(f"The result is: {add(num1, num2)}")  # Call the add function
            elif choice == '2':
                print(f"The result is: {subtract(num1, num2)}")  # Call the subtract function
            elif choice == '3':
                print(f"The result is: {multiply(num1, num2)}")  # Call the multiply function
            elif choice == '4':
                print(f"The result is: {divide(num1, num2)}")  # Call the divide function

        else:
            # Handle invalid inputs that do not match the menu options
            print("Invalid Input. Please select a valid option.")

# Initiating the calculator by calling the main function
calculator()
