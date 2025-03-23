import os

# File to store book details
LIBRARY_FILE = "library.txt"

# Function to load books from the file
def load_books():
    if not os.path.exists(LIBRARY_FILE):
        return []
    with open(LIBRARY_FILE, "r") as file:
        books = [line.strip().split(",") for line in file.readlines()]
    return books

# Function to save books to the file
def save_books(books):
    with open(LIBRARY_FILE, "w") as file:
        for book in books:
            file.write(",".join(book) + "\n")

# Function to add a book
def add_book(books):
    print("\n📖 Add a Book")
    title = input("Enter the title: ")
    author = input("Enter the author: ")
    year = input("Enter the year: ")
    genre = input("Enter the genre: ")
    read_status = input("Have you read this book? (yes/no): ").lower()
    if read_status not in ["yes", "no"]:
        print("Invalid input for read status. Please enter 'yes' or 'no'.")
        return
    books.append([title, author, year, genre, read_status])
    save_books(books)
    print(f"Book '{title}' added successfully! ✅")

# Function to remove a book
def remove_book(books):
    print("\n🗑️ Remove a Book")
    title = input("Enter the title of the book to remove: ")
    found = False
    for book in books:
        if book[0].lower() == title.lower():
            books.remove(book)
            save_books(books)
            print(f"Book '{title}' removed successfully! ✅")
            found = True
            break
    if not found:
        print(f"Book '{title}' not found. ❌")

# Function to search for books
def search_books(books):
    print("\n🔍 Search for Books")
    search_term = input("Enter the title or author to search: ").lower()
    found_books = [book for book in books if search_term in book[0].lower() or search_term in book[1].lower()]
    if found_books:
        print("\nSearch Results:")
        for book in found_books:
            print(f"Title: {book[0]}, Author: {book[1]}, Year: {book[2]}, Genre: {book[3]}, Read: {book[4]}")
    else:
        print("No books found. ❌")

# Function to display all books
def display_books(books):
    print("\n📚 All Books")
    if not books:
        print("No books in the library. ❌")
    else:
        for book in books:
            print(f"Title: {book[0]}, Author: {book[1]}, Year: {book[2]}, Genre: {book[3]}, Read: {book[4]}")

# Function to display library statistics
def library_statistics(books):
    print("\n📊 Library Statistics")
    total_books = len(books)
    read_books = sum(1 for book in books if book[4] == "yes")
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0
    print(f"Total Books: {total_books}")
    print(f"Books Read: {read_books} ({percentage_read:.2f}%)")

# Main function
def main():
    books = load_books()
    while True:
        print("\n📚 Library Manager")
        print("1. Add a Book 📖")
        print("2. Remove a Book 🗑️")
        print("3. Search for Books 🔍")
        print("4. Display All Books 📚")
        print("5. Library Statistics 📊")
        print("6. Exit 🚪")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_book(books)
        elif choice == "2":
            remove_book(books)
        elif choice == "3":
            search_books(books)
        elif choice == "4":
            display_books(books)
        elif choice == "5":
            library_statistics(books)
        elif choice == "6":
            print("Exiting the program. Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please try again. ❌")

if __name__ == "__main__":
    main()