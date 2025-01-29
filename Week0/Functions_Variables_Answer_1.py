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
    # HINT: Use the input() function and convert the result to a float.
    num1 = float(input("Enter the first number: "))

    # TODO 2: Prompt the user to enter the second number and store it in a variable
    num2 = float(input("Enter the second number: "))

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
    # HINT: Use input() and ensure it's stored as an integer.
    choice = int(input("\nChoose an operation (1-4): "))

    # -----------------------------------------------
    # Step 4: Perform the chosen operation
    # -----------------------------------------------

    # Call the appropriate function based on the user's choice
    if choice == 1:
        result = add(num1, num2)  # Call the add function
    elif choice == 2:
        result = subtract(num1, num2)  # Call the subtract function
    elif choice == 3:
        result = multiply(num1, num2)  # Call the multiply function
    elif choice == 4:
        result = divide(num1, num2)  # Call the divide function
    else:
        # TODO 4: Handle invalid choices by displaying an error message
        # HINT: Use a print statement to display "Invalid choice!" and return.
        print("Invalid choice!")
        return

    # -----------------------------------------------
    # Step 5: Display the result
    # -----------------------------------------------

    # TODO 5: Display the result using a formatted string
    # HINT: Use an f-string to format and display the result neatly.
    print(f"\nThe result of your operation is: {result}")

# -----------------------------------------------
# Functions for arithmetic operations
# -----------------------------------------------

# Function to add two numbers
def add(a, b):
    """Returns the sum of a and b."""
    return a + b

# TODO 6: Write a function named subtract() that takes two parameters and returns their difference
def subtract(a, b):
    """Returns the difference of a and b."""
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    """Returns the product of a and b."""
    return a * b

# Function to divide two numbers
def divide(a, b):
    """Returns the quotient of a and b. Handles division by zero."""
    # TODO 7: Add a check to ensure b is not zero. If it is, return an error message.
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

# -----------------------------------------------
# Run the main function
# -----------------------------------------------

# TODO 8: Call the main() function to start the program
main()