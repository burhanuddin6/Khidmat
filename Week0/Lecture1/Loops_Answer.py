# ===============================================
# Library Book Management
# ===============================================

# Create an empty list to store books
books = []

# Function: add_books
def add_books():
    while True:
        title = input("Enter book title (or type 'done' to stop): ")
        if title.lower() == 'done':
            break
        books.append(title)
        print(f"'{title}' has been added to the library.")

# Function: display_books
def display_books():
    if len(books) == 0:
        print("No books available.")
    else:
        print("\nAvailable Books:")
        for index, book in enumerate(books, start=1):
            print(f"{index}. {book}")

# Function: search_book
def search_book():
    title = input("Enter the book title to search: ")
    for book in books:
        if book.lower() == title.lower():
            print("Book found!")
            return
    print("Book not available.")

# Function: remove_book
def remove_book():
    title = input("Enter the title of the book to remove: ")
    if title in books:
        books.remove(title)
        print(f"'{title}' has been removed from the library.")
    else:
        print("Book not found.")

# Main Program
def main():
    while True:
        print("\nLibrary Book Management")
        print("1. Add Books")
        print("2. Display Books")
        print("3. Search for a Book")
        print("4. Remove a Book")
        print("5. Exit")
        
        choice = int(input("Select an option (1-5): "))
        
        if choice == 1:
            add_books()
        elif choice == 2:
            display_books()
        elif choice == 3:
            search_book()
        elif choice == 4:
            remove_book()
        elif choice == 5:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Call main() to start the program
main()