# Project-3(To-Do List Application)
# Simple To-Do List Application

# Purpose: To create a simple command-line application that allows users to manage tasks by adding, removing, viewing, and marking tasks as completed. This helps users stay organized and keep track of their responsibilities.

# Function to display the menu options to the user
def display_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add a task")       # Option to add a new task
    print("2. View tasks")      # Option to view all tasks
    print("3. Remove a task")   # Option to remove a specific task
    print("4. Exit")            # Option to exit the application

# Function to add a new task to the todo_list
def add_task(todo_list):
    task = input("Enter the task you want to add: ")  # Prompt user for a task
    todo_list.append(task)  # Add the task to the list
    print(f'Task "{task}" added to the list.')  # Confirm the task has been added

# Function to view all tasks in the todo_list
def view_tasks(todo_list):
    if not todo_list:  # Check if the list is empty
        print("Your to-do list is empty.")  # Inform user if no tasks are present
    else:
        print("\n--- Your To-Do List ---")  # Heading for task list
        # Enumerate through the list of tasks to display each one with its index
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")  # Print each task with its corresponding number

# Function to remove a specific task from the todo_list
def remove_task(todo_list):
    view_tasks(todo_list)  # Show current tasks to the user
    if todo_list:  # Proceed only if the list is not empty
        task_index = int(input("Enter the task number you want to remove: ")) - 1  # Prompt user for task number
        # Check if the index is valid
        if 0 <= task_index < len(todo_list):
            removed_task = todo_list.pop(task_index)  # Remove the task from the list
            print(f'Task "{removed_task}" removed from the list.')  # Confirm the removal
        else:
            print("Invalid task number.")  # Inform user if the number is out of range

# Main function to run the To-Do List application
def main():
    todo_list = []  # Initialize an empty list to hold tasks
    while True:  # Loop indefinitely until the user chooses to exit
        display_menu()  # Show the menu options
        choice = input("Choose an option (1-4): ")  # Get user input for menu selection

        # Check user input and call the appropriate function
        if choice == '1':
            add_task(todo_list)  # Call function to add a task
        elif choice == '2':
            view_tasks(todo_list)  # Call function to view tasks
        elif choice == '3':
            remove_task(todo_list)  # Call function to remove a task
        elif choice == '4':
            print("Exiting the To-Do List app. Goodbye!")  # Exit message
            break  # Exit the loop
        else:
            print("Invalid choice. Please select a valid option.")  # Inform user if input is invalid

# Start the app by calling the main function
main()
