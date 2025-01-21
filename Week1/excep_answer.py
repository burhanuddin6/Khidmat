# ===============================================
# Bank Account Manager with Exception Handling
# ===============================================

balance = 0.0

# Function: deposit
def deposit():
    global balance
    try:
        amount = float(input("Enter the amount to deposit: "))
        if amount <= 0:
            print("Deposit amount must be positive.")
        else:
            balance += amount
            print(f"${amount:.2f} deposited successfully. New balance: ${balance:.2f}")
    except ValueError:
        print("Invalid amount. Please enter a valid number.")

# Function: withdraw
def withdraw():
    global balance
    try:
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > balance:
            print("Insufficient funds. You cannot withdraw more than the available balance.")
        else:
            balance -= amount
            print(f"${amount:.2f} withdrawn successfully. New balance: ${balance:.2f}")
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Function: check_balance
def check_balance():
    print(f"Your current balance is: ${balance:.2f}")

# Main Program
def main():
    while True:
        print("\nBank Account Manager")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")
        
        try:
            choice = int(input("Select an option (1-4): "))
            if choice == 1:
                deposit()
            elif choice == 2:
                withdraw()
            elif choice == 3:
                check_balance()
            elif choice == 4:
                print("Thank you for using the Bank Account Manager. Goodbye!")
                break
            else:
                print("Invalid option. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid option. Please enter a number between 1 and 4.")

# Start the program
main()