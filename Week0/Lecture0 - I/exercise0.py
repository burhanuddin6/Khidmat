# ===============================================
# Simple Calculator Program
# ===============================================
# This program performs basic arithmetic operations
# including addition, subtraction, multiplication,
# and division.
# ===============================================

# Pseudocode (High-Level Steps)
# 1. Display a welcome message.
# 2. Get two numbers from the user.
# 3. Ask the user to choose an operation.
# 4. Perform the operation using a corresponding function.
# 5. Display the result.

# -----------------------------------------------
# Step 1: Welcome Message
# -----------------------------------------------

def main():
    # Display a welcome message to the user
    print("Welcome to the Simple Calculator!")
    print("You can add, subtract, multiply, or divide two numbers.\n")
    
    # -----------------------------------------------
    # Step 2: Get input from the user
    # -----------------------------------------------

    # TODO 1: Prompt the user to enter the first number and store it in a variable
    # HINT: Use input() to get user input and convert it to a float.
    

    # TODO 2: Prompt the user to enter the second number and store it in a variable
    

    # -----------------------------------------------
    # Step 3: Ask the user to choose an operation
    # -----------------------------------------------

    # Display available operations
    print("\nAvailable operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # TODO 3: Get the user's choice (1, 2, 3, or 4) and store it in a variable
    # HINT: Use input() to get user input and convert it to an integer.
    

    # -----------------------------------------------
    # Step 4: Perform the chosen operation
    # -----------------------------------------------

    # Call the appropriate function based on the user's choice
    if choice == 1:
        # TODO 4: Call the add() function with the two numbers as arguments
        pass
    elif choice == 2:
        # TODO 5: Call the subtract() function with the two numbers as arguments
        pass
    elif choice == 3:
        # TODO 6: Call the multiply() function with the two numbers as arguments
        pass
    elif choice == 4:
        # TODO 7: Call the divide() function with the two numbers as arguments
        # HINT: Ensure that division by zero is handled inside the divide() function.
        pass
    else:
        # TODO 8: Handle invalid choices by displaying an error message
        # HINT: Use print() to display "Invalid choice!" and return.
        pass

    # -----------------------------------------------
    # Step 5: Display the result
    # -----------------------------------------------

    # TODO 9: Display the result using a formatted string
    # HINT: Use f-string to format and display the result neatly.
    

# -----------------------------------------------
# Functions for arithmetic operations
# -----------------------------------------------

# TODO 10: Write a function named add() that takes two parameters and returns their sum.
# HINT: Use the return keyword to return the result.
def add(a, b):
    """Returns the sum of a and b."""
    

# TODO 11: Write a function named subtract() that takes two parameters and returns their difference.
def subtract(a, b):
    """Returns the difference of a and b."""
    

# TODO 12: Write a function named multiply() that takes two parameters and returns their product.
def multiply(a, b):
    """Returns the product of a and b."""
    

# TODO 13: Write a function named divide() that takes two parameters and returns their quotient.
# HINT: Check if the second parameter is zero. If it is, return an error message.
def divide(a, b):
    """Returns the quotient of a and b. Handles division by zero."""
    

# -----------------------------------------------
# Run the main function
# -----------------------------------------------

# TODO 14: Call the main() function to start the program