# ===============================================
# Country-Capital Directory
# ===============================================
# This program manages a directory of countries and their capitals.
# The user can:
# 1. Add a country and its capital.
# 2. View all countries and their capitals.
# 3. Search for the capital of a specific country.
# 4. Update the capital of a country.
# 5. Remove a country from the directory.
# ===============================================

# Create an empty dictionary to store countries and their capitals
directory = {}

# -----------------------------------------------
# Function: add_country
# -----------------------------------------------
# This function allows the user to add a new country and its capital.
def add_country():
    # TODO 1: Ask the user to enter a country name and its capital.
    # Add the country and capital to the 'directory' dictionary.
    # Hint: Use the dictionary syntax: dictionary[key] = value
    pass

# -----------------------------------------------
# Function: view_directory
# -----------------------------------------------
# This function displays all countries and their capitals.
def view_directory():
    # TODO 2: Check if the directory is empty.
    # If empty, print "No countries in the directory."
    # Otherwise, use a for loop to print each country and its capital.
    pass

# -----------------------------------------------
# Function: search_capital
# -----------------------------------------------
# This function searches for the capital of a specific country.
def search_capital():
    # TODO 3: Ask the user to enter a country name.
    # Check if the country exists in the 'directory' dictionary.
    # If found, print the capital.
    # Otherwise, print "Country not found in the directory."
    pass

# -----------------------------------------------
# Function: update_capital
# -----------------------------------------------
# This function updates the capital of a specific country.
def update_capital():
    # TODO 4: Ask the user to enter a country name.
    # If the country exists, ask for the new capital and update the value.
    # If the country does not exist, print "Country not found."
    pass

# -----------------------------------------------
# Function: remove_country
# -----------------------------------------------
# This function removes a country from the directory.
def remove_country():
    # TODO 5: Ask the user to enter a country name.
    # If the country exists in the dictionary, remove it using the `pop()` method.
    # Otherwise, print "Country not found."
    pass

# -----------------------------------------------
# Main Program
# -----------------------------------------------
def main():
    while True:
        print("\nCountry-Capital Directory")
        print("1. Add a Country")
        print("2. View Directory")
        print("3. Search for a Capital")
        print("4. Update a Capital")
        print("5. Remove a Country")
        print("6. Exit")
        
        # TODO 6: Ask the user to select an option (1-6).
        # Call the appropriate function based on the user's choice.
        pass

# TODO 7: Call main() to start the program