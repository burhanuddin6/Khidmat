# ===============================================
# Student Score Tracker
# ===============================================

# Step 1: Create an empty dictionary to store student names and scores
students = {}

# -----------------------------------------------
# Function: Add Student
# -----------------------------------------------
def add_student():
    name = input("Enter student's name: ")
    score = int(input("Enter student's score: "))
    students[name] = score
    print(f"Student '{name}' with score {score} added successfully.")

# -----------------------------------------------
# Function: Display Students
# -----------------------------------------------
def display_students():
    if len(students) == 0:
        print("No students to display.")
    else:
        print("\nStudents and their scores:")
        for name, score in students.items():
            print(f"{name}: {score}")

# -----------------------------------------------
# Function: Calculate Average Score
# -----------------------------------------------
def calculate_average():
    if len(students) == 0:
        print("No students to calculate an average.")
        return
    total_score = sum(students.values())
    average_score = total_score / len(students)
    print(f"The average score is: {average_score:.2f}")

# -----------------------------------------------
# Main Program Loop
# -----------------------------------------------
def main():
    while True:
        print("\nStudent Score Tracker")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Display Average Score")
        print("4. Exit")
        
        choice = int(input("Select an option (1-4): "))
        
        if choice == 1:
            add_student()
        elif choice == 2:
            display_students()
        elif choice == 3:
            calculate_average()
        elif choice == 4:
            print("Exiting Student Score Tracker. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Call the main function to start the program
main()