# ===============================================
# Bank Account Manager with Exception Handling
# ===============================================
# This program allows users to:
# 1. Deposit money
# 2. Withdraw money
# 3. Check balance
# 4. Exit the program
# It uses exception handling to catch errors such as:
# - Invalid input (non-numeric values)
# - Withdrawal amount exceeding the balance
# ===============================================

# Initialize account balance
balance = 0.0

# -----------------------------------------------
# Function: deposit
# -----------------------------------------------
def deposit():
    try:
        # TODO 1: Ask the user to enter the deposit amount.
        # Validate that the input is a positive number.
        # Add the deposit amount to the balance and display the updated balance.
        # Hint: Use `float(input())` to accept a floating-point number.
        pass
    except ValueError:
        # TODO 2: Handle cases where the user enters invalid input (e.g., a string).
        print("Invalid amount. Please enter a valid number.")

# -----------------------------------------------
# Function: withdraw
# -----------------------------------------------
def withdraw():
    try:
        # TODO 3: Ask the user to enter the withdrawal amount.
        # Validate that the input is a positive number and not greater than the balance.
        # Deduct the withdrawal amount from the balance and display the updated balance.
        # Hint: Use a conditional to check if the withdrawal amount is valid.
        pass
    except ValueError:
        # TODO 4: Handle cases where the user enters invalid input (e.g., a string).
        print("Invalid amount. Please enter a valid number.")
    except Exception as e:
        # TODO 5: Handle any other unexpected errors and print a generic error message.
        print(f"An unexpected error occurred: {e}")

# -----------------------------------------------
# Function: check_balance
# -----------------------------------------------
def check_balance():
    # TODO 6: Print the current balance in the account.
    print(f"Your current balance is: ${balance:.2f}")

# -----------------------------------------------
# Main Program
# -----------------------------------------------
def main():
    while True:
        print("\nBank Account Manager")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")
        
        try:
            # TODO 7: Ask the user to select an option (1-4).
            # Validate the user's choice and call the appropriate function.
            # If the user enters invalid input, print an error message and prompt again.
            pass
        except ValueError:
            print("Invalid option. Please enter a number between 1 and 4.")

# TODO 8: Call main() to start the program