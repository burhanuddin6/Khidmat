# ===============================================
# Task List Manager
# ===============================================

# Step 1: Create an empty list to store tasks
tasks = []

# -----------------------------------------------
# Function: Add Task
# -----------------------------------------------
def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully.")

# -----------------------------------------------
# Function: Remove Task
# -----------------------------------------------
def remove_task():
    task = input("Enter the task to remove: ")
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' removed successfully.")
    else:
        print(f"Task '{task}' not found.")

# -----------------------------------------------
# Function: Display Tasks
# -----------------------------------------------
def display_tasks():
    if len(tasks) == 0:
        print("No tasks to display.")
    else:
        print("\nTasks List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# -----------------------------------------------
# Function: Search Task
# -----------------------------------------------
def search_task():
    task = input("Enter the task to search for: ")
    if task in tasks:
        print(f"Task '{task}' found in the list.")
    else:
        print(f"Task '{task}' not found.")

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
        
        choice = int(input("Select an option (1-5): "))

        if choice == 1:
            add_task()
        elif choice == 2:
            remove_task()
        elif choice == 3:
            display_tasks()
        elif choice == 4:
            search_task()
        elif choice == 5:
            print("Exiting Task List Manager. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Call the main function to start the program
main()