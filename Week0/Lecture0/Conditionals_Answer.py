# ===============================================
# Grading System
# ===============================================

# -----------------------------------------------
# Function: get_grade
# -----------------------------------------------
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# -----------------------------------------------
# Function: display_message
# -----------------------------------------------
def display_message(score):
    if score % 5 == 0:
        print("Your score is a multiple of 5! Great job!")

# -----------------------------------------------
# Main Program
# -----------------------------------------------
def main():
    print("Welcome to the Grading System!\n")
    
    score = int(input("Enter your score: "))
    
    grade = get_grade(score)
    print(f"Your grade is: {grade}")
    
    display_message(score)

# Call the main function to run the program
main()