# ===============================================
# Country-Capital Directory
# ===============================================

# Create an empty dictionary to store countries and their capitals
directory = {}

# Function: add_country
def add_country():
    country = input("Enter the country name: ")
    capital = input("Enter the capital city: ")
    directory[country] = capital
    print(f"Added {country} with capital {capital}.")

# Function: view_directory
def view_directory():
    if not directory:
        print("No countries in the directory.")
    else:
        print("\nCountries and their Capitals:")
        for country, capital in directory.items():
            print(f"{country}: {capital}")

# Function: search_capital
def search_capital():
    country = input("Enter the country name to search for its capital: ")
    if country in directory:
        print(f"The capital of {country} is {directory[country]}.")
    else:
        print("Country not found in the directory.")

# Function: update_capital
def update_capital():
    country = input("Enter the country name to update its capital: ")
    if country in directory:
        new_capital = input(f"Enter the new capital for {country}: ")
        directory[country] = new_capital
        print(f"The capital of {country} has been updated to {new_capital}.")
    else:
        print("Country not found.")

# Function: remove_country
def remove_country():
    country = input("Enter the country name to remove: ")
    if country in directory:
        directory.pop(country)
        print(f"{country} has been removed from the directory.")
    else:
        print("Country not found.")

# Main Program
def main():
    while True:
        print("\nCountry-Capital Directory")
        print("1. Add a Country")
        print("2. View Directory")
        print("3. Search for a Capital")
        print("4. Update a Capital")
        print("5. Remove a Country")
        print("6. Exit")
        
        choice = int(input("Select an option (1-6): "))
        
        if choice == 1:
            add_country()
        elif choice == 2:
            view_directory()
        elif choice == 3:
            search_capital()
        elif choice == 4:
            update_capital()
        elif choice == 5:
            remove_country()
        elif choice == 6:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Call main() to start the program
main()