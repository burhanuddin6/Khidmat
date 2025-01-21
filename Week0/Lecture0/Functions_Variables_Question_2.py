# ===============================================
# Task List Manager
# ===============================================
# This program manages a list of tasks.
# It allows the user to:
# 1. Add new tasks.
# 2. Remove existing tasks.
# 3. Display all tasks.
# 4. Search for a specific task.
# ===============================================

# TODO 1: Create an empty list named 'tasks' to store the tasks


# -----------------------------------------------
# Function: Add Task
# -----------------------------------------------
# This function adds a new task to the list.
def add_task():
    # TODO 2: Prompt the user to enter a task
    # HINT: Use input() to get the task from the user
    # Add the task to the 'tasks' list using the append() method
    

# -----------------------------------------------
# Function: Remove Task
# -----------------------------------------------
# This function removes an existing task from the list.
def remove_task():
    # TODO 3: Prompt the user to enter the task they want to remove
    # Check if the task exists in the list using 'in' keyword
    # If the task exists, remove it using the remove() method
    # Otherwise, display a message that the task was not found
    

# -----------------------------------------------
# Function: Display Tasks
# -----------------------------------------------
# This function displays all tasks in the list.
def display_tasks():
    # TODO 4: Check if the list is empty
    # If empty, display "No tasks to display."
    # Otherwise, display each task using a loop
    

# -----------------------------------------------
# Function: Search Task
# -----------------------------------------------
# This function searches for a specific task in the list.
def search_task():
    # TODO 5: Prompt the user to enter a task to search for
    # Check if the task exists in the list using 'in' keyword
    # Display an appropriate message based on the result
    

# -----------------------------------------------
# Main Program Loop
# -----------------------------------------------
def main():
    while True:
        print("\nTask List Manager")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Search Task")
        print("5. Exit")
        
        # TODO 6: Prompt the user to select an option (1-5)
        # Use input() to get the user's choice
        # Convert the input to an integer
        

        # TODO 7: Call the appropriate function based on the user's choice
        # HINT: Use if-elif-else statements to handle each option
        
        # TODO 8: Exit the loop if the user selects option 5 (Exit)
        

# Call the main function to start the program
# TODO 9: Call main()