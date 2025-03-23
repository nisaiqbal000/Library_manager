# **Library Manager**

**Library Manager** is a Command-Line Interface (CLI) based Library Management System built in Python. It allows users to manage their personal digital library by adding, removing, searching, and viewing books. The system stores book details in a file and provides an interactive menu for seamless book management.

## **Features**

- **Add a Book 📖**: Input book details (title, author, year, genre, read status) and store them.
- **Remove a Book 🗑️**: Delete a book by its title if it exists.
- **Search for Books 🔍**: Find books by title or author.
- **Display All Books 📚**: View a complete list of books along with their details.
- **Library Statistics 📊**: Get insights like total books and percentage read.
- **Data Persistence 💾**: All book records are saved in a file to ensure they are not lost.
- **CLI-Based Interface 🖥️**: Simple text-based menu for easy interaction.

---

## **How It Works**

1. The program loads existing books from the file (`library.txt`) when started.
2. Users navigate through an interactive menu to manage their library.
3. All updates (adding/removing books) are saved automatically to the file.
4. The program continues running until the user chooses to exit.

Usage
Add a Book:
Choose 1. Add a Book from the menu.
Enter the book details (title, author, year, genre, read status).
Remove a Book:

Choose 2. Remove a Book from the menu.
Enter the title of the book to remove.
Search for Books:

Choose 3. Search for Books from the menu.
Enter the title or author to search.
Display All Books:
Choose 4. Display All Books from the menu.
View all books in the library.

Library Statistics:
Choose 5. Library Statistics from the menu.
View total books and percentage read.

Exit:
Choose 6. Exit to close the program.

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:
Fork the repository.
Create a new branch (git checkout -b feature/YourFeatureName).
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature/YourFeatureName).
Open a pull request.
