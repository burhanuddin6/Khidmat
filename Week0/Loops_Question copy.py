# ===============================================
# Library Book Management
# ===============================================
# This program helps manage a collection of books.
# The user can:
# 1. Add new books to the collection.
# 2. Display all available books.
# 3. Search for a book by title.
# 4. Remove a book when borrowed.
# ===============================================

# Create an empty list to store books
books = []

# -----------------------------------------------
# Function: add_books
# -----------------------------------------------
# This function allows the user to add books to the library.
def add_books():
    while True:
        # TODO 1: Ask the user to enter a book title or 'done' to stop adding books
        # If the user enters 'done', break the loop
        # Otherwise, append the title to the 'books' list
        pass

# -----------------------------------------------
# Function: display_books
# -----------------------------------------------
# This function displays all available books in the library.
def display_books():
    # TODO 2: If there are no books in the list, print "No books available."
    # Otherwise, use a for loop to print each book in the list
    pass

# -----------------------------------------------
# Function: search_book
# -----------------------------------------------
# This function searches for a book by its title.
def search_book():
    # TODO 3: Ask the user to enter a book title to search for
    # Use a for loop to check if the book exists in the 'books' list
    # If found, print "Book found!"
    # If not found, print "Book not available."
    pass

# -----------------------------------------------
# Function: remove_book
# -----------------------------------------------
# This function removes a book when it is borrowed.
def remove_book():
    # TODO 4: Ask the user to enter the title of the book to remove
    # If the book exists in the 'books' list, remove it and print "Book removed."
    # If the book does not exist, print "Book not found."
    pass

# -----------------------------------------------
# Main Program
# -----------------------------------------------
def main():
    while True:
        print("\nLibrary Book Management")
        print("1. Add Books")
        print("2. Display Books")
        print("3. Search for a Book")
        print("4. Remove a Book")
        print("5. Exit")
        
        # TODO 5: Ask the user to select an option (1-5)
        # Call the appropriate function based on the user's choice
        pass

# TODO 6: Call main() to start the program
